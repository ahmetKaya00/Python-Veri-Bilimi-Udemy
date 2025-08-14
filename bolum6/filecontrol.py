import os
import shutil

if os.path.exists("deneme.txt"):
    print("Dosya var.")
else:
    print("Dosya yok")

if os.path.exists("deneme.txt"):
    os.remove("deneme.txt")
else:
    print("Dosya yok")

#os.rename("gunluk.txt","gunluk_not.txt")

#os.mkdir("yeni_klasör")
#os.rmdir("yeni_klasör")

#shutil.move("gunluk_not.txt", "arsiv/gunluk_not.txt")

shutil.copy("buyuk_dosya.txt","yedek/buyuk_dosya.txt")