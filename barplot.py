import matplotlib.pyplot as plt
names = ["anirudh","Alice","Charlie","David"]
marks = [80, 95, 66, 87]

plt.barh(names, marks, color = 'green')
plt.title("Marks of students")
plt.xlabel('Marks')
plt.ylabel("Students")
plt.show()