username = input("Enter a username: ")
password = input("Enter your password: ")

if not username or not password:
    print("Username or password cannot be empty")
else:
    print("Credentials are valid")
