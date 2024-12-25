input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
result_string = ''.join('*' if char in vowels else char for char in input_string)
print("After: ", result_string)