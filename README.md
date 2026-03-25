# Sales Data Analysis Report
### Week 3 Project — Introduction to Data Analysis

**Prepared by:** Mohith.M  
**Date:** March 2026  
**Dataset:** sales_data.csv

---

## What I Was Trying to Do

This week's project was about getting comfortable with real data. I picked a sales dataset covering multiple products and regions, and set out to answer three honest questions:

1. How much revenue did the business actually make?
2. Which product was driving the most sales?
3. Which region was performing the best — and by how much?

The dataset was small — 100 rows — but it had enough variety across products, regions, and dates to make the analysis genuinely interesting.

---

## First Look at the Data (Day 1–2)

After installing pandas and loading the CSV, the first thing I did was just *look* at what I had.

```python
import pandas as pd

df = pd.read_csv('sales_data.csv')
print(df.shape)    # (100, 7)
print(df.dtypes)
print(df.head())
```

**Shape:** 100 rows, 7 columns  
**Columns:** `Date`, `Product`, `Quantity`, `Price`, `Customer_ID`, `Region`, `Total_Sales`

The data types looked mostly fine. `Quantity`, `Price`, and `Total_Sales` were all integers, which is what you'd want for arithmetic. `Date` came in as a string — something to fix if I needed monthly trends later.

Products in the dataset: **Laptop, Tablet, Phone, Headphones, Monitor**  
Regions covered: **North, South, East, West**

A clean, structured dataset. Nice to work with.

---

## Data Cleaning (Day 3)

```python
print(df.isnull().sum())
```

| Column | Missing Values |
|--------|---------------|
| Date | 0 |
| Product | 0 |
| Quantity | 0 |
| Price | 0 |
| Customer_ID | 0 |
| Region | 0 |
| Total_Sales | 0 |

Zero missing values across all 7 columns. No duplicates either.

Honestly, this was a bit anticlimactic — I'd spent time reading about `fillna()` and `dropna()` and didn't need any of it here. But I think that's a good lesson too: sometimes the data is clean, and the right move is to just say so and move on, rather than inventing problems to fix.

**Cleaning required: None.** The dataset was ready to analyze as-is.

---

## The Analysis (Day 4)

### Total Revenue

```python
total_revenue = df['Total_Sales'].sum()
print(f'Total Revenue: ₹{total_revenue:,.2f}')
```

**Total Revenue: ₹1,23,65,048.00**

That's a strong number across 100 transactions. It also means the average order value is quite high — which makes sense given that the product mix includes laptops and monitors, not cheap impulse buys.

---

### Average Order Value

```python
avg_order = df['Total_Sales'].mean()
print(f'Average Order Value: ₹{avg_order:,.2f}')
```

**Average Order Value: ₹1,23,650.48**

This is high, and it makes sense — when your product lineup includes laptops at premium prices, the average gets pulled up significantly. If the business ever adds lower-cost accessories, this number will shift a lot.

---

### Best-Selling Product

```python
best_by_qty = df.groupby('Product')['Quantity'].sum().idxmax()
best_by_rev = df.groupby('Product')['Total_Sales'].sum().idxmax()
```

**Best Seller by Quantity: Laptop**  
**Top Revenue Product: Laptop**

Laptop won on both counts — units sold *and* total revenue. That's not always the case (a cheap product can dominate volume while something expensive leads on revenue), but here they aligned. Laptop is clearly the flagship product.

---

### Revenue by Product

```python
product_revenue = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
```

| Product | Revenue |
|---------|---------|
| 💻 Laptop | ₹38,89,210 |
| 📱 Tablet | ₹28,84,340 |
| 📞 Phone | ₹28,59,394 |
| 🎧 Headphones | ₹13,84,033 |
| 🖥️ Monitor | ₹13,48,071 |

A few things stand out here:

- **Laptop leads by a comfortable margin** — almost ₹10 lakh ahead of second place.
- **Tablet and Phone are very close** — only ~₹25,000 separating them. A few more phone sales and they'd flip positions.
- **Headphones and Monitor are bunched together at the bottom** — both solid contributors, but clearly not the stars of the lineup.

---

### Revenue by Region

```python
region_revenue = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
```

| Region | Revenue | Share |
|--------|---------|-------|
| 🟢 North | ₹39,83,635 | 32.2% |
| 🔵 South | ₹37,37,852 | 30.2% |
| 🟡 East | ₹25,19,639 | 20.4% |
| 🔴 West | ₹21,23,922 | 17.2% |

**North is the top-performing region**, but not by a massive margin over South — just about ₹2.5 lakh difference. Together, North and South account for over **62% of total revenue**.

The gap between North+South and East+West is more notable. East and West together bring in ₹46.4 lakh — less than either North or South individually. That's worth investigating: is it fewer customers? Lower-priced products being bought there? Smaller order sizes? The data doesn't tell us *why*, but it flags that something is different.

---

## Summary at a Glance

| Metric | Value |
|--------|-------|
| Total Revenue | ₹1,23,65,048 |
| Total Transactions | 100 |
| Average Order Value | ₹1,23,650 |
| Best Product (Units) | Laptop |
| Best Product (Revenue) | Laptop |
| Top Region | North (₹39,83,635) |
| Weakest Region | West (₹21,23,922) |

---

## What I Actually Learned

**Clean data is a gift, not the norm.** This dataset had zero missing values. In real projects, that almost never happens. I shouldn't expect it — I got lucky here.

**"Best" depends on the question.** I checked best-selling by quantity AND by revenue. They happened to match this time, but they often don't. Always ask: best by *what* measure?

**Regional gaps are a story waiting to be told.** The North-South vs. East-West split is interesting. The numbers show *what* happened, but not *why*. That "why" is where the real business insight would come from — and it would need more data to answer.

**pandas clicked for me around Day 3.** The first two days felt like I was just copying syntax. By Day 3, I was actually thinking in dataframes — groupby this, sort by that, filter for these rows. That shift felt good.

---

## Project Files

```
week3-sales-analysis/
├── sales_analysis.py       # Main analysis script
├── sales_data.csv          # Dataset (100 rows, 7 columns)
├── analysis_report.md      
├── requirements.txt        # pandas: 3.0.1
└── README.md               # This file
```

---
*All figures are based on the provided sample dataset.*
