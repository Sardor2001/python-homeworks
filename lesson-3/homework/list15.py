given_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
even_count = len([num for num in given_list if num % 2 == 0])
print(even_count)
