age = int(input("Yaşınızı Girin: "))
print("10 yıl sonra", age + 10, "yaşında olacaksın!")

current_year = 2025
birth_year = int(input("Doğum yılınızı girin: "))
age = current_year - birth_year
print("Yaşınız:", age)

try:
    birth_year = int(input("Doğum yılınızı girin: "))
    age = current_year - birth_year
    print("Yaşınız:", age)
except ValueError:
    print("Lütfen geçerli bir sayı girin. Örneğin 1965 gibi.")