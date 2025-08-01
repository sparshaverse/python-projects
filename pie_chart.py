import  matplotlib.pyplot as plt

n = int(input("How many categories? " ))
labels = []
values = []

for i in range(n):
    label = input(f"Enter categories {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    labels.append(label)
    values.append(value)


plt.pie(values, labels = labels, autopct='%1.1f%%', startangle=90)
plt.title("User Input Pie Chart")
plt.axis('equal')
plt.show()
