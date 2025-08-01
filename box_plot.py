import matplotlib.pyplot as plt
data = [5, 7, 8, 9, 10, 12, 13, 13, 15, 18]

plt.boxplot(data)
plt.title("box plot")
plt.ylabel("values")
plt.show()