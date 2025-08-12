musteriler = {}

def musteri_ekle(isim):
    if isim not in musteriler:
        musteriler[isim] = []
        print(f"{isim} sisteme eklendi.")
    else:
        print(f"{isim} zaten kayıtlı.")

def siparis_ekle(isim, *urunler):
    if isim in musteriler:
        for urun in urunler:
            musteriler[isim].append(urun)
        print(f"{isim} müşterisine {len(urunler)} ürün eklendi")
    else:
        print(f"{isim} adlı kullanıcı bulunamadı.")

def siparis_listeleme(isim):
    if isim in musteriler:
        if musteriler[isim]:
            print(f"{isim} müşterisinin siparişleri:")
            for urun, fiyat in musteriler[isim]:
                print(f"-{urun}:{fiyat} TL")
        else:
            print(f"{isim} müşterisinin siparişi yok.")
    else:
        print(f"{isim} adlı kullanıcı bulunamadı.")

def toplam_tutar(isim, indirim=0):
    if isim in musteriler:
        toplam = sum([fiyat for _, fiyat in musteriler[isim]])
        toplam -= toplam * (indirim / 100)
        return round(toplam,2)
    else:
        return None

def musterileri_sirala():
    sirali = sorted(musteriler.items(), key=lambda x: toplam_tutar(x[0]) or 0, reverse=True)
    print("Müşteriler (Toplam Harcamaya Göre):")
    for isim, _ in sirali:
        print(f"- {isim}: {toplam_tutar(isim)} TL")

musteri_ekle("Ahmet")
musteri_ekle("Mehmet")

siparis_ekle("Ahmet",("Telefon",15000),("Mouse",500))
siparis_ekle("Zeynep",("Telefon",10000),("Mouse",700))

siparis_listeleme("Ahmet")

musterileri_sirala()
    
