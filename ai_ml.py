import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X,y)



print("Slope:", model.coef_)
print("Intercept:", model.intercept_)

print("Predict for 5:", model.predict([[5]]))