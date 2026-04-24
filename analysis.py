import pandas as pd

# Load dataset
df = pd.read_csv("superstore.csv")

# Basic cleaning
df.dropna(inplace=True)

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Monthly sales
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()

# Top categories
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

print(monthly_sales.head())
print(category_sales)
