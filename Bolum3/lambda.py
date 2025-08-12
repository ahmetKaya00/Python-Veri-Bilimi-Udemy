topla = lambda a,b:a+b
print(topla(5,3))

print((lambda x:x**2)(5))

urunler = [("Telefon",5000),("Laptop",12000),("Kulaklık",500)]
sirali = sorted(urunler , key=lambda urun:urun[1])
print(sirali)

sayiler = [1,2,3,4,5,6]

tekler = list(filter(lambda x:x%2 != 0,sayiler))
print("Tek Sayılar:",tekler)

kareler = list(map(lambda x:x**2,sayiler))
print("Kareler:",kareler)