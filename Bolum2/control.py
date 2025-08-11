"""
if(age>=18){
    print("tamam");
}
"""

age = 17

if age>=18:
    print("reşitsiniz!")
else:
    print("reşit değilsiniz!")

score = 75

if score >= 90:
    print("AA")
elif score>=70:
    print("BB")
elif score>=50:
    print("CC")
else:
    print("FF")

age = 15
membership = True

if age >= 18:
    if membership:
        print("Giriş başarılı!")
    else:
        print("Lütfen üye olun!")
else:
    print("Yaş sınırı nedeniyle giriş yapılamadı!")

if age>=18 and membership:
    print("Üye girişi başarılı")

status = "Reşit" if age>=18 else "Reşit değil"
print(status)

notu = float(input("Notunuzu girin: "))

if notu >= 90:
    print("AA")
elif notu>=80:
    print("BA")
elif notu>=70:
    print("BB")
elif notu>=50:
    print("CC")
else:
    print("FF - Kaldınız!")