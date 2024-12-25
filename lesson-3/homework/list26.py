def find_middle(lst):
    length = len(lst)

    # If the list is empty, return None
    if length == 0:
        return None

    # If the list has an odd number of elements, return the middle element
    if length % 2 != 0:
        middle_index = length // 2
        return lst[middle_index]

    # If the list has an even number of elements, return the two middle elements
    else:
        middle_index1 = (length // 2) - 1
        middle_index2 = length // 2
        return lst[middle_index1], lst[middle_index2]


# Example usage
lst_odd = [1, 2, 3, 4, 5]
lst_even = [1, 2, 3, 4, 5, 6]

print("Middle element (odd list):", find_middle(lst_odd)) 
print("Middle elements (even list):", find_middle(lst_even))
