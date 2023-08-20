import datetime

employee_data = {} 

def ReadEmployeeData(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            emp_id, username, timestamp, gender, salary = line.strip().split(', ')
            employee_data[emp_id] = {
                'username' :  username,
                'emp_id': emp_id,
                'timestamp': timestamp,
                'gender': gender,
                'salary': int(salary)
            }

def save_employee_data(file_name):
    print(employee_data.items())
    with open(file_name, 'w') as file:
        for username, employee in employee_data.items():
            print(username)
            file.write(f"{employee['emp_id']}, {employee['username']}, {employee['timestamp']}, {employee['gender']}, {employee['salary']}\n")

def user_login():
    count = 0
    while count < 5:
        username = input("Enter your username: ")
        if username == "admin": 
            password = input("Enter your password: ")
            if password == "admin123123":
                display_admin_menu()
                break
        if username in employee_data:
            password = input("Enter your password: ")
            if len(password) == 0:
                display_user_menu(username)
                break
            else:
                print("Incorrect Username and/or Password")
                count += 1
        else:
            print("Incorrect Username and/or Password")
            count += 1
    else:
        print("You've reached the limit of incorrect credentials.")

def display_user_menu(username):
    gender = employee_data[username]['gender']
    title = "Mr." if gender == 'male' else "Ms."
    print(f"Hi {title} {username}")
    while True:
        print("1. Check my Salary")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Your salary is: {employee_data[username]['salary']}")
        elif choice == '2':
            save_login_timestamp(username)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

def save_login_timestamp(username):
    with open("login_timestamps.txt", 'a') as file:
        file.write(f"{username}, {getCurrentTime()}\n")

def getCurrentTime():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d")

def mainUser():
    ReadEmployeeData("employee_data.txt")
    print("Welcome to the Employee Management System!")

    user_login()


def display_admin_menu():
    choice= None
    while choice!=7:
        print("1. Display Statistics")
        print("2. Add an Employee")
        print("3. Display all Employees")
        print("4. Change Employee's Salary")
        print("5. Remove Employee")
        print("6. Raise Employee's Salary")
        print("7. Exit")
        choice= int(input("Enter your choice: ")) 
        
        if choice == 1:
            DisplayStatistics()
        elif choice == 2:
            AddEmployee()
        elif choice == 3:
            DisplayAll()
        elif choice == 4:
            ChangeSalary()
        elif choice == 5:
            Remove()
        elif choice == 6:
            Raise()
        elif choice == 7:
            save_employee_data("employee_data.txt")
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select again.")
            
def DisplayStatistics():
    male_count = 0
    female_count = 0
    
    for employee in employee_data:
        if employee_data[employee]['gender'] == 'male':
            male_count += 1
        elif employee_data[employee]['gender'] == 'female':
            female_count += 1

    print(f"Number of male employees: {male_count}")
    print(f"Number of female employees: {female_count}")

def AddEmployee():
    emp_id = "emp"+str(len(employee_data) + 1).zfill(3)  # Auto-increment employee ID
    username = input("Enter employee username: ")
    gender = input("Enter employee gender (male/female): ")
    salary = int(input("Enter employee salary: "))
    timestamp = getCurrentTime()

    employee_data[emp_id] = {
        'emp_id': emp_id,
        'username': username,
        'timestamp': timestamp,
        'gender': gender,
        'salary': salary
    }


def DisplayAll():
    sorted_employees = sorted(employee_data,reverse=True)
    print(sorted_employees)
    for employee in sorted_employees:
        print(f"ID: {employee_data[employee]['emp_id']}, Username: {employee_data[employee]['username']}, Gender: {employee_data[employee]['gender']}, Salary: {employee_data[employee]['salary']}")

def ChangeSalary():
    emp_id = input("Enter employee ID: ")
    new_salary = int(input("Enter new salary: "))
    found = False
    for employee in employee_data:
        if employee == emp_id:
            employee_data[employee]['salary'] = new_salary
            print("Salary updated successfully.")
            found = True
            return
    if not found: print("Employee not found.")

def Remove():
    emp_id = input("Enter employee ID to remove: ")
    if emp_id in employee_data:
        del employee_data[emp_id]
        print("Employee removed successfully.")
    else:
        print("Employee not found.")

def Raise():
    emp_id = input("Enter employee ID: ")
    raise_percentage = float(input("Enter raise percentage (e.g., 1.05 for 5% raise): "))
    for employee in employee_data:
        if employee == emp_id:
            employee_data[emp_id]['salary'] = int(employee_data[emp_id]['salary'] * raise_percentage)
            print("Salary raised successfully.")
            return
    print("Employee not found.")

def getCurrentTime():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d")

def main():
    ReadEmployeeData("employee_data.txt")
    # admin()
    mainUser()

main()
