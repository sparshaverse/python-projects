import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

print(df.info())
print(df.describe())

sns.countplot(x='class', data=df, hue='survived')
plt.title("Passenger class vs Survival")
plt.show()