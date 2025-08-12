class Calisan:
    def __init__(self,isim,maas):
        self.isim = isim
        self.maas = maas
    def zam_yap(self,oran):
        self.maas += self.maas * (oran / 100)
        print(f"{self.isim} adlı çalışanın yeni maaşı: {self.maas} TL")
c1 = Calisan("Ahmet",70000)
c1.zam_yap(10)

class Calisan:
    firma = "ABC Teknoloji"

    @classmethod
    def firma_degistir(cls,yeni_firma):
        cls.firma = yeni_firma
        print(f"Yeni firma adı: {cls.firma}")

Calisan.firma_degistir("XYZ Yazılım")

class HesapMakinesi:
    @staticmethod
    def kare_al(sayi):
        return sayi**2
    
print(HesapMakinesi.kare_al(5))

class Personel:
    firma ="Yobodobo"

    def __init__(self,isim):
        self.isim = isim
    
    def selam_ver(self):
        print(f"Merhaba, ben {self.isim} ve {self.firma}'da çalışıyorum")
    @classmethod
    def firma_guncelle(cls,yeni_firma):
        cls.firma = yeni_firma
    
    @staticmethod
    def tarih_formatla(yil,ay,gun):
        return f"{gun:02d}/{ay:02d}/{yil}"
    
p1 = Personel("Ahmet")
p1.selam_ver()

Personel.firma_guncelle("ABC Yazılım")
p1.selam_ver()
print(Personel.tarih_formatla(2025,8,12))