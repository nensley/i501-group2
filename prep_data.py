# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# open dataframe to work with
df = pd.read_csv("adult.data.csv")

# remove the leading space of every value in columns containing string data
df['sex'] = df['sex'].str.strip()
df['workclass'] = df['workclass'].str.strip()
df['education'] = df['education'].str.strip()
df['marital-status'] = df['marital-status'].str.strip()
df['occupation'] = df['occupation'].str.strip()
df['relationship'] = df['relationship'].str.strip()
df['race'] = df['race'].str.strip()
df['native-country'] = df['native-country'].str.strip()
df['income'] = df['income'].str.strip()

# Confirmation of the number of missing values
df = df.replace('?', np.nan)
missing_per_column = df.isnull().sum() # number of missing values regarding columns 
missing_rows_count = data.isnull().any(axis=1).sum() # number of rows having at lease one missing value 
plt.figure(figsize=(10, 6))
missing_per_column.plot(kind='bar', color='skyblue')
plt.title('Number of Missing Values per Column')
plt.xlabel('Variables')
plt.ylabel('Missing Value Count')
plt.xticks(rotation=45)
plt.show()
print(f'Total number of rows with missing values: {missing_rows_count}')

# Remove rows with missing values
df = df.dropna()
