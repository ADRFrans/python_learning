from src.phase_1.utils import sum_evens, is_even

random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

evens = is_even(random_numbers)

even_sum = sum_evens(random_numbers)

print(f"The sum of even numbers in the list is: {even_sum}")