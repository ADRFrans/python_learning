def read_from_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

file = read_from_file('data/numbers.txt')

def strip_and_check_digit(string):
    numbers = []
    for line in string.splitlines():
        stripped_line = line.strip()
        if stripped_line.isdigit():
            numbers.append(int(stripped_line))
    return numbers

number_list = strip_and_check_digit(file)

def count_numbers(numbers):
    count = 0
    for number in numbers:
        count += 1
    return count

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def min_number(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

def max_number(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

def average_number(numbers):
    total = sum_numbers(numbers)
    count = count_numbers(numbers)
    return total / count

print(f"Count: {count_numbers(number_list)}")
print(f"Sum: {sum_numbers(number_list)}")
print(f"Min: {min_number(number_list)}")
print(f"Max: {max_number(number_list)}")
print(f"Average: {average_number(number_list)}")