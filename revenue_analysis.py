"""Analyze monthly revenue using Python standard library only.
Usage: python3 revenue_analysis.py monthly_revenue.csv --output analysis_output.json
Input columns: month,total_revenue,online_revenue,hsinchu_revenue
Blank store values mean unavailable/not operating, not zero sales.
"""
import argparse
import csv
import json
import math
from datetime import datetime
from pathlib import Path


def amount(value, required=False):
    text = str(value or "").strip().replace(",", "")
    if not text:
        if required:
            raise ValueError("Missing required revenue value")
        return None
    result = float(text)
    if not math.isfinite(result) or result < 0:
        raise ValueError("Revenue must be finite and nonnegative")
    return result


def analyze(path):
    records = []
    seen = set()
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        expected = {"month", "total_revenue", "online_revenue", "hsinchu_revenue"}
        if not expected.issubset(reader.fieldnames or []):
            raise ValueError("Missing required columns")
        for row in reader:
            month = row["month"].strip()
            parsed = datetime.strptime(month, "%Y-%m")
            if parsed.strftime("%Y-%m") != month or month in seen:
                raise ValueError("Invalid or duplicated month")
            seen.add(month)
            total = amount(row["total_revenue"], True)
            online = amount(row["online_revenue"], True)
            store = amount(row["hsinchu_revenue"])
            if online > total or (store is not None and store > total):
                raise ValueError("Channel revenue exceeds total")
            records.append(dict(month=month, total=total, online=online, store=store))
    if not records:
        raise ValueError("Input has no data rows")
    records.sort(key=lambda row: row["month"])
    if len({r["month"][:4] for r in records}) != 1:
        raise ValueError("Use one calendar year per analysis")
    total = sum(r["total"] for r in records)
    online = sum(r["online"] for r in records)
    store_rows = [r for r in records if r["store"] is not None]
    monthly = []
    previous = None
    for row in records:
        consecutive = previous is not None and (
            int(row["month"][5:]) - int(previous["month"][5:]) == 1)
        monthly.append({
            "month": row["month"],
            "online_share_pct": round(100 * row["online"] / row["total"], 4) if row["total"] else None,
            "total_revenue_mom_pct": round(100 * (row["total"] / previous["total"] - 1), 4)
                if consecutive and previous["total"] else None,
        })
        previous = row
    return {
        "reported_month_count": len(records),
        "full_calendar_year": len(records) == 12,
        "online_share_pct": round(100 * online / total, 4) if total else None,
        "hsinchu_observed_months": [r["month"] for r in store_rows],
        "hsinchu_observed_monthly_mean": round(sum(r["store"] for r in store_rows) / len(store_rows), 2)
            if store_rows else None,
        "monthly_metrics": monthly,
        "limitations": [
            "Blank store months excluded, not imputed as zero.",
            "Revenue data alone cannot establish profit, avoided losses, or causal marketing impact.",
            "Total minus online is a residual, not an independently verified physical-store total.",
            "Input totals must be reconciled with source accounting records.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=Path("analysis_output.json"))
    args = parser.parse_args()
    results = analyze(args.input)
    args.output.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
