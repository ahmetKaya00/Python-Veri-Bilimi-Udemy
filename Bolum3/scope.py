def function():
    x = 10
    print("Fonksiyon içi:", x)

function()
#print("Fonksiyon dışı:" , x)
x = 10
def function():
    print("Fonksiyon içi:", x)

function()
print("Fonksiyon dışı:" , x)

def function():
    global x
    x = 15

function()
print(x)

def function():
    x = 100
    print("Fİ:",x)

function()
print(x)

def dis_function():
    b = 10
    def ic_function():
        print(b) #nonlocal
    ic_function()

dis_function()