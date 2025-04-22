
# 🐼 Python_Pandas

## 🗓️ Date: 2025-04-05

---

## ✅ Day 1: Getting Started with Pandas

### 1. `df.info()`
- Returns a concise summary of the DataFrame.
- Shows:
  - Column names
  - Non-null counts
  - Data types
  - Memory usage

```python
df.info()
```

---

### 2. `df.describe()`
- Returns summary statistics of numeric columns.
- Includes:
  - Count
  - Mean
  - Std
  - Min, Max
  - 25%, 50%, 75% Quartiles

```python
df.describe()
```

---

### 🧠 What You Learned
- Initial structure and health of your dataset.
- Quick numerical profiling.
- Prepping your data for deeper analysis.

---

## ✅ Day 2: Sales Operations & Visualization

### 1. `df['Revenue'] = df['Units_Sold'] * df['Unit_Price']`
- Adds a new column called `Revenue` to the DataFrame.
- Helps calculate how much revenue each row generated.

```python
df['Revenue'] = df['Units_Sold'] * df['Unit_Price']
```

---

### 2. `df.groupby('Product')['Revenue'].sum()`
- Groups the data by `Product`
- Returns total revenue for each product.

```python
df.groupby('Product')['Revenue'].sum()
```

---

### 3. `df.to_csv("sales_updated.csv", index=False)`
- Saves the modified DataFrame to a new CSV file.
- Prevents writing index numbers into the file.

```python
df.to_csv("sales_updated.csv", index=False)
```

---

### 4. Share-Market Style Line Graph

- Plots revenue per day using `matplotlib`
- X-axis = Date, Y-axis = Revenue

```python
import matplotlib.pyplot as plt

plt.plot(daily_revenue['Date'], daily_revenue['Revenue'])
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.title("📈 Daily Revenue Trend")
plt.show()
```

---

### 🔧 Requirements

Install libraries using:

```bash
pip install pandas matplotlib
```

---

### ✅ Summary

- Read and analyze sales data from CSV
- Performed grouping, aggregation, and created new columns
- Built a share-market style line chart
- Saved the updated CSV with computed fields

---

🚀 Day 3: Coming Soon…
