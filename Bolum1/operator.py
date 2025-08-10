a = 10
b = 3

print("Toplama:" , a + b)
print("Çıkarma:" , a - b)
print("Çarpma:" , a * b)
print("Bölme:" , a / b) #Burası float değer döner
print("Tam Bölme:" , a // b) 
print("Kalan:" , a % b) 
print("Üs Alma:" , a ** b) 

x = 5
y = 10

print(x == y)
print(x != y)
print(x < y)
print(x > y)
print(x >= y)
print(x <= y)

print(x > 0 and b > 0)
print(x > 0 or b < 0)
print(not(x>0))

sonuc = 3 + 2 * 5
print(sonuc)

sonuc = (3 + 2) * 5
print(sonuc)

not1 = float(input("1. sınav notunuz:"))
not2 = float(input("2. sınav notunuz:"))

ortalama = (not1 + not2) / 2
print("Ortalama:", ortalama)