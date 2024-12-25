# Input the list and the elements to replace
my_list = input("Enter the list (space-separated values): ").split()
old_element = input("Enter the element to replace: ")
new_element = input("Enter the new element: ")

# Replace the first occurrence of the old element with the new element
if old_element in my_list:
    index = my_list.index(old_element)  # Find the first occurrence
    my_list[index] = new_element  # Replace it

# Output the modified list
print("Modified List:", my_list)
