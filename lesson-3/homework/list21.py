def second_smallest(lst):
    # Remove duplicates and sort the list in ascending order
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()

    # Check if there are at least two unique elements
    if len(unique_lst) < 2:
        return None  # Not enough elements for a second smallest
    return unique_lst[1]  # Return the second smallest


# Example usage
lst = ['apple', 'banana', 'cherry', 'date', 'banana', 'apple', 'cherry']

print("Second smallest:", second_smallest(lst))
