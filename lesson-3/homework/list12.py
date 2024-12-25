list = (input("Enter the list elements seperated by spaces: ")).split()
element = input("Enter the element: ")
index = int(input("Enter the index: "))
list.insert(index, element)

print("The list:", list)