main_list = input("Enter the main list (space-separated values): ").split()
sub_list = input("Enter the sublist (space-separated values): ").split()


# Check if the sublist exists
def is_sublist(main_list, sub_list):
    n, m = len(main_list), len(sub_list)
    return any(main_list[i:i + m] == sub_list for i in range(n - m + 1))


# Result
exists = is_sublist(main_list, sub_list)
print("Sublist exists:", exists)
