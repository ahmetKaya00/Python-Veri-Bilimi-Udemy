with open("gunluk.txt","a") as file:
    file.write("Bugün python öğrendim.\n")

try:
    with open("gunluk.txt","a") as file:
        file.write("Bugün append modu öğrendim.\n")
except PermissionError:
    print("Hata: Bu dosyaya yazma izniniz yok")

while True:
    not_icerik = input("Günlüğe eklemek istediğiniz metin(çıkmak için q):")
    if not_icerik.lower() == "q":
        break
    with open("gunluk.txt","a") as file:
        file.write(not_icerik + "\n")