from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[4]])
y = np.array([3, 6, 9, 12])

model = LinearRegression()
model.fit(X,y)

print("Prediction for x=5:", model.predict([[5]]))