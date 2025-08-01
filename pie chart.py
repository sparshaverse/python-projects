import matplotlib.pyplot as plt

labels = ["Apples", "Bananas", "Mangoes", "Grapes"]
values = [30, 20, 40, 10]


plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Fruit Distribution")
plt.axis('Equal')
plt.show()
