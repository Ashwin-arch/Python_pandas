import pandas as pd

# New dataset: Sales
data = {
    "Date": ["2024-04-01", "2024-04-01", "2024-04-02", "2024-04-02", "2024-04-03"],
    "Product": ["Pen", "Notebook", "Pen", "Eraser", "Notebook"],
    "Units_Sold": [10, 5, 12, 8, 6],
    "Unit_Price": [5, 25, 5, 3, 25]
}

# Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_csv("sales.csv", index=False)

print("sales.csv created ✅")
