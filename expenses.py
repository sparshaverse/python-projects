import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('expenses.csv')


df.plot(x='Category', y='Amount', kind='bar',color='purple')
plt.title('Monthly Expenses')
plt.xlabel("Category")
plt.ylabel("Amount ($)")
plt.show()