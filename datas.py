import pandas as pd

data  = {"Name:['Alice', 'Bob', 'Charlie],"
"Age":[25, 31, 20],
"Salary":[50000, 25000, 33000]}


df = pd.DataFrame(data)

print("Summary Statistics:")
print(df.describe())