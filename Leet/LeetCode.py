#Instances where we subtract the roman numeral value 
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.


# The Problem: Given a roman numeral, convert it to an integer.
# we need to pass in a string and then break up that string and evaluate each int
def romanToInt(val):
    #Break the string into individual characters
    eval = list(val)
    # we need a way to identify the numbers we have 
    roman_nums= {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50, 
        "C" : 100, 
        "D" : 500,
        "M" : 1000,
    }
    #now we need to iterate throug the new list and assign a number 
    # I need to iterate throug the list we recieve and match each character from the list  with it' corisponding value in the dict
    for x in eval: 
        num = 0 
        current_key = {}
        t = roman_nums["I"]
    print(t)


rnum = "IV"

romanToInt(rnum)


