try:
    sayi = int(input("Bir sayi girin"))
    print(10 / sayi)
except:
    print("Bir hata oluştu")

try:
    sayi = int(input("Bir sayi girin"))
    print(10 / sayi)
except ZeroDivisionError:
    print("Sıfıra bölme yapılamaz!")
except ValueError:
    print("Lütfen sayısal bir değer girin.")

try:
    sayi = int(input("Bir sayi girin"))
    print(10 / sayi)
except (ZeroDivisionError,ValueError) as e:
    print("Hata:",e)

try:
    sayi = int(input("Bir sayı girin: "))
except ValueError:
    print("Sayısal değer girin.")
else:
    print("Girdiğiniz sayi: ", sayi)

try:
    dosya = open("veri.txt","r")
    veri = dosya.read()
except FileNotFoundError:
    print("Dosya bulunamadı!")
finally:
    print("Dosya işlemi tamamlandı!")
