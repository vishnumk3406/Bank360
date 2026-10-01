import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from analytics import load_data, kpis, product_penetration, summary_by_segment, top_opportunities

st.set_page_config(
    page_title="Bank360 | Retail Banking Analytics",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank360")
st.caption("Retail banking customer analytics dashboard • Synthetic data for portfolio demonstration")

df = load_data()

# Sidebar filters
st.sidebar.header("Customer Filters")
segment_options = ["All"] + sorted(df["customer_segment"].unique().tolist())
selected_segment = st.sidebar.selectbox("Customer Segment", segment_options)

income_min = int(df["monthly_income"].min())
income_max = int(df["monthly_income"].max())
income_range = st.sidebar.slider(
    "Monthly Income (₹)",
    min_value=income_min,
    max_value=income_max,
    value=(income_min, min(income_max, 250000))
)

digital_only = st.sidebar.checkbox("Digital usage ≥ 50%", value=False)

filtered = df.copy()
if selected_segment != "All":
    filtered = filtered[filtered["customer_segment"] == selected_segment]
filtered = filtered[
    filtered["monthly_income"].between(income_range[0], income_range[1])
]
if digital_only:
    filtered = filtered[filtered["digital_usage_pct"] >= 50]

metrics = kpis(filtered)
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Customers", f'{metrics["customers"]:,}')
c2.metric("Avg. Monthly Income", f'₹{metrics["avg_income"]:,.0f}')
c3.metric("Avg. Account Balance", f'₹{metrics["avg_balance"]:,.0f}')
c4.metric("Total Deposits*", f'₹{metrics["total_balance"]/1e7:,.2f} Cr')
c5.metric("Digitally Active", f'{metrics["digital_users"]:.1f}%')

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Customer Segments")
    seg = summary_by_segment(filtered)
    st.dataframe(seg.style.format({
        "avg_income": "₹{:,.0f}",
        "avg_balance": "₹{:,.0f}",
        "avg_transactions": "{:.1f}",
    }), use_container_width=True, hide_index=True)

with right:
    st.subheader("Product Penetration")
    pen = product_penetration(filtered)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(pen["product"], pen["customers"])
    ax.set_ylabel("Customers")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    st.pyplot(fig)

st.divider()

st.subheader("🎯 Cross-Sell Opportunity View")
st.write(
    "These rule-based recommendations are portfolio-demo logic, not financial advice "
    "and not representative of ICICI Bank's actual internal decision systems."
)

product_options = ["All"] + sorted(df["recommended_product"].unique().tolist())
selected_product = st.selectbox("Recommended Product", product_options)

opps = top_opportunities(
    filtered,
    None if selected_product == "All" else selected_product,
    top_n=15
)

st.dataframe(
    opps.style.format({
        "monthly_income": "₹{:,.0f}",
        "account_balance": "₹{:,.0f}",
    }),
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("🔎 Individual Customer Profile")
customer_id = st.selectbox("Customer ID", filtered["customer_id"].tolist())

cust = filtered[filtered["customer_id"] == customer_id].iloc[0]

a, b, c, d = st.columns(4)
a.metric("Income", f'₹{cust["monthly_income"]:,.0f}')
b.metric("Balance", f'₹{cust["account_balance"]:,.0f}')
c.metric("Credit Score", f'{int(cust["credit_score"])}')
d.metric("Digital Usage", f'{cust["digital_usage_pct"]}%')

st.info(
    f'**Segment:** {cust["customer_segment"]}  |  '
    f'**Recommended product:** {cust["recommended_product"]}'
)

st.caption("*Account-balance aggregation is a synthetic portfolio metric used only for this demonstration.")
