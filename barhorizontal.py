import pandas as pd
import matplotlib.pyplot as plt

data = {'Product': ["A", "B", "C", "D"],
        'Quantity': [120, 109, 159, 162]}

df = pd.DataFrame(data)


df.plot(x='Product', y='Quantity', kind='barh', color='orange')
plt.title('Product Quantities')
plt.xlabel('Quantity')
plt.ylabel('Product')
plt.show()
