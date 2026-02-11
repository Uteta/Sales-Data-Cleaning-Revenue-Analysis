import pandas as pd

# Load data set
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print(df.head())

# check missing values
print(df.isnull().sum())

#remove duplicates
df = df.drop_duplicates()

#convert date column
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

#Create revenue column
df['Revenue'] = df['Quantity'] * df['Price']

#save cleaned file
df.to_csv("cleaned_sales_data.csv", index=False)

print("Data cleaning complete.")
