# Function to add a new employee record
def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee record added successfully!")


# Function to view all employee records
def view_all_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if records:
                print("Employee Records:")
                for record in records:
                    print(record.strip())
            else:
                print("No employee records found.")
    except FileNotFoundError:
        print("No employee records file found.")


# Function to search for an employee by Employee ID
def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            found = False
            for record in records:
                if record.startswith(emp_id):
                    print("Employee found:", record.strip())
                    found = True
                    break
            if not found:
                print("Employee not found.")
    except FileNotFoundError:
        print("No employee records file found.")


# Function to update an employee's information
def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    found = False
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
        with open("employees.txt", "w") as file:
            for record in records:
                if record.startswith(emp_id):
                    found = True
                    print("Current Record:", record.strip())
                    name = input("Enter new Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")
                    file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                    print("Employee record updated successfully!")
                else:
                    file.write(record)
        if not found:
            print("Employee ID not found.")
    except FileNotFoundError:
        print("No employee records file found.")


# Function to delete an employee record
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    found = False
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
        with open("employees.txt", "w") as file:
            for record in records:
                if record.startswith(emp_id):
                    found = True
                    print("Employee record deleted.")
                else:
                    file.write(record)
        if not found:
            print("Employee ID not found.")
    except FileNotFoundError:
        print("No employee records file found.")


# Main program loop with menu options
def main():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
