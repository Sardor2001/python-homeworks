def remove_element_at_index(lst, index):
    # Check if the index is valid
    if index < 0 or index >= len(lst):
        return "Invalid index"

    # Remove the element at the specified index
    lst.pop(index)
    return lst


# Example usage
lst = [1, 2, 3, 4, 5]
index_to_remove = 2

print("Updated list:", remove_element_at_index(lst, index_to_remove))
