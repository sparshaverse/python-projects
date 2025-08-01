import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Aprl", "May", "June", "July"]
sales = [2500, 2700, 3000, 5000, 5400, 2900, 5999]

plt.plot(months, sales, marker='o')
plt.title("Monthly Sales")
plt.grid(True)
plt.show()