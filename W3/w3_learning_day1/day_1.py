import sys 
print(sys.version)

if 5 > 2: 
    print("Five is greater than two!")

print("Python is fun!")

print("Hello, World!")
print("Have a good day.")
print("Learning python is fun!")

print("Hello"); print("How ar you?"); print("Bye bye")

print("Hello World!")
print("I am learning python.")
print("It is awesome!")

print("This will work!")
print("Hello world!", end=" ")
print("I will print on the same line.")

print(3)
print(358)
print(50000)

print(3 + 3)
print(2 * 5)

print("I am", 35, "years old.")

x = 5
y = "John"
print(x)
print(y)

x = 4 # x is of type int 
x = "sally" # x is now of type str 
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as 
x = 'John'

#Example 
a = 4 
A = "Sally"
#A will not overwrite a
print(a)

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Lesson - Python Variables  Assign Multiple Values 
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Lesson - Python Output variables

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5 
y = 10
print(x + y)

x = 5 
y = "John"
print(x, y)

x = 5
y = "John"
#print(x + y)

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

#if you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global x 
    x = "fantastic"
myfunc()

print("\nPython is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
    global x 
    x = "fantastic"

myfunc()

print("Python is " + x)

textType = str("Hello World")

print(textType)

numType1 = int(20)
numType2 = float(20.5)
numType3 = complex(1j)

print(numType1)
print(numType2)
print(numType3)

sequenceType1 = list(("apple", "banana", "cherry"))
sequenceType2 = tuple(("apple", "banana", "cherry"))
sequenceType3 = range(6)

print(sequenceType1)
print(sequenceType2)
print(sequenceType3)

mappingType = dict(name="John", age=36)

print(mappingType)

setType1 = set(("apple", "banana", "cherry"))
setType2 = frozenset(("apple", "banana", "cherry"))

print(setType1)
print(setType2)

boolean = bool(5 > 2)

print(boolean)

BinaryType1 = bytes(5)
BinaryType2 = bytearray(5)
BinaryType3 = memoryview(bytes(5))

print(BinaryType1)
print(BinaryType2)
print(BinaryType3)

#Print the data type of the variable x:
x = 5
print(type(x))

x = 1 # int 
y = 2.8 # float
z = 1j # complex

print(type(x))
print(type(y))
print(type(z))

#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1 
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#You can convert from one type to another with the int(), float(), and complex() methods:

x = 1   # int
y = 2.8 # float
z = 1j  # complex

a = float(x) # convert from int to float
b = int(y)   # convert from float to int
c = complex(x) # convert from int to complex

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random 

print(random.randrange(1, 10))

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(x)
print(y)
print(z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(x)
print(y)
print(z)
print(w)

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print(x)
print(y)
print(type(z))

print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hellow"
print(a[1])

for x in "banana":
    print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")