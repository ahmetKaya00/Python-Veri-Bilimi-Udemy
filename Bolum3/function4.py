def toplama(*sayilar):
    toplam = 0
    for s in sayilar:
        toplam += s
    return toplam

print(toplama(3,5))
print(toplama(3,5,456,98))

def indirim_orani(indirim, *fiyatlar):
    for fiyat in fiyatlar:
        print(f"{fiyat} TL -> {fiyat - (fiyat * indirim / 100)} TL")
    
indirim_orani(10,100,200,300)

def kullanici_bilgileri(**bilgiler):
    for anahtar, deger in bilgiler.items():
        print(f"{anahtar}: {deger}")

kullanici_bilgileri(isim="Ahmet",yas=20,sehir="İstanbul")

def siparis(detay,*urunler,**adres):
    print("Sipariş Detayı:",detay)
    print("Ürünler:",urunler)
    print("Teslimat Adresi:",adres)

siparis("Hızlı teslimat","Laptop","Mouse",sehir="İstanbul",mahalle="kadıköy")