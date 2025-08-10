my_list = []

numbers = [10,20,30,40,50]

mixed = [10,"Ahmet",True,99.5]

print(my_list)
print(numbers)
print(mixed)

fruits = ["elma","muz","armut"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::2])

fruits.append("çilek")
fruits.insert(1,"karpuz")
print(fruits)
del fruits[0]
print(fruits)

list1 = [1,2]
list2 = [3,4]
print(list1 + list2)

nums = [5,1,8,3]

nums.sort()
print(nums)
nums.reverse()
print(nums)
