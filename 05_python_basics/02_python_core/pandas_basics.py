"""Pandas basics for tabular radiology data."""
import pandas as pd
import numpy as np

np.random.seed(42)
N = 8
df = pd.DataFrame({
    "patient_id": range(1001, 1001+N),
    "age": np.random.normal(62, 10, N).round(1),
    "sex": np.random.choice(["F","M"], N),
    "sarcopenia": np.random.choice([0,1], N, p=[0.65,0.35]),
    "LOS": np.random.gamma(3, 1.2, N).round(1)
})

print(df)
print("\nGroupby (sarcopenia) LOS mean:")
print(df.groupby("sarcopenia")["LOS"].mean())
