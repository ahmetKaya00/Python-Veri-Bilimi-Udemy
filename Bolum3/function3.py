def selamla(isim="Misafir"):
    print(f"Merhaba {isim}")

selamla()

def karsilama(isim="Misafir",sehir="İstanbul"):
    print(f"Merhaba {isim}, {sehir} şehrina hoş geldin!")

karsilama()
karsilama("Ahmet")
karsilama(sehir="İzmir")

def listeye_ekle(eleman,liste=[]):
    liste.append(eleman)
    return liste

print(listeye_ekle(1))
print(listeye_ekle(2))

def listeye_ekle(eleman,liste=None):
    if liste is None:
        liste = []
    liste.append(eleman)
    return liste

print(listeye_ekle(1))
print(listeye_ekle(2))