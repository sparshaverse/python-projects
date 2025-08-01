import matplotlib.pyplot as plt

categories = ['Math', 'Science', 'English', 'History', 'Geography']  
scores = [90, 85, 78, 88, 92]  

plt.bar(categories, scores, color='skyblue')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.title('Student Performance')
plt.show()
