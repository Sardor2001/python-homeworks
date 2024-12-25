tup = (1, 2, 3, 4, 5)
element = 3
new_tup = tuple(x for i, x in enumerate(tup) if x != element or (x == element and i != tup.index(element)))
print("New tuple:", new_tup)
