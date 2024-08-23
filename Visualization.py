
import pandas as pd
import matplotlib.pyplot as plt 

# Read the cleaned CSV file
df = pd.read_csv('product_group_table.csv')

plt.figure(figsize=(10, 6))
df['ProductGroupID'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Number of ProductsGroupID')
plt.xlabel('GroupName')
plt.ylabel('LastModified')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(8, 8))
df['Category'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'yellowgreen', 'lightblue'])
plt.title('Percentage of Product Types in Main Categories')
plt.ylabel('DateCreated')
plt.show()





# plt.figure(figsize=(10, 6))
# df['GroupName'].value_counts().plot(kind='bar', color='orange')
# plt.title('Number of Products by Group')
# plt.xlabel('Product Group')
# plt.ylabel('Number of Products')
# plt.xticks(rotation=45)
# plt.show()

# Significance: This bar chart helps us see the number of products in each product group. It allows us to easily identify which group has the most products and which has fewer.
