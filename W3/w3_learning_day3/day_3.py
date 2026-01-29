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

#python lists 
#Example 
thislist = ["","",""]
print(thislist)

#Example 
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Exampole 
print (len(thislist))

#Example 
list1 = ["","",""]
list2 = [1, 5, 7, 7, 8]
list3 = [True,False,True]

#Example - a list with strings, int and bool
list1 = ["abc", 34, True, 40 , "male"]

#Example - what is the data type of a lit 

print(type(list1))

#Example - Using the list() constructor to make a list 
thislist = list(("apple","banana", "cherry"))

print(thislist)

#Lesson Access List Items 

#Example - Print the second item of the list: 
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#example 
print(thislist[-1])

#Example 
thislist = ["apple", "banana", "cherry","apple", "banana", "cherry"]
print(thislist[2:5])

#Example 
thislist = ["apple", "banana", "cherry","apple", "banana", "cherry"]

print(thislist[:4])


#Example - by leaving ou the end value, the range will go on to the end of the list 
print(thislist[2:])

#Example - This example returns the items from "orange" (-4) to, but not including mango
print(thislist[-4:-1])

#Example 
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("yes, apple is in the fruits list")

# Example - change the second item: 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Example - change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Example change the second value by replacing it with two new values: 

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Example - Insert "watermelon" as the third item: 
thislist = ["apple", "banana", "cherry "]
thislist.insert(2, "watermelon")
print(thislist)

#Example - Using the append() method an item: 
thislist = ["","",""]
thislist.append("orange")
print(thislist)

#Example - Insert an item as the second position: 
t = ["","",""]
t.insert(1,"")
print(t)

#Example - Add the elements of tropical to thelist: 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Example - add elements of a tuple to a list: 

thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)