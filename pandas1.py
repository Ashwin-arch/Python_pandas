import pandas as pd
df=pd.read_csv("student.csv")
print("First Few rows")
print(df.head())
print("Info:\n")
print(df.info())
print("Description")
print(df.describe())