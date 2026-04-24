import pandas as pd

# Load dataset
df = pd.read_csv("superstore.csv", encoding='latin1')

# Clean data
df.dropna(inplace=True)

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create new columns
df['Month'] = df['Order Date'].dt.to_period('M')

# 1. Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

# 2. Category Performance
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

# 3. Region Performance
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

# 4. Top 10 Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

print("\nMonthly Sales:\n", monthly_sales.head())
print("\nCategory Sales:\n", category_sales)
print("\nRegion Sales:\n", region_sales)
print("\nTop Products:\n", top_products)
