import pandas as pd

df = pd.DataFrame({
    'height':[100, 150, 170, 190, 200, 500],
    'Weight':[80, 90, 50, 66, 59, 88],
    'Age':[30, 55, 42, 69, 85, 75],
})

print("Correlation Matrix:")
print(df.corr())