import pandas as pd
import numpy as np

PRODUCTS = [
    "Investment / Wealth Product",
    "Fixed Deposit / Savings",
    "Personal Loan",
    "Credit Card",
    "Digital Banking Onboarding",
    "Relationship Deepening",
]

def load_data(path="data/banking_customers.csv"):
    return pd.read_csv(path)

def kpis(df):
    return {
        "customers": len(df),
        "avg_income": df["monthly_income"].mean(),
        "avg_balance": df["account_balance"].mean(),
        "total_balance": df["account_balance"].sum(),
        "digital_users": (df["digital_usage_pct"] >= 50).mean() * 100,
    }

def product_penetration(df):
    return pd.DataFrame({
        "product": ["Credit Card", "Loan", "Fixed Deposit", "Investment Product"],
        "customers": [
            df["credit_card"].sum(),
            df["loan"].sum(),
            df["fixed_deposit"].sum(),
            df["investment_product"].sum(),
        ]
    })

def top_opportunities(df, product=None, top_n=10):
    data = df.copy()
    if product:
        data = data[data["recommended_product"] == product]
    cols = [
        "customer_id", "age", "monthly_income", "account_balance",
        "transaction_count", "credit_score", "customer_segment",
        "recommended_product"
    ]
    data = data.sort_values(
        ["account_balance", "monthly_income"], ascending=False
    )
    return data[cols].head(top_n)

def summary_by_segment(df):
    return (
        df.groupby("customer_segment")
        .agg(
            customers=("customer_id", "count"),
            avg_income=("monthly_income", "mean"),
            avg_balance=("account_balance", "mean"),
            avg_transactions=("transaction_count", "mean"),
        )
        .reset_index()
        .sort_values("customers", ascending=False)
    )
