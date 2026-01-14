# this is a set, not a list a set is unordered and unindexed
#use [] for a list 
random_number = [1,2,3,4,5,6,7,8,9,10]

even = []
total = 0

for number in random_number:    
    if number % 2 == 0:
        even.append(number)
    else:
        total += number

def total_odd(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

def number_type(array):
    for num in array:
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

print(f"{even} are the even numbers and {total} is the total of odd numbers")
print (f"sum of numbers in the list {total_odd(random_number)}")
number_type(random_number)