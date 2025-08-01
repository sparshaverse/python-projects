from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = load_wine()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

model = RandomForestClassifier()
model.fit(X_train, y_train)


pred = model.predict(X_test)
print(classification_report(y_test, pred))