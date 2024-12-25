list = (input("Enter the list elements seperated by spaces: ")).split()

if len(list)!=0:
    print(list[-1])
else:
    print("The list is empty")