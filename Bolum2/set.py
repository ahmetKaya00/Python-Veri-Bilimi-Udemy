my_set = set()

fruit = {"elma","muz","armut"}
nums = {1,2,2,3,4,4}
print(nums)
fruit.add("karpuz")
fruit.update(["çilek","kavun"])
print(fruit)

fruit.remove("muz")
fruit.discard("muzlar")
print(fruit)
fruit.clear()

A = {1,2,3}
B = {3,4,5}

print(A|B)
print(A&B)
print(A - B)
print(A^B)

names = ["Ali","Ayşe","Ali","Mehmet","Ayşe"]
unique_names = set(names)
print(unique_names)
print(names)