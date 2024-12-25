lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n = 3

# Trim the list to the nearest multiple of n
lst = lst[:len(lst) - len(lst) % n]

# Create the sublists
sublists = [lst[i:i + n] for i in range(0, len(lst), n)]

print("Sublists:", sublists)

