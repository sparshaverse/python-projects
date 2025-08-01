import pandas as pd
import matplotlib.pyplot as plt

data = {'Subject': ['Math', 'Science', 'History'],
        'Marks': [85, 90, 80]}

df = pd.DataFrame(data)
df.plot(x='Subject', y='Marks', kind='bar')

plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Marks by Subject')

plt.show()
