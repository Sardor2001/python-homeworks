import copy


def deep_copy_list(lst):
    return copy.deepcopy(lst)


# Example usage
original_list = [1, 2, [3, 4], 5]
copied_list = deep_copy_list(original_list)

# Modifying the copied list
copied_list[2][0] = 99

print("Original List:", original_list)
print("Copied List:", copied_list)
