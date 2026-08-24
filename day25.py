import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1. READ TRANSACTION DATA
# ==============================

file_path = "transactions.csv"

df = pd.read_csv(file_path)

print("\n========== TRANSACTION DATA ==========")
print(df.head())

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# ==============================
# 2. BASIC INFORMATION
# ==============================

print("\n========== DATA INFORMATION ==========")
print(df.info())

print("\nTotal Transactions:", len(df))
print("Total Amount:", df["Amount"].sum())


# ==============================
# 3. DETECT DUPLICATE TRANSACTIONS
# ==============================

duplicates = df[df.duplicated(keep=False)]

print("\n========== DUPLICATE TRANSACTIONS ==========")

if len(duplicates) > 0:
    print(duplicates)
else:
    print("No duplicate transactions found.")


# ==============================
# 4. HIGH VALUE TRANSACTIONS
# ==============================

threshold = 50000

high_value = df[df["Amount"] > threshold]

print("\n========== HIGH VALUE TRANSACTIONS ==========")
print(high_value)

print("\nNumber of High Value Transactions:", len(high_value))


# ==============================
# 5. FREQUENT / SUSPICIOUS ACCOUNTS
# ==============================

transaction_count = df["Account"].value_counts()

print("\n========== ACCOUNT TRANSACTION COUNT ==========")
print(transaction_count)

# Account making more than 5 transactions
frequent_accounts = transaction_count[transaction_count > 5].index

suspicious_accounts = df[
    df["Account"].isin(frequent_accounts)
]

print("\n========== SUSPICIOUS ACCOUNTS ==========")
print(suspicious_accounts)


# ==============================
# 6. CREATE RISK SCORE
# ==============================

def calculate_risk(row):

    score = 0

    # High amount
    if row["Amount"] > threshold:
        score += 50

    # Frequent account
    if row["Account"] in frequent_accounts:
        score += 30

    # Duplicate transaction
    if df.duplicated(
        subset=["Account", "Amount", "Date"],
        keep=False
    ).loc[row.name]:
        score += 20

    return score


df["Risk_Score"] = df.apply(calculate_risk, axis=1)


# ==============================
# 7. RISK LEVEL
# ==============================

def risk_level(score):

    if score >= 70:
        return "High Risk"

    elif score >= 40:
        return "Medium Risk"

    else:
        return "Low Risk"


df["Risk_Level"] = df["Risk_Score"].apply(risk_level)


print("\n========== RISK ANALYSIS ==========")
print(
    df[
        [
            "Transaction_ID",
            "Account",
            "Amount",
            "Risk_Score",
            "Risk_Level"
        ]
    ]
)


# ==============================
# 8. SUSPICIOUS TRANSACTIONS
# ==============================

suspicious_transactions = df[
    df["Risk_Score"] >= 40
]

print("\n========== SUSPICIOUS TRANSACTIONS ==========")
print(suspicious_transactions)


# ==============================
# 9. EXPORT SUSPICIOUS TRANSACTIONS
# ==============================

suspicious_transactions.to_csv(
    "suspicious_transactions.csv",
    index=False
)

print(
    "\nSuspicious transactions exported to "
    "'suspicious_transactions.csv'"
)


# ==============================
# 10. TRANSACTION CATEGORY CHART
# ==============================

category_count = df["Category"].value_counts()

plt.figure(figsize=(8, 5))

category_count.plot(kind="bar")

plt.title("Transaction Category Distribution")
plt.xlabel("Transaction Category")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.show()


# ==============================
# 11. DAILY TRANSACTION TREND
# ==============================

daily_transactions = df.groupby("Date")["Amount"].sum()

plt.figure(figsize=(10, 5))

daily_transactions.plot(kind="line", marker="o")

plt.title("Daily Transaction Trend")
plt.xlabel("Date")
plt.ylabel("Transaction Amount")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ==============================
# 12. TOP 10 HIGHEST TRANSACTIONS
# ==============================

top_10 = df.nlargest(10, "Amount")

print("\n========== TOP 10 HIGHEST TRANSACTIONS ==========")
print(
    top_10[
        [
            "Transaction_ID",
            "Account",
            "Amount",
            "Category"
        ]
    ]
)

plt.figure(figsize=(10, 5))

plt.bar(
    top_10["Transaction_ID"].astype(str),
    top_10["Amount"]
)

plt.title("Top 10 Highest Transactions")
plt.xlabel("Transaction ID")
plt.ylabel("Amount")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ==============================
# 13. FINAL SUMMARY
# ==============================

print("\n========== FINAL SUMMARY ==========")

print("Total Transactions:", len(df))
print("Duplicate Transactions:", len(duplicates))
print("High Value Transactions:", len(high_value))
print("Suspicious Transactions:", len(suspicious_transactions))

print(
    "\nFraud Detection & Transaction Analysis Completed Successfully!"
)