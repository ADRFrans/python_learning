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