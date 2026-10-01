-- Bank360: example SQL analysis queries
-- Compatible with PostgreSQL / MySQL with minor syntax adjustments.

-- 1. Product penetration
SELECT
    SUM(credit_card) AS credit_card_customers,
    SUM(loan) AS loan_customers,
    SUM(fixed_deposit) AS fd_customers,
    SUM(investment_product) AS investment_customers
FROM banking_customers;

-- 2. Highest-balance customers without investment products
SELECT
    customer_id,
    age,
    monthly_income,
    account_balance,
    credit_score
FROM banking_customers
WHERE investment_product = 0
ORDER BY account_balance DESC, monthly_income DESC
LIMIT 20;

-- 3. Digitally active customers without a credit card
SELECT
    customer_id,
    monthly_income,
    transaction_count,
    digital_usage_pct
FROM banking_customers
WHERE digital_usage_pct >= 65
  AND credit_card = 0
ORDER BY transaction_count DESC;

-- 4. Average metrics by customer segment
SELECT
    customer_segment,
    COUNT(*) AS customers,
    AVG(monthly_income) AS avg_income,
    AVG(account_balance) AS avg_balance
FROM banking_customers
GROUP BY customer_segment
ORDER BY customers DESC;
