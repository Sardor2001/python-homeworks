tup = (1, 2, 3, 4, 5)
unique_tup = set(tup)  # Remove duplicates
sorted_tup = sorted(unique_tup)  # Sort the tuple
second_largest = sorted_tup[-2] if len(sorted_tup) > 1 else None  # Handle case with less than 2 unique elements

print("The second largest element is:", second_largest)
