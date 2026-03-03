# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")

# 2. Load Dataset
df = pd.read_csv("Supermart Grocery Sales - Retail Analytics Dataset.csv")

print("First 5 Rows of Dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# 3. Data Cleaning
df = df.drop_duplicates()

# Convert Order Date to datetime (important)
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')

print("\nData Cleaning Completed!")


# 4. Data Analysis & Visualization


# 1️⃣ Total Sales Over Time
sales_trend = df.groupby('Order Date')['Sales'].sum()

plt.figure(figsize=(10,5))
sales_trend.plot()
plt.title("Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()


# 2️⃣ Top Selling Categories
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(6,4))
sns.barplot(x=category_sales.values, y=category_sales.index)
plt.title("Top Selling Categories")
plt.xlabel("Total Sales")
plt.ylabel("Category")
plt.tight_layout()
plt.show()


# 3️⃣ Region Wise Sales
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(6,4))
sns.barplot(x=region_sales.index, y=region_sales.values)
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()


# 4️⃣ Profit by Category
profit_analysis = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(6,4))
profit_analysis.plot(kind='bar')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.show()


# 5️⃣ Top 10 Customers by Sales
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_customers.values, y=top_customers.index)
plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Customer Name")
plt.tight_layout()
plt.show()



# 5. Conclusion (Print Insights)


print("\nPROJECT INSIGHTS:")
print("- Sales show variation over time.")
print("- Some categories generate higher revenue than others.")
print("- Certain regions contribute more to total sales.")
print("- Profit varies across categories.")
print("- Top 10 customers contribute major portion of revenue.")

print("\nProject Completed Successfully!")