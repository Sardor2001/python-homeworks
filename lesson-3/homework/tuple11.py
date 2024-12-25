tup = (1, 2, 3, 2, 4, 2, 5)
element = 2
indices = [index for index, value in enumerate(tup) if value == element]

print("Indices of the element:", indices)
