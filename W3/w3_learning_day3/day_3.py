print(10 + 5)

sum1 = 100 + 50 
sum2 = sum1 + 250 
sum3 = sum2 + sum2

#Python Arithmetic 
x = 15
y = 4 


print(x + y)
print(x - y)
print(x * y)
#returns a float 
print(x / y)
#modulus 
print(x % y)

#Exponentiation 
print(x ** y)

#Floor division returns an int 
print(x // y)

#Walrus operator 
numbers = [1,2,3,45,6]

if (count := len(numbers)) > 3: 
    print(f"List has {count} elements")

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print(1 < x < 10)
print(1 < x and x < 10)

print(x > 0 and x < 10)

print(x < 5 or x > 10)

print(not(x > 3 and x < 10))

# Example 
# the is operator returns True if both variables point to the same object 

x = ["apple", "banana"]
y = ["apple", "banana"]

z = x 

print(x is z)
print(x is y)
print(x == y)

#Example 
# the is not operator retuns true if both variables do not point to the same object: 

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#Example 

x = [1, 2, 3]
y = [1, 2, 3]

#is checks Identity and == checks value
print(x == y)
print(x is y)

#Example 
fruits = ["apple", "banana", "cherry"]

print(f"banana is in furits{"banana" in fruits}") 

print("pineapple" not in fruits     )

text = "hello world"

print("H" in text)
print("hello" in text)
print("z" not in text)

#example 
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated firs
print((6 + 3) - (6 + 3))

#Example 
#Multiplication * has higher precedence that addition +, and therefore multiplications are evaluated before additions: 

print(100 + 5 * 3)

#Example 
#Addition + and subtracton - has the same precedence, and therefore we evaluate the expression from left to right: 
print(5 + 4 - 7 + 3)
