import pandas as pd

veri = {
    "isim": ["Ahmet","Zeynep","Mert","Ayşe"],
    "yas": [25,29,22,31],
    "sehir": ["İstanbul","Ankara","İzmir","Bursa"]
}

df = pd.DataFrame(veri)
print(df)

df.to_csv("veriler.csv",index=False, sep=";",encoding="utf-8-sig")

okunan = pd.read_csv("veriler.csv",sep=";",encoding="utf-8-sig")

print(okunan)

df.to_excel("veriler.xlsx",index=False,sheet_name="Kisiler")

okunan_excel = pd.read_excel("veriler.xlsx")
print(okunan_excel)