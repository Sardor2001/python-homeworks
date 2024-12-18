input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"

vowels_count = 0
consonants_count = 0

for char in input_string:
    if char.isalpha():
        if char in vowels:
            vowels_count+=1
        else:
            consonants_count+=1


print(f"Vowels: {vowels_count}")
print(f"Consonants count: {consonants_count}")


