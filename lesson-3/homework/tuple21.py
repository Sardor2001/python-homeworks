tup = (1, 2, 3, 4)
n = 3
new_tup = tuple(x for x in tup for _ in range(n))
print("New tuple:", new_tup)
