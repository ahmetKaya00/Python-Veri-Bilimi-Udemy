import pandas as pd

veri = {
    "isim":["Ahmet","Mesude","Mert","Ayşe"],
    "yas":[25,29,22,31],
    "sehir":["İstanbul","Ankara","İzmir","Mersin"]
}

df = pd.DataFrame(veri)
print(df)

yaslar = pd.Series([25,29,22,31], name="yas")
print(yaslar)

print(df["yas"])