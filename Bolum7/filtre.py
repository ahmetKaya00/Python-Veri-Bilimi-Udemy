import pandas as pd

data = {
    "isim":["Ahmet","Zeynep","Mert","Ayşe","Ali","Elif","Can","Deniz"],
    "departman":["Satış","Satış","IT","IT","Muhasebe","Satış","Muhasebe","IT"],
    "maas":[15000,18500,20000,17000,16000,15500,14000,21000],
    "sehir":["İstanbul","Ankara","İzmir","İstanbul","Ankara","İstanbul","İzmir","Bursa"]
    }
df = pd.DataFrame(data)
print(df)

print(df[df["maas"]>17000])

print(df[(df["departman"] == "Satış") | (df["maas"]>20000)])

print(df.sort_values(by="maas", ascending=False))

print(df.sort_values(by=["departman","maas"],ascending=[True, False]))

print(df.groupby("departman")["maas"].mean())

ortalamalar = df.groupby("departman",as_index=False)["maas"].mean()
print(ortalamalar)

print(df.groupby("departman")["maas"].agg(["mean","max","min","count"]))

print(df.groupby(["departman","sehir"])["maas"].mean())

print(df.sort_values(by="maas",ascending=False).head(3))