def toplama(a,b):
    return a + b

sonuc = toplama(5,3)
print("Toplam:",sonuc)

def islemler(a,b):
    return a+b, a-b,a*b

toplam, fark, carpim = islemler(10,5)
print("Toplam",toplam)
print("Fark",fark)
print("Çarp",carpim)

def kargo_ucreti(hacim,mesafe):
    ucret = (hacim * 0.5) + (mesafe * 0.2)
    return round(ucret,2)

siparis1 = kargo_ucreti(10,300)
siparis2 = kargo_ucreti(5,120)

print("Sipariş 1:",siparis1, "TL")
print("Sipariş 2:",siparis2, "TL")
