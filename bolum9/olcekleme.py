import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler, RobustScaler

df = pd.DataFrame({
    "yas":[22,35,47,51,38,29,42],
    "gelir": [2500,4200,5800,9100,7600,3300,6400],
    "harcama":[400,800,900,1200,1100,500,950]
})

print(df.describe())

scaler = MinMaxScaler(feature_range=(0,1))
scaled = scaler.fit_transform(df)
df_minmax = pd.DataFrame(scaled,columns=df.columns)

print(df_minmax)

Sscaler = StandardScaler()
Sscaled = Sscaler.fit_transform(df)
df_std = pd.DataFrame(Sscaled,columns=df.columns)
print(df_std)

Rscaler = RobustScaler()
Rscaled = Rscaler.fit_transform(df)
df_robust = pd.DataFrame(Rscaled,columns=df.columns)
print(df_robust)
