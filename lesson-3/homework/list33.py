def find_all_indices(lst, element):
    # Find all indices of the given element in the list
    return [i for i, x in enumerate(lst) if x == element]


# Example usage
lst = [1, 2, 3, 4, 2, 5, 2]
element = 2

indices = find_all_indices(lst, element)
print("Indices of element:", indices)
