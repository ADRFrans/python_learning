import json

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def sum_evens(numbers):
    #Scope variable to hold total
    total = 0
    #loop to check numbers in given list 
    for number in numbers:
        #check if numbers are even for each number in list 
        if is_even(number):
            #if even, add to total
            total += number
    return total

# read a local file 
def read_from_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

#dumps a dictionary into a json format 

def save_to_file(file_name, string):
    with open(file_name, 'w') as file:
        json.dump(string, file, indent=2)

# read a file and convert it back to python object
def read_from_file(file_name):
    with open(file_name, 'r') as file:
        content = json.load(file)
    return content