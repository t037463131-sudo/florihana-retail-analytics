# Florihana Retail and Audience Analytics

A case study by Shun-Min Tang based on work as a Retail Market Research Assistant at Florihana's Taiwan exclusive distributor in 2025. This public narrative was prepared retrospectively in October 2026 from the author's account and a supplied 2025 revenue screenshot. It presents analytical reasoning and decisions without publishing internal customer or advertising records.

## Business questions
- Which audiences engaged with digital marketing, and how should the brand experience reflect their needs?
- How did online revenue compare with individual physical locations?
- How could revenue analysis and recruitment constraints inform a store-closure decision?

## Tools and evidence
Excel was used for monthly revenue review. The author reports reviewing demographic, impression, and click data in Meta-related and Google Ads dashboards, including Facebook, Instagram, and Threads activity. The author also reports conducting interviews and surveys with 50+ primarily female Taiwanese customers. Advertising exports, respondent-level records, and an operating-cost ledger are not included in this public package.

## Main findings
Women aged 30 and above were identified as a key engaged audience based on the author's dashboard review. Engagement demographics should not be treated as a verified purchaser profile without transaction-level evidence.

Reported online revenue represented approximately 35.2% of annual revenue and was the largest individual reported channel. Physical locations together still represented the majority. This channel mix is a descriptive finding for this business and period, not evidence of a general consumer preference for online shopping.

The Hsinchu store recorded average monthly revenue of approximately NT$321K over January–June. March revenue was NT$409,449, so it would be incorrect to describe every month as below NT$410K. The author reports that weak performance and recruitment difficulties informed its closure at the end of June 2025.

## Actions and business contribution
According to the author's account, audience and customer insights informed calming website imagery, a relaxed in-store environment, and messaging around self-care and independence. The desired experience emphasized product exploration and freedom from sales pressure. Revenue analysis and staffing constraints supported review of the Hsinchu location and its June closure.

## Outcomes and evidence limits
The case demonstrates audience analysis, channel comparison, and decision support. No measured sales uplift, conversion improvement, or quantified savings is claimed. A store-closure decision can limit future operating exposure, but six months of avoided losses cannot be calculated from revenue alone. No causal effect of the creative or in-store changes has been established.

## Files
- `case_study.md`: analytical approach, actions, and evidence boundaries
- `findings_summary.csv`: compact public summary with evidence status

## Privacy and preparation
Original revenue sheets, advertising-account screenshots, customer responses, and identifying account details are omitted. The public case uses rounded business aggregates and author-reported activities. Confirm the distributor permits disclosure of these aggregates before publishing. This repository documents a case, not a runnable advertising-data pipeline.

## Author
Shun-Min Tang. Public case narrative organized with AI assistance in October 2026; underlying work is described as performed in 2025.

## New Python portfolio extension
`revenue_analysis.py` was created in October 2026 to reproduce selected revenue calculations. The 2025 work described above used Excel and advertising dashboards; this extension does not imply Python was used during that employment.

The script validates month keys and revenue values, calculates online share and consecutive-month revenue changes, and computes the observed-store monthly mean while preserving blank months. It uses the Python standard library; no additional packages are required.

### Run with authorized source data
```bash
python3 revenue_analysis.py monthly_revenue.csv --output analysis_output.json
```

Provide a CSV with columns `month,total_revenue,online_revenue,hsinchu_revenue`. The private source CSV is not distributed, so this repository cannot be run end to end without authorized input. See `validation_notes.md` for results checked against the supplied revenue screenshot. No advertising-data analysis is implemented because campaign exports were not supplied.
