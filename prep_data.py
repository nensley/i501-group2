# import pandas and numpy
import pandas as pd
import numpy as np

# open dataframe to work with
df = pd.read_csv("adult.data.csv")

# remove missing values

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