list = (input("Enter the list elements seperated by spaces: ")).split()
list = [float(num) for num in list]
print(f"Listdagi sonlar yig'indisi: {sum(list)}")