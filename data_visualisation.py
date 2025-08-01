import matplotlib.pyplot as plt

x = ['Maths', 'Science ','English', 'Social']
y = [88, 90, 75, 50]

plt.bar(x,y, color='skyblue')
plt.title("Student Marks")   
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()