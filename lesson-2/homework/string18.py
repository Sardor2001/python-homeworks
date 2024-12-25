input_string = input("Enter a string: ")
start_word = input("Start Word: ")
end_word = input("End Word: ")

if input_string.startswith(start_word) and input_string.endswith(end_word):
    print("True")
else:
    print("False")