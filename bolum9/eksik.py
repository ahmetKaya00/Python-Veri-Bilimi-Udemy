import pandas as pd
import numpy as np

df = pd.DataFrame({
    "yas": [25,np.nan,32,28,np.nan,40,19],
    "maas": [5000,6000,np.nan,5500,5200,np.nan,4800],
    "departman":["IT","IT","HR","HR","IT",np.nan,"Finance"],
    "sehir": ["İstanbul","Ankara","Ankara","İzmir",np.nan,"İstanbul","İzmir"],
})
print(df)

print(df.isna().sum())

df["yas"].fillna(30)

df["yas"].fillna(df["yas"].mean(),inplace=True)

print(df.groupby("departman")["yas"].mean())

print(df.groupby("departman")["yas"].transform("mean"))

df["yas"] = df["yas"].fillna(
    df.groupby("sehir")["yas"].transform("median")
)
print(df)

df["departman"].fillna(df["departman"].mode()[0],inplace=True)
print(df)

for col in df.columns:
    if df[col].dtype == "O":
        df[col].fillna(df[col].mode()[0],inplace=True)
    else:
        df[col].fillna(df[col].median(),inplace=True)
print(df)
