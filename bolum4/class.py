class Araba:
    def __init__(self,marka,renk):
        self.marka = marka
        self.renk = renk
    
    def calistir(self):
        print(f"{self.marka} çalıştı!")

araba1 = Araba("Toyota","Kırmızı")
araba1.calistir()

araba2 = Araba("Audi","Beyaz")
araba2.calistir()


class Calisan:
    firma = "ABC Teknoloji"

    def __init__(self,isim,pozisyon):
        self.isim = isim
        self.pozisyon =pozisyon

class Musteri:
    firma_adi = "XYZ Mağaza"

    def __init__(self,isim,sehir):
        self.isim = isim
        self.sehir = sehir
    
    def siparis_ver(self, urun):
        print(f"{self.isim} adlı müşteri {urun} sipariş etti!")

m1 = Musteri("Ahmet","İstanbul")
m2 = Musteri("Mehmet","Ankara")

m1.siparis_ver("Laptop")
m2.siparis_ver("Telefon")

