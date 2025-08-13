yas = int(input("Yaşınızı girin: "))
if yas < 18:
    raise ValueError("18 yaşından küçükler bu siteye giremez!")
else:
    print("Kayıt Başarılı!")
try:
    maas = int(input("Maaşınızı girin: "))
    if maas < 0:
        raise ValueError("Maaş negatif olamaz!")
except ValueError as e:
    print("Hata:",e)
else:
    print("Maaşınız:", maas)

try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Veri dönüştürme başarısız!") from e