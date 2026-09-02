import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('shopx_ecommerce_raw.csv')

print("shape:")
print(df.shape)


print("\nINFO:")
df.info()



print("\nduplicated values:")
print(df.duplicated().sum())

print("\nBEFORE removing duplicates:")
print(df.shape)

df = df.drop_duplicates()

print("\nAFTER removing duplicates:")
print(df.shape)

print("\nBEFORE removing missing Customer_ID:")
print(df.shape)

df = df.dropna(subset=["Customer_ID"])

print("\nAFTER removing missing Customer_ID:")
print(df.shape)

print(df[df["Product_ID"].isin(["P011", "P009"])][["Product_ID", "Product_Name"]].drop_duplicates())

print("\nROWS WITH MISSING PRODUCT NAME:")
print(df[df["Product_Name"].isnull()])

df.loc[
    (df["Product_ID"] == "P011") & (df["Product_Name"].isnull()),
    "Product_Name"
] = "Office Chair"

df.loc[
    (df["Product_ID"] == "P009") & (df["Product_Name"].isnull()),
    "Product_Name"
] = "Backpack"




print("\nROWS WITH MISSING DISCOUNT:")
print(df[df["Discount"].isnull()])

df.loc[df["Discount"].isnull(), "Discount"] = (
    1 - (
        df["Sales"] /
        (df["Unit_Price"] * df["Quantity"])
    )
)

print("\nFINAL MISSING VALUES:")
print(df.isnull().sum())

print("\nFINAL DUPLICATES:")
print(df.duplicated().sum())

print("\nFINAL SHAPE:")
print(df.shape)

(df["Sales"] < 0).sum()

(df["Profit"] < 0).sum()

(df["Quantity"] <= 0).sum()


total_revenue = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)

print("Total Revenue:", total_revenue)

total_units_sold = df["Quantity"].sum()

print("Total Units Sold:", total_units_sold)

total_orders = df["Order_ID"].nunique()

print("Total Orders:", total_orders)


total_customers = df["Customer_ID"].nunique()

print("Total Unique Customers:", total_customers)


average_order_value = total_revenue / total_orders

print("Average Order Value:", average_order_value)

profit_margin = (total_profit / total_revenue) * 100

print("Profit Margin:", profit_margin, "%")

product_sales = df.groupby("Product_Name")["Sales"].sum()

print("Product Sales:", product_sales)

best_product = product_sales.idxmax()

print("Best Product:", best_product)

total_quantity_sold = df.groupby("Product_Name")["Quantity"].sum()

highest_sold_out_product = total_quantity_sold.idxmax()

print("Most Units Sold Product:", highest_sold_out_product)
print("Units Sold:", total_quantity_sold.max())

category_sales = df.groupby("Category")["Sales"].sum()

highest_revenue_category = category_sales.idxmax()

print("Highest Revenue Category:", highest_revenue_category)
print("Category Revenue:", category_sales.max())

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\nSALES BY CATEGORY:")
print(category_sales)


category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

print("\nPROFIT BY CATEGORY:")
print(category_profit)

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print("\nSALES BY REGION:")
print(region_sales)

highest_sales_region = region_sales.idxmax()

print("\nHighest Sales Region:", highest_sales_region)
print("Highest Region Sales:", region_sales.max())

state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False)

print("\nSALES BY STATE:")
print(state_sales)

top_state = state_sales.idxmax()

print("\nTop Sales State:", top_state)
print("State Revenue:", state_sales.max())

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.month_name()

monthly_sales = (
    df.groupby(["Month", "Month_Name"])["Sales"]
    .sum()
    .reset_index()
    .sort_values("Month")
)

plt.figure(figsize=(10, 5))

plt.bar(monthly_sales["Month_Name"], monthly_sales["Sales"])

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))

plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=30)
plt.tight_layout()

plt.show()

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))

plt.bar(region_sales.index, region_sales.values)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.show()

top_products = (
    df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

plt.bar(top_products.index, top_products.values)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))

plt.bar(category_profit.index, category_profit.values)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.xticks(rotation=30)
plt.tight_layout()

plt.show()

top_customers = (
    df.groupby("Customer_ID")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 CUSTOMERS BY REVENUE:")
print(top_customers)

plt.figure(figsize=(12, 6))

plt.bar(top_customers.index, top_customers.values)

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

customer_orders = (
    df.groupby("Customer_ID")["Order_ID"]
    .nunique()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 CUSTOMERS BY NUMBER OF ORDERS:")
print(customer_orders)

most_frequent_customer = customer_orders.idxmax()

print("Most Frequent Customer:", most_frequent_customer)
print("Number of Orders:", customer_orders.max())

plt.figure(figsize=(12, 6))

plt.bar(customer_orders.index, customer_orders.values)

plt.title("Top 10 Customers by Number of Orders")
plt.xlabel("Customer ID")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


discount_sales = df.groupby("Discount")["Sales"].mean().sort_index()

print("\nAVERAGE SALES BY DISCOUNT:")
print(discount_sales)


plt.figure(figsize=(10, 5))

plt.bar(
    [f"{x:.0%}" for x in discount_sales.index],
    discount_sales.values
)

plt.title("Average Sales by Discount")
plt.xlabel("Discount")
plt.ylabel("Average Sales")

plt.tight_layout()
plt.show()

df.to_csv("shopx_ecommerce_cleaned.csv", index=False)

print("Cleaned dataset saved successfully!")

print("\n" + "=" * 40)
print("SHOPX BUSINESS DASHBOARD")
print("=" * 40)

print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Profit: ₹{total_profit:,.2f}")
print(f"Total Units Sold: {total_units_sold:,}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")

print("=" * 40)