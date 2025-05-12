import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Srinivas\Downloads\Data Analytics\Python\healthcare-dataset-stroke-data.csv")

print(df.head())

print(df.shape)

print(df.info())

print(df.describe())

print("Unique values in each column:\n", df.nunique())

print(df.isnull().sum())

df['bmi'] = df['bmi'].fillna(df['bmi'].median())

df['smoking_status'] = df['smoking_status'].fillna('Unknown')

df.drop_duplicates(inplace=True)