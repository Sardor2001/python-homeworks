def is_sorted_ascending(lst):
    # Check if the list is sorted in ascending order
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


# Example usage
lst = [1, 2, 3, 4, 5]
print("Is the list sorted in ascending order?", is_sorted_ascending(lst))

lst_unsorted = [1, 3, 2, 4, 5]
print("Is the list sorted in ascending order?", is_sorted_ascending(lst_unsorted))
