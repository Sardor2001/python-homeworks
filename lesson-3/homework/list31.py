def repeat_elements(lst, n):
    # Create a new list where each element is repeated 'n' times
    return [element for element in lst for _ in range(n)]


# Example usage
lst = [1, 2, 3]
n = 3

new_lst = repeat_elements(lst, n)
print("New list:", new_lst)
