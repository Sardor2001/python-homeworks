def filter_odd_numbers(lst):
    # Using list comprehension to filter even numbers
    odds = [num for num in lst if num % 2 == 1]
    return odds


# Example usage
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter_odd_numbers(lst)
print("Odd numbers:", odd_numbers)
