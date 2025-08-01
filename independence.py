import pandas as pd
from scipy.stats import chi2_contingency

data = {'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female'],
        'Purchased': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No']}
df = pd.DataFrame(data)

contingency = pd.crosstab(df['Gender'], df['Purchased'])
chi2, p, _, _ = chi2_contingency(contingency)

print("P-Value:", p)
