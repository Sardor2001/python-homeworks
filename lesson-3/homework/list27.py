def max_in_sublist(lst, start, end):
    # Check if the provided indices are valid
    if start < 0 or end >= len(lst) or start > end:
        return "Invalid indices"

    # Extract the sublist and find the maximum element
    sublist = lst[start:end + 1]
    return max(sublist)


# Example usage
lst = [1, 5, 3, 9, 7, 6, 4]
start_index = 2
end_index = 5

print("Maximum element in sublist:", max_in_sublist(lst, start_index, end_index))
