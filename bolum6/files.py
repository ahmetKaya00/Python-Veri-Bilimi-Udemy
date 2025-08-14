file = open("deneme.txt","w")
file.write("Merhaba dosya")
file.close()

"""
r -> Read
w -> Yazma
a -> Ekleme
x -> Create
b -> Binary
t -> text
"""

with open("deneme.txt","w") as file:
    file.write("Bu yönten güvenlidir!")