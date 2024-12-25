def filter_even_numbers(lst):
    # Using list comprehension to filter even numbers
    evens = [num for num in lst if num % 2 == 0]
    return evens


# Example usage
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(lst)
print("Even numbers:", even_numbers)
