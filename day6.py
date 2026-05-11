import pandas as pd
df = pd.read_csv("sales_data.csv")
df["TOTAL"] = df["QUANTITY"]*df["PRICE"]
print("Dataset :\n")
print(df)

sales_per_product = df.groupby("PRODUCT")["TOTAL"].sum()
print("\n Total Sales Per Product: \n")
print(sales_per_product)
total_revenue =df["TOTAL"].sum()
print("\n Total Revenue:",total_revenue)
top_product = sales_per_product.idxmax()
print("\n Ttop - selling product:",top_product)
sorted_df = df.sort_values(by = "TOTAL",ascending = False)
print("\n data sorted by revenue :\n ")
print(sorted_df)