lst = [1, 2, 2, 3, 4, 3, 5, 6, 6]
unique_lst = []

for item in lst:
    if item not in unique_lst:
        unique_lst.append(item)

print("Unique List:", unique_lst)
