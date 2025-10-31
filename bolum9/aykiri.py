import pandas as pd
import numpy as np

df = pd.DataFrame({
    "yas": [22,25,26,27,28,29,30,120],
    "gelir": [3000,3200,3100,3050,3300,3500,3400,100000],
    "harcama": [400,420,410,405,430,450,440,20000]
})

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outlier_mask = (df < lower) | (df>upper)

print(Q1)
print(Q3)
print(IQR)
print(lower)
print(upper)
print(outlier_mask)

df_clipped = df.clip(lower=lower, upper=upper, axis=1)

print(df_clipped)

df_clean = df[~outlier_mask.any(axis=1)]
print(df_clean)
