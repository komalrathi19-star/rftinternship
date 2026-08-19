import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("sales_data.csv")

print("\nOriginal Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# ==========================================
# 2. CLEAN DATA
# ==========================================

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Convert Sales column to numeric
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

# Remove rows where important values are missing
df = df.dropna(subset=["Date", "Customer", "Product", "Category", "Sales"])

# Remove invalid sales values
df = df[df["Sales"] >= 0]

print("\nCleaned Dataset:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# ==========================================
# 3. TOTAL SALES & AVERAGE REVENUE
# ==========================================

total_sales = df["Sales"].sum()
average_revenue = df["Sales"].mean()

print("\n========== SALES SUMMARY ==========")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Average Revenue per Sale: ₹{average_revenue:,.2f}")

# ==========================================
# 4. TOP 5 CUSTOMERS
# ==========================================

top_customers = (
    df.groupby("Customer")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n========== TOP 5 CUSTOMERS ==========")
print(top_customers)

# ==========================================
# 5. SALES TREND - LINE CHART
# ==========================================

daily_sales = (
    df.groupby("Date")["Sales"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(10, 5))
plt.plot(daily_sales.index, daily_sales.values, marker="o")

plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales Revenue")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# 6. TOP PRODUCTS - BAR CHART
# ==========================================

top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n========== TOP 5 PRODUCTS ==========")
print(top_products)

plt.figure(figsize=(8, 5))
top_products.plot(kind="bar")

plt.title("Top 5 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ==========================================
# 7. CATEGORY DISTRIBUTION - PIE CHART
# ==========================================

category_sales = df.groupby("Category")["Sales"].sum()

print("\n========== CATEGORY DISTRIBUTION ==========")
print(category_sales)

plt.figure(figsize=(7, 7))
plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Distribution by Category")
plt.tight_layout()
plt.show()

# ==========================================
# 8. BUSINESS INSIGHTS
# ==========================================

best_customer = top_customers.index[0]
best_customer_sales = top_customers.iloc[0]

best_product = top_products.index[0]
best_product_sales = top_products.iloc[0]

best_category = category_sales.idxmax()
best_category_sales = category_sales.max()

print("\n========== 5 BUSINESS INSIGHTS ==========")

print(f"1. {best_customer} is the top customer with sales of ₹{best_customer_sales:,.2f}.")

print(f"2. {best_product} is the best-performing product with sales of ₹{best_product_sales:,.2f}.")

print(f"3. {best_category} is the highest-revenue category with sales of ₹{best_category_sales:,.2f}.")

print(f"4. The average revenue per transaction is ₹{average_revenue:,.2f}.")

print("5. The sales trend can be used to identify high-performing and low-performing dates for better business planning.")