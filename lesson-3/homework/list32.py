def merge_and_sort_lists(lst1, lst2):
    # Merge the two lists and sort the result
    merged_list = lst1 + lst2
    return sorted(merged_list)


# Example usage
lst1 = [3, 1, 4]
lst2 = [2, 5, 0]

sorted_merged_list = merge_and_sort_lists(lst1, lst2)
print("Sorted merged list:", sorted_merged_list)
