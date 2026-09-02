# ShopX E-Commerce Data Analytics Project

## 📌 Project Overview

This project analyzes ShopX e-commerce sales data to understand business performance, customer behavior, product performance, regional sales, profitability, and discount impact.

The project follows an end-to-end data analytics workflow:

Raw Data → Data Cleaning → Exploratory Data Analysis → Business Insights → Power BI Dashboard → Recommendations

---

## 🎯 Business Questions

- What is the total revenue?
- What is the total profit?
- How many orders were placed?
- How many unique customers are there?
- How many units were sold?
- Which product generates the highest revenue?
- Which category generates the highest revenue and profit?
- Which region and state perform best?
- Which month has the highest revenue?
- Who are the top customers by revenue and profit?
- How do discounts relate to average sales?

---

# 🧹 Data Cleaning

The original dataset contained:

- 12,002 rows
- 14 columns
- 3 missing Customer_ID values
- 2 missing Product_Name values
- 2 missing Discount values
- 2 duplicate rows

### Cleaning Steps

1. Removed duplicate rows.
2. Removed rows with missing Customer_ID.
3. Recovered missing Product_Name using Product_ID.
4. Calculated missing Discount values.
5. Validated the dataset for incorrect values.

### Final Dataset

- 11,997 rows
- 14 columns
- 0 missing values
- 0 duplicate rows

---

# 📊 Key Insights

- ShopX generated approximately **180M in total revenue**.
- ShopX generated approximately **40M in total profit**.
- The overall **profit margin was approximately 21.99%**.
- **April** was the highest-revenue month.
- **Electronics** generated the highest revenue.
- **Electronics** also generated the highest profit.
- The **South** region generated the highest revenue.
- **Telangana** was the highest-revenue state.
- **Laptop Pro 14** generated the highest product revenue and profit.
- **Customer C0574** generated the highest customer revenue.
- **Customer C1041** generated the highest customer profit.
- Higher discounts did not consistently result in higher average sales.

---

# 📈 Python Data Analysis

The Python analysis includes:

- Monthly Sales Trend
- Sales by Category
- Sales by Region
- Top Products by Revenue
- Profit by Category
- Top Customers by Revenue
- Customer Purchase Frequency
- Average Sales by Discount

---

# 📊 Power BI Dashboard

## Page 1 — Executive Dashboard

The executive dashboard provides a high-level overview of business performance.

### KPIs

- Total Revenue
- Total Profit
- Total Orders
- Total Customers
- Total Quantity
- Profit Margin

### Visual Analysis

- Monthly Revenue Trend
- Revenue by Category
- Revenue by Region
- Profit by Category
- Top Products by Revenue

---

## Page 2 — Detailed Sales Analysis

The detailed dashboard allows deeper exploration using interactive slicers.

### Filters

- Region
- Category
- Month

### Visual Analysis

- Top States by Revenue
- Top 5 Customers by Revenue
- Top 5 Customers by Profit
- Product Profit Performance

---

# 💡 Business Recommendations

### 1. Focus on Electronics

Electronics generated the highest revenue and profit, making it the most strategically important category.

### 2. Maintain Laptop Pro 14 Inventory

Laptop Pro 14 performed best in both revenue and profit. Maintaining sufficient inventory can help prevent stock-outs.

### 3. Investigate April Performance

April generated the highest revenue. Further analysis can investigate promotions, pricing, campaigns, or seasonal demand during this period.

### 4. Learn From South and Telangana

The South region and Telangana performed strongly. Successful strategies in these markets could potentially be applied to weaker markets.

### 5. Evaluate Revenue and Profit Separately

Customer C0574 generated the highest revenue, while C1041 generated the highest profit. This shows that high revenue does not always mean high profitability.

---

# 🛠 Tools Used

- Python
- Pandas
- Matplotlib
- Power BI
- VS Code

---

# 📂 Project Structure

```text
ShopX_Data_Analytics/
│
├── Data/
│   ├── shopx_ecommerce_raw.csv
│   └── shopx_ecommerce_cleaned.csv
│
├── analysis/
│   └── analysis.py
│
├── dashboard/
│   └── ShopX Dashboard.pbix
│
└── README.md