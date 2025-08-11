PIN = "1234"
giris = ""

while giris != PIN:
    giris = input("Şifrenizi girin:")
    if giris != PIN:
        print("Yanlış şifre,tekrar deneyin")
print("Giriş başarılı")

bakiye = 1000

while True:
    print("\n --ATM Menüsü---")
    print("1. Bakiye Sorgulama")
    print("2. Para Yatırma")
    print("3. Para Çekme")
    print("4. Çıkış")

    secim = input("Seçiminiz:")

    if secim == "1":
        print(f"Mavcut Bakiyeniz: {bakiye} TL")
    elif secim == "2":
        miktar = float(input("Yatırmak istediğiniz miktar:"))
        bakiye += miktar
        print(f"Yeni Bakiyeniz: {bakiye} TL")
    elif secim == "3":
        miktar = float(input("Çekmek istediğiniz miktar:"))
        if miktar <= bakiye:
            bakiye -= miktar
            print(f"Kalan Bakiyeniz: {bakiye} TL")
        else:
            print("Bakiye Yetersiz!")
    elif secim == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz Seçim! Lütfen 1-4 arası bir sayı girin!")


