# MINI EDA DASHBOARD (COMBINED)
# DAY 15 PROJECT
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# -----------------------------
# SAMPLE DATASET
# -----------------------------
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 170, 160, 200, 220],
    "Profit": [20, 25, 30, 28, 35, 40]
}
df = pd.DataFrame(data)
# -----------------------------
# CREATE SUBPLOTS
# -----------------------------
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
# -----------------------------
# 1. LINE CHART (TREND)
# -----------------------------
axes[0].plot(df["Month"], df["Sales"], marker='o')
axes[0].set_title("Sales Trend")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Sales")

# -----------------------------
# 2. BAR CHART (COMPARISON)
# -----------------------------
axes[1].bar(df["Month"], df["Profit"])
axes[1].set_title("Profit Comparison")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Profit")

# -----------------------------
# 3. HISTOGRAM (DISTRIBUTION)
# -----------------------------
sns.histplot(df["Sales"], bins=5, kde=True, ax=axes[2])
axes[2].set_title("Sales Distribution")

# -----------------------------
# SHOW PLOTS
# -----------------------------
plt.tight_layout()
plt.show()

# -----------------------------
# INSIGHTS
# -----------------------------
print("INSIGHTS:")
print("1. Sales show an overall increasing trend.")
print("2. Profit is highest in June.")
print("3. Most sales values are between 150 and 220.")
print("4. No major outliers are visible in the dataset.")