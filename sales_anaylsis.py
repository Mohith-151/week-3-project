#==============================================================================
# SALES ANAYLSIS PROJECT
#==============================================================================

import pandas as pd

#── Step 1: Loading dataset ──
salesdf = pd.read_csv("sales_data.csv")
print("=" *50)
print("       SALES DATA ANALYSIS REPORT")
print("=" *50)

#── Step 2: Explore the Data. ──
print("\n RAW DATA OVERVIEW: ")
print(f"  SHAPE   : {salesdf.shape[0]} rows x {salesdf.shape[1]} columns")
print(f"  columns : {list(salesdf.columns)}")
print(f"\nData Type:\n {salesdf.dtypes.to_string()}")
print(f"\nMISSING VALES:\n{salesdf.isna().sum().to_string()}")

#── Step 3: Data Cleaning ──
print("\n DATA CLEANING: ")
print("Because there is No missing values. So this step is not required for this dataset.")

#── Step 4: Analyze ──

#Metric 1: Total Revenue
total_revenue = salesdf['Total_Sales'].sum()

#Metric 2: Best Selling Product by quantity
bstproduc_qty = salesdf.groupby('Product')['Quantity'].sum().idxmax()

#Metric 3: Highest Revenue product.
bstproduct_rev = salesdf.groupby('Product')['Total_Sales'].sum().idxmax() 

#Metric 4: Sales By region
region_sales = salesdf.groupby('Region')['Total_Sales'].sum().sort_values(ascending=0)

#Metric 5: Average Oder Value
avg_order = salesdf['Total_Sales'].mean()

#── FINAL STEP: Printing the report: ──
print("\n" + '='*50)
print("     KEY METRICS")
print("\n" + '='*50)
print(f"  TOTAL REVENUE : ₹{total_revenue:,.1f}")
print(f"  BEST SELLER(BY QUANTITY :{bstproduc_qty}")
print(f"  TOP SOLD PRODUCT : {bstproduct_rev}")
print(f"  AVERAGE ODER VALUE : ₹{avg_order:,.2f}")

print("\n   REVENUE BY REGION: ")
print("-"*30)
for reg, rev in region_sales.items():
  print(f"  {reg:<10} : ₹{rev:,.1f}")

print("\n   REVENUE BY PRODUCT:")
print("-"*30)
product_summary = salesdf.groupby('Product')['Total_Sales'].sum().sort_values(ascending=0)
for pdt,rev in product_summary.items():
  print(f"  {pdt:<10} : ₹{rev:,.1f}")

print("\n" + '='*50)
print("   ✅ REPORT COMPLETE")
print("\n" + '='*50)
