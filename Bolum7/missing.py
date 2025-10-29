import pandas as pd
import numpy as np

veri = {
    "isim": ["Ahmet","Zeynep","Mert","Ayşe","Ali"],
    "yas":[25,np.nan,22,np.nan,30],
    "maas":[15000,18500,np.nan,17000,95000]
}

df = pd.DataFrame(veri)
print(df)

print(df.isnull().sum())

"""df.dropna(inplace=True)"""

df["yas"].fillna(df["yas"].mean(),inplace=True)

df["maas"].fillna(df["maas"].median(),inplace=True)
print(df)


Q1 = df["maas"].quantile(0.25)
Q3 = df["maas"].quantile(0.75)

IQR = Q3 - Q1

alt_sinir = Q1 - 1.5 * IQR
ust_sinir = Q3 + 1.5 * IQR

aykirilar = df[(df["maas"]<alt_sinir) | (df["maas"]>ust_sinir)]

print(aykirilar)

df["maas"] = np.where(df["maas"]>ust_sinir,ust_sinir,np.where(df["maas"]<alt_sinir,alt_sinir,df["maas"]))
print(df)
