#Lesson - Python Sort Lists 

#Example - Sort the list Alphabetically: 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Example - sort the list numerically 
thisnumlist = [100, 50, 65, 82, 23]
thisnumlist.sort()
print(thisnumlist)
#Example - sort the list descending 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Example - sort the list descending 
thisnumlist.sort(reverse = True)
print(thisnumlist)

#Example  - sort the list based on how close the number is to 50: 
def myfunc(n):
    return abs(n - 50)

thisnumlist.sort(key = myfunc)
print(thisnumlist)

#Example - Case sensitive sorting can gve an unexpected result: 
thislist.sort()
print(thislist)

#Example - Perform a case-insensitive sort of the list: 
thislist.sort(key = str.lower)
print(thislist)

#Example - Reverse the order of the list items: 
thislist.reverse()
print(thislist)

#Lesson - Python - Copy Lists 

#Example - Make a copy of a list with the copy() method:
mylist = thislist.copy()
print(f"Copied list{mylist}")

#Example - Make a copy of a list with the list() method: 
mylist = list(thislist)
print(mylist)

#Example  - make a copy of a list with the : operator 
mylist = thislist[:]
print(mylist)

# Lesson - Python - Join Lists 

#Example - Join two lists : 
list1 = ["a","b","c","d"]
list2 = [1, 2, 3]

list3 = list1 + list2 
print(list3)

#Example - Append list2 into list1:
for x in list2: 
    list1.append(x)
print(list1)

# Example - Use the extend() method to add list2 at the end of list1: 
list1.extend(list2)
print(list1)

#Lesson - Pytohn - tuples 

#Example - Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Example - Tuples allow duplicate valeus: 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Example - print the number of items in the tuple 
print(len(thistuple))

#Examle - One item tuple, remember the comma 
tuple1 = ("apple",)
print(type(tuple1))

tuple2 = ("apple")
print(type(tuple2))

#Example - string int and bool type: 
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#Example - A tupel with strings, integers and boolean values: 

tuple1 = ("abc", 34, True, 40, "male")

#Example - What is the data type of a tuple? 
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Example - Using the tuple() method to make a tuple: 
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#Lesson Python - Dictionaries 

#Example - Create and print a dictionary: 
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#Example = Print the brand value of the dictionary 
print(thisdict["brand"])

#Example - Duplicate values will overwrite Existing values: 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Example - print the number of items in the dictionary: 
print(len(thisdict))

# Example - String, int, bool and list data types: 
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#Example - Print the data type of a dictionary: 
print(type(thisdict))

#Example - using the dict() method to make a dictionary: 
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Lesson - Pyton Access Dictionary Items 

#Example - get the value of the model key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#Example - get the value of the "model key"

x = thisdict.get("model")
print(x)

#Example - get a list of the keys: 
x = thisdict.keys()
print(x)

# Example  - Add a new item to the original dictionary, and see that the keys list gets updated as well 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x)

car["color"] = "White"

print(x)

#Example - get a list of the values: 
x = thisdict.values()

#Example = make a change in the orignal dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x)

car["year"] = 2020

print(x)

#Example - get a list of the key:value pairs 
x = thisdict.items()

#Example - make a change in the original dictonary, and see that the items lst gets updated as well: 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x)

car["year"]

print(x)

#Example - add a new item to the orignial dictionary, and see that the items list gets updated as well 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x)

car["color"] = "red"

print(x)

#Example - check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Lesson - Python - Change Dictionary Items 

#Example - Change the "year" to 2018 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

thisdict.update({"year": 2020})
#Lesson Add dictionary items 

#example 
thisdict["color"] = "red"
print(thisdict)

#Example - add a color item to the dictionary by using the update() method: 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.update({"color": "red"})

