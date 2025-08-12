class Calisan:
    def __init__(self,isim,maas):
        self.isim = isim
        self.maas = maas
    def bilgileri_goster(self):
        print(f"İsim: {self.isim}, Maaş: {self.maas}")

class Yazilimci(Calisan):
    def __init__(self, isim, maas,diller):
        super().__init__(isim, maas)
        self.diller = diller
    
    def dilleri_goster(self):
        print(f"{self.isim} şu dilleri biliyor: {', '.join(self.diller)}")

class Yonetici(Calisan):
    def bilgileri_goster(self):
        print(f"[YONETICI] {self.isim} - Maaş: {self.maas} TL")

y1 = Yazilimci("Ahmet",50000,["Python","JavaScript"])
y1.bilgileri_goster()
y1.dilleri_goster()
yn1 = Yonetici("Veli",500000)
yn1.bilgileri_goster()

class Insan:
    def selam_ver(self):
        print("Merhaba")
class Programci:
    def kod_yaz(self):
        print("Kod yaziyor...")

class Yazilimci(Insan,Programci):
    pass

y = Yazilimci()
y.selam_ver()
y.kod_yaz()