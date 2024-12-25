def rotate_list(lst):
    # Check if the list is not empty
    if lst:
        # Rotate the list by slicing: take the last element and add the rest of the list
        return [lst[-1]] + lst[:-1]
    return lst  # If the list is empty, return it as is


# Example usage
lst = [1, 2, 3, 4, 5]
rotated_list = rotate_list(lst)
print("Rotated List:", rotated_list)
