my_tuple = (10,20,30)
print(my_tuple)

mixed_tuple = (10, "Ahmet", True,99.5)
print(mixed_tuple)

single = (5,)
print(type(single))

fruits = ("elma","armut","çilek")
print(fruits[1])
print(fruits[-1])
print(fruits[1:3])

#fruits[0] = "karpuz" HATA!!

colors = ("red","blue","cyan","green","green")
print(colors.count("green"))
print(colors.index("blue"))

t = ("elma","muz","armut")
l = list(t)
l[0] = "çilek"
t = tuple(l)
print(t)