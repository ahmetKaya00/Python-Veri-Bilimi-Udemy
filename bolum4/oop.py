class Araba:
    def __init__(self,marka,renk):
        self.marka = marka
        self.renk = renk
    
    def calistir(self):
        print(f"{self.marka} çalıştı!")

araba1 = Araba("Toyota","Kırmızı")
araba1.calistir()