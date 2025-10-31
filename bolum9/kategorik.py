import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "sehir":["İstanbul","Ankara","İzmir","Ankara","İstanbul","Bursa","Antalya","İzmir"],
    "urun_kategorisi": ["Elektronik","Moda","Elektronik","Ev","Moda","Moda","Ev","Elektronik"],
    "egitim": ["Lise","Üniversite","Lise","Ortaokul","Üniversite","Lise","İlkokul","Üniversite"],
    "cinsiyet": ["Kadın","Erkek","Erkek","Kadın","Kadın","Erkek","Kadın","Erkek"],
    "yas":[23,31,27,45,36,29,41,33],
    "satinalma": [1,0,1,0,1,0,1,1]
})

x = df.drop(columns=["satinalma"])
y = df["satinalma"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42,stratify=y)

x_train_one = pd.get_dummies(
    x_train,
    columns=["sehir","urun_kategorisi","cinsiyet"],
    drop_first=False,
    dtype=np.uint8
)
print(x_train_one.head())