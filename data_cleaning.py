"""
Sales Data Cleaning & Revenue Analysis
Author: Uwase Laetitia Uteta
Description: This script load raw sales data,cleans it,and creates a revenue column for analysis with basic insights.
"""
import pandas as pd

# ------------------------------
# 1. Load data set
# ------------------------------
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("First 5 rows of raw data:")
print(df.head())

# -------------------------------
# 2. Handle  missing values
# -------------------------------
# Fill missing Quantity or Price with 0
df['Quantity'] = df['Quantity'].fillna(0)
df['Price'] = df['Price'].fillna(0)

# Drop rows with missing Order_Date
df = df.dropna(subset=['Order_Date'])

# -------------------------------
# 3. Standardize column names
# -------------------------------
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# -------------------------------
# 4. Remove duplicate records
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# 5. Convert date column
# -------------------------------
df['order_date'] = pd.to_datetime(df['order_date'])

# -------------------------------
# 6. Create revenue column
# -------------------------------
df['revenue'] = df['quantity'] * df['price']

# -------------------------------
# 7. Save cleaned dataset
# -------------------------------
df.to_csv("cleaned_sales_data.csv", index=False)
print("Cleanded data saved to 'cleaned_sales_data.csv'.")


