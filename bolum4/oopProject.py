from datetime import date
class Personel:
    firma_adi = "Yobodobo"

    def __init__(self,ad,tc,maas,departman,ise_giris=None):
        self.ad = ad
        self.tc = tc
        self.__maas = maas
        self.departman = departman
        self.ise_giris = ise_giris or date.today()
    
    @property
    def maas(self):
        return self.__maas
    @maas.setter
    def maas(self, yeni_maas):
        if yeni_maas <= 0:
            raise ValueError("Maaş sıfırdan büyük olmalı!")
        self.__maas = yeni_maas
    
    def bilgi(self):
        return f"{self.ad} | {self.departman} | {self.maas} TL | Giriş: {self.ise_giris}"
    
    def prim_hesapla(self):
        yil = date.today().year - self.ise_giris.year
        return round(self.maas * (0.03 + yil * 0.005),2)
    
    @classmethod
    def firma_degistir(cls,yeni_ad):
        cls.firma_adi = yeni_ad

    @staticmethod
    def format_tarih(d):
        return d.strftime("%d.%m.%y")
    
class Muhendis(Personel):
    def __init__(self, ad, tc, maas, diller=None,proje_sayisi=0, ise_giris=None):
        super().__init__(ad, tc, maas, departman="Mühendislik", ise_giris = ise_giris)
        self.diller = diller or []
        self.proje_sayisi = proje_sayisi
    
    def prim_hesapla(self):
        taban = super().prim_hesapla()
        ek = (len(self.diller)*0.01 + self.proje_sayisi * 0.005)* self.maas
        return round(taban + ek,2)
    
class Yonetici(Personel):
    def __init__(self, ad, tc, maas, ekip=None,butce=0, ise_giris=None):
        super().__init__(ad, tc, maas, departman="Yönetim", ise_giris = ise_giris)
        self.ekipr = ekip or []
        self.butce = butce
    
    def prim_hesapla(self):
        taban = super().prim_hesapla()
        ek = (len(self.ekipr)*0.02)* self.maas
        butce_katsayi = 0.0001 if self.butce > 0 else 0
        return round(taban + ek + (self.maas * butce_katsayi),2)
    
class PersonelKayitSistemi:
    def __init__(self):
        self.__kayit = {}
    
    def ekle(self, personel: Personel):
        if personel.tc in self.__kayit:
            print(f"TC zaten kayitli: {personel.tc}")
            return
        self.__kayit[personel.tc] = personel
        print(f"Kayit Eklendi: {personel.ad}({personel.tc})")
    
    def sil(self,tc):
        if tc in self.__kayit:
            silinen = self.__kayit.pop(tc)
            print(f"Silindi: {silinen.ad}({tc})")
        else:
            print("kayıt bulunamadı!")
    def bul(self,tc):
        return self.__kayit.get(tc)
    def listele(self,departman=None):
        kisiler = list(self.__kayit.values())
        if departman:
            kisiler = [k for k in kisiler if k.departman == departman]
            kisiler = sorted(kisiler, key=lambda p:p.maas, reverse=True)
            for p in kisiler:
                print(p.bilgi)
    def toplam_maas(self):
        return sum(p.maas for p in self.__kayit.values())
    
    def prim_raporu(self):
        print("\n Prim Raporu")
        for p in self.__kayit.values():
            print(f"- {p.ad:15} | {p.departman:12} | Prim: {p.prim_hesapla()} TL")

sistem = PersonelKayitSistemi()

p1 = Muhendis("Ahmet","111",60000,diller=["Python","JS"],proje_sayisi=4)
p3 = Muhendis("Veli","333",60000,diller=["Python","JS"],proje_sayisi=4)
p2 = Yonetici("Zeynep","222",95000,ekip=["Ahmet","Mehmet","Elif"],butce=2_000_000)

sistem.ekle(p1)
sistem.ekle(p2)
sistem.ekle(p3)

sistem.listele()

sistem.prim_raporu()