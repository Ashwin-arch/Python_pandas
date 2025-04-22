import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
df = pd.read_csv("sales.csv")

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Calculate Revenue
df['Revenue'] = df['Units_Sold'] * df['Unit_Price']

# Group by Date for daily revenue
daily_revenue = df.groupby('Date')['Revenue'].sum().reset_index()

# Plot the revenue trend
plt.figure(figsize=(10, 5))
plt.plot(daily_revenue['Date'], daily_revenue['Revenue'], marker='o', linestyle='-', color='green')
plt.title("📈 Daily Revenue Trend - Like a Share Market Chart", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Revenue (₹)")
plt.grid(True)
plt.savefig("Sales_graph.jpg")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
