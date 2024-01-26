# 'datetime' library was imported to get current system time, date and layout
import datetime 

# Empty lists were created to store any usernames and passwords currently registered or that will be registered
usernames = []
passwords = []

# LOGIN DETAILS BLOCK
# 'user.txt' file was opened, and the admin username and password was assigned into the empty lists above
print("Login Details")

with open("user.txt", "r") as file:
    for line in file:
        admin = line.strip().split(", ")
        usernames.append(admin[0])  
        passwords.append(admin[1]) 

while True:
    entered_username = input("Please enter a username: ")
    entered_password = input("Please enter a password: ")
    
    # 'if and else' statments used to validate whether entered details correspond within the usernames and password lists
    # The index variable was created to locate the position of the stored details in the list
    if entered_username in usernames:
        index = usernames.index(entered_username)
        if entered_password == passwords[index]:
            print("\nLogin successful! Welcome to the menu.")
            break
        else:
            print("Invalid password. Please enter the correct password.")
    else:
        print("Username not found. Please try again!\n")

# MENU BLOCK
# 'while' loop created to repeat options for user until user exits menu
# 'if' statement displays admin menu with 'ds' as option and 'else' statement displays normal user menu options
while True:
    if entered_username == 'admin': 
        print("\nPlease select one of the following options:")
        print("r - register a user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("ds - display statistics")
        print("e - exit")
    
    else:
        print("\nPlease select one of the following options:")
        print("r - register a user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("e - exit")
    
    menu = input("User option: ").lower()
    
    # REGISTER USER BLOCK (ADMIN ONLY)
    # 'if and else' statement used to register user, of which, nested 'if and else' statement used in order to assign only admin the registration privileges 
    # Once users details confirmed, details are written to the 'user.txt' file
    if menu == 'r':
        if entered_username == 'admin':
            with open('user.txt', 'r+') as file:
                new_username = input("\nPlease enter a new username: ")
                new_password = input("Please enter a new password: ")
                confirm_password = input("Please confirm new password again: ")

                if new_password == confirm_password:
                    file.seek(0, 2)
                    file.write('\n' + new_username + ', ' + new_password)
                    usernames.append(new_username)
                    passwords.append(new_password)
                    print("User registered successfully!")
                
                else:
                    print("The passwords entered do no not match, please try again!")
        else:
            print("Sorry, only admin is allowed to register users!")

    # ADD TASK BLOCK
    # 'elif' statement used to open, write to and append new task details to 'task.txt' file utilizing the datetime library for current system time 
    elif menu == 'a':
        with open('tasks.txt', 'a') as tasks_file:
            username_task = input("\nPlease enter the username of the person the task is assigned to: ")
            task_title = input("Please enter the title of the task: ")
            task_description = input("Please enter the description of the task: ")
            due_date = input("Please enter the due date of the task (e.g. 01 Sept 2019): ")
            current_date = datetime.datetime.now().strftime("%d %b %Y")
            task_completion = 'No'
            
            task_details = f"\n{username_task}, {task_title}, {task_description}, {due_date}, {current_date}, {task_completion}"            
            tasks_file.write(task_details)
            
            print("Task added successfully!")

    # VIEW ALL TASKS BLOCK
    # 'elif' statement used to open and read each task deatil, utilizing list indexing to classify and seperate each variable assigned to the task 
    elif menu == 'va':
        with open('tasks.txt', 'r') as tasks_file:
            task_counter = 0 
            for line in tasks_file:
                task_counter += 1
                task = line.strip().split(', ')
                
                username_task = task[0]
                task_title = task[1]
                task_description = task[2]
                due_date = task[3]
                date_assigned = task[4]
                task_completion = task[5]
                
                print(f"\nTask {task_counter}")
                print(f"Username: {username_task}")
                print(f"Title of task: {task_title}")
                print(f"Task description: {task_description}")
                print(f"Due date: {due_date}")
                print(f"Date assigned: {date_assigned}")
                print(f"Task completed: {task_completion}\n")

    # VIEW USER ASSIGNED TASK BLOCK
    # 'elif' statement used to open and read task details assigned to a specific registered user according to login username
    elif menu == 'vm':
        if entered_username in usernames:
            with open("tasks.txt", "r") as tasks_file:
                for line in tasks_file:
                    task = line.strip().split(', ')
                    
                    if task[0] == entered_username:              
                        task_title = task[1]
                        task_description = task[2]
                        due_date = task[3]
                        date_assigned = task[4]
                        task_completion = task[5]

                        print(f"\nThe task details for user '{entered_username}' is as follows:")
                        print(f"Title of task: {task_title}")
                        print(f"Task description: {task_description}")
                        print(f"Due date: {due_date}")
                        print(f"Date assigned: {date_assigned}")
                        print(f"Task completed: {task_completion}\n")

    # DISPLAY STATISTICS BLOCK (ADMIN ONLY)
    # 'elif' statement used for admin menu option 'ds' where the number of usernames is counted and displayed as both a number and a list
    # 'tasks.txt' file is opened and read in order to gather and display the number of tasks as well as listing the title of each task
    elif menu == 'ds':
        number_of_users = len(usernames)        
        print(f"\nThe total number of usernames is: {number_of_users} \nThey are listed as follows: {usernames}")
        
        with open('tasks.txt', 'r') as tasks_file:
            number_of_tasks = 0           
            task_titles = []
            
            for line in tasks_file:               
                task = line.strip().split(', ')
                
                number_of_tasks += 1
                task_titles.append(task[1])

            print(f"\nThe total number of tasks is: {number_of_tasks}")
            print(f"Title of each task is: \n{task_titles}")

    # EXIT BLOCK
    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")
    break