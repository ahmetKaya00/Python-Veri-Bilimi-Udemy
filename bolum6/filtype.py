import csv
import json
"""
with open("veriler.txt","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Ad","Yaş","Şehir"])
    writer.writerow(["Ahmet",38,"İstanbul"])
    writer.writerow(["Mehmet",20,"Adana"])

with open("veriler.txt","r") as file:
    reader = csv.reader(file)
    for satir in reader:
        print(satir)

veri = {
    "ad": "Ahmet",
    "yas": 25,
    "sehir": "Van"
}

with open("veri.json","w", encoding="utf-8") as file:
    json.dump(veri,file,ensure_ascii=False,indent=4)

with open("veri.json","r", encoding="utf-8") as file:
    veri = json.load(file)
    print(veri["ad"])


"""
with open("veri.json","r", encoding="utf-8") as file:
    data = json.load(file)

with open("veri.csv","w", newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(data[0].keys())
    for row in data:
        writer.writerow(row.values())