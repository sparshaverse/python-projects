import pandas as pd 
import matplotlib.pyplot as plt

data = {'Subjects': ["Maths", "Science", "Social", "English", "History",],
        'Marks' : [85, 90, 55, 79, 66]}
df = pd.DataFrame(data)
df.plot(x ='Subjects', y ='Marks', kind ='line')
plt.show()