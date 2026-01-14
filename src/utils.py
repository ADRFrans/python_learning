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
