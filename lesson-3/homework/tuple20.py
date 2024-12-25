tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
n = 4
new_tup = tuple(tup[i:i + n] for i in range(0, len(tup) - len(tup) % n, n))
print("New tuple with subtuples:", new_tup)
