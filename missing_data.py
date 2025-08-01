import pandas as pd
import numpy as np

data = {'Age':[25, np.nan, 30], 'Salary':[50000, 60000, np.nan]}
df = pd.DataFrame(data)

print("Before Filling:")
print(df)

df_filled = df.fillna(df.mean())

print("After filling Missing Values:")
print(df_filled)