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