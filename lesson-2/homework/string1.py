from datetime import datetime

name = input("Name: ")
year = int(input("Year of birth: "))

current_year = datetime.now().year

age = current_year - year

print(f"Hello, {name}! Your age is {age} years old.")