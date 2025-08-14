with open("deneme.txt","r") as file:
    icerik = file.read()
    print(icerik)
    
with open("deneme.txt","r") as file:
    icerik = file.readline()
    print(icerik)

with open("deneme.txt","r") as file:
    icerik = file.readlines()
    print(icerik)

with open("deneme.txt","r") as file:
    for satir in file:
        print(satir.strip())

try:
    with open("olmayan_dosya.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("Hata: Dosya Bulunamadı!")

with open("buyuk_dosya.txt","r") as file:
    while True:
        veri = file.read(1024)
        if not veri:
            break
        print(veri)