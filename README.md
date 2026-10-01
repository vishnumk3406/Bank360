# Bank360 | Retail Banking Customer Analytics

Bank360 is a portfolio project that demonstrates how customer data can be used
for segmentation, customer profiling, product-penetration analysis and
rule-based cross-sell opportunity identification.

> **Important:** The included dataset is entirely synthetic. The product
> recommendation logic is a demonstration and is not representative of any
> bank's internal models or policies.

## Why this project

This project is intentionally designed around four themes:
- Customer 360 / customer profiling
- Data Science & Analytics
- Digital/customer engagement
- Business-oriented insight generation

## Features

### Dashboard
- Customer segment filters
- Income range filter
- Digital-usage filter
- KPI cards
- Segment summary
- Product penetration chart
- Cross-sell opportunity table
- Individual customer profile

### Analytics
- Affluent
- Digitally Active
- Savings Potential
- Credit Potential
- Mass Retail

### Example recommendation logic
The project uses transparent business rules rather than a black-box ML model.
This makes the reasoning easy to explain in an interview.

## Run locally

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

## Project structure

```text
Bank360/
├── app.py
├── analytics.py
├── queries.sql
├── requirements.txt
├── README.md
└── data/
    └── banking_customers.csv
```

## Interview talking points

### Problem
Banks have many customer records, but raw records do not directly show
which customers may be suitable for deeper engagement.

### Approach
1. Clean/derive customer metrics.
2. Create interpretable customer segments.
3. Measure product penetration.
4. Apply explainable recommendation rules.
5. Present results through an interactive dashboard.

### Limitations
- Synthetic data
- Rule-based recommendations
- No actual bank policy or product eligibility model
- No causal inference or predictive validation

## Possible next version

A future version could compare the rule-based system with a supervised model,
add model evaluation, introduce time-series transaction behavior, and deploy
the application with a cloud database.
