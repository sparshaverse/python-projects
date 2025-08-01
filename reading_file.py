import pandas as pd

df = pd.read_csv('C:/Users/Sparsha/Desktop/data.csv')


print("First 5 rows:")
print(df.head())


print("\nMissing Values Count:")
print(df.isnull().sum())