def second_largest(my_list):
    # Remove duplicates and sort the list in ascending order
    unique_lst = list(set(my_list))  # Remove duplicates
    unique_lst.sort()

    # Check if there are at least two unique elements
    if len(unique_lst) < 2:
        return None  # Not enough elements for a second largest
    return unique_lst[-2]  # Return the second largest


# Example usage
lst = ['apple', 'banana', 'cherry', 'date', 'banana', 'apple', 'cherry']

print("Second largest:", second_largest(lst))
