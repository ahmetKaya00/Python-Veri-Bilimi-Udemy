for i in range(5):
    print(i)

fruits = ["elma","armut","muz"]
for fruit in fruits:
    print(fruit)

for letter in "Python":
    print(letter)

count = 0
while count < 5:
    print("Sayı:", count)
    count += 1

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(3):
    for j in range(2):
        print(i,j)

password = "1234"
attempt = ""

while attempt != password:
    attempt = input("Şifreyi Girin:")
    if attempt != password:
        print("Yanlış şifre, tekrar deneyin")
print("Giriş başarılı")