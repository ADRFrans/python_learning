# Lesson - Python - Modify Strings

a = "Hello, world!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))

# Lesson - Python - String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#Lesson - Python - String Formatting
age = 25
txt = f"My name is John, and I am {age}"
print(txt)

price = 59 
txt = f"The price is {price} dollars"
print(txt)

price = 59 
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#Lesson - Python - Python Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200 
b = 33 

if b > a: 
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

def myFunction() :
    return False

if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200 
print(isinstance(x, int))