class BankaHesabi:
    def __init__(self,sahip,bakiye):
        self.sahip = sahip
        self.__bakiye = bakiye
    def bakiye_goster(self):
        return self.__bakiye, self.sahip
    def para_yatir(self,miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.__bakiye} TL")
        else:
            print("Yatırılacak miktar pozitif olmalı.")

hesap = BankaHesabi("Ahmet",1000)
print(hesap.bakiye_goster())
hesap.__bakiye = 1500
hesap.sahip = "Mehmet"
print(hesap.bakiye_goster())

"""
public = "Genel"
_protected = "Korumalı"
__private = "Özel"
"""

class Calisan:
    def __init__(self,isim,maas):
        self.isim = isim
        self.__maas = maas
    def get_maas(self):
        return self.__maas
    def set_maas(self,yeni_maas):
        if yeni_maas > 0:
            self.__maas = yeni_maas
        else:
            print("Maaş sıfırdan büyük olmalı.")

c1 = Calisan("Zeynep",50000)
print(c1.get_maas())
c1.__maas = 60000
print(c1.get_maas())
c1.set_maas(60000)
print(c1.get_maas())


class Sepet:
    def __init__(self):
        self.__urunler = []
    def urun_ekle(self,urun):
        self.__urunler.append(urun)
    def urunleri_goster(self):
        return self.__urunler.copy()