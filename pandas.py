import pandas as pd

# Import CSV file into DataFrame
df = pd.read_csv('sale_table.csv')

# Display the first 15 rows to check the data
print("\nSample data:")
print(df.head(15))

# Check the number of blank values ​​in each column
missing_data = df.isnull().sum()
print("Number of blank values ​​in each column:")
print(missing_data)

# Remove rows with any blank values
df_cleaned = df.dropna()
print(df_cleaned)

# # Remove columns with any blank values
# df_cleaned = df.dropna(axis=1)
# print(df_cleaned)

# # Hoặc loại bỏ các hàng có giá trị trống trong một cột cụ thể
# df_cleaned = df.dropna(subset=['LastPurchaseDate'])

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('cleaned_file.csv', index=False)
print("Data cleaned and saved to cleaned_file.csv successfully.")

