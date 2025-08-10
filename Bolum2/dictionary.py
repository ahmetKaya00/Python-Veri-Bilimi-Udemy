my_dict = {}

person = {
    "name": "Ahmet",
    "age": 20,
    "city": "Mersin"
}
print(person)

print(person["name"])
print(person.get("names","Bulunamadı"))

person["email"] = "ahmet@kaya.com"
person["age"] = 26
print(person)

person.pop("email")
del person["city"]
print(person)
person.clear()

person = {
    "name": "Ahmet",
    "age": 20,
    "city": "Mersin"
}
print(person.keys())
print(person.values())
print(person.items())

students = {
    "1001": {"name":"Ahmet","age":20},
    "1002": {"name": "Ayşe","age":30}
}
print(students["1001"]["name"])