import csv
import os


DOSYA_ADI = "musteriler.csv"

def kayitlari_goster():
    if not os.path.exists(DOSYA_ADI):
        print("Kayıt bulunamadı!")
        return
    with open(DOSYA_ADI, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for satir in reader:
            print(satir)

def kayit_ekle():
    ad = input("Ad: ")
    telefon = input("Telefon: ")
    sehir = input("Şehir: ")

    try:
        with open(DOSYA_ADI, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([ad,telefon,sehir])
        print("Kayıt oluştu")
    except Exception as e:
        print("Kayıt oluşmadı", e)

while True:
    print("\n1- Kayıtları Göster")
    print("2- Kayıt Ekle")
    print("3- Çıkış")

    secim = input("Seçiniz: ")

    if secim == "1":
        kayitlari_goster()
    elif secim == "2":
        kayit_ekle()
    elif secim == "3":
        break
    else:
        print("Geçersiz işlem.")