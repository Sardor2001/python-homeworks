given_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
odd_count = len([num for num in given_list if num % 2 == 1])
print(odd_count)
