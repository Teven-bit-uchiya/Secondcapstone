# ===========importing Libraries=======#
from datetime import date, datetime
from os import path

from tomlkit import value


# Function to add a user to a text file
def add_user():
    # Declare variables to store username and password input
    new_username = input("Enter a username:\n")  # Store username input
    new_password = input("Enter a password:\n")  # Store password input
    confirm_password = input("Confirm password:\n")  # Store password input for confirmation

    # If password and confirm password match
    if new_password == confirm_password:
        with open("user.txt", "r") as f:  # Open the user.txt file in read mode
            for line in f:  # Iterate through each line in the file
                line = line.replace("\n", "").split(
                    ", ")  # Remove the newline at the end of each line and split each line where there is a comma

                if line[
                    0] != new_username:  # If the username from the file does not equal the username entered by the user
                    with open("user.txt", "a") as file:  # Open the user.txt file in append mode
                        file.write(f"\n{new_username}, {new_password}")  # Write the username and password to the file
                        print("User added successfully")  # Print success message to the user
                else:  # If the username from the file equals the username entered by the user
                    print("Username already exists")  # Print error message to the user
    else:
        print("Passwords do not match")  # If passwords do not match, print error message to the user


# here we are creating a function to add a task


def add_task():
    # here we are asking the user to input the username who the task is assigned to
    username_tasked = input("Enter the username whom the task is assigned to:\n")
    # here we are asking the user to input the title of the task
    task_title = input("Enter the title of the task:\n")
    # here we are asking the user to input the description of the task
    task_description = input("Enter the description of the task:\n")
    # here we are asking the user to input the due date of the task
    due_date = input("Enter the due date:\n")
    # here we are getting the current date
    today = date.today()
    # here we are changing the format of the output
    today = str(today.strftime("%d %B %Y"))
    # here we are setting the default value of whether the task has been completed to No
    task_complete = "No"
    # here we are opening the tasks.txt file
    with open("tasks.txt", "a") as f:
        # here we are appending the task to the file
        f.write(
            username_tasked + ", " + task_title + ", " + task_description + ", " + due_date + ", " + today + ", " + task_complete + "\n")


def view_all_tasks():
    """
    - Opens file in read mode
    - For each line of the file
        - Replaces newline character with nothing
        - Splits line at comma and space
        - Prints each line in a formatted way
    """
    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "").split(", ")
            print(
                f"\nTask: {line[1]}\nAssigned to: {line[0]} \nDate assigned: {line[4]}\nDue date: {line[3]}\nTask "
                f"complete?: {line[5]}\nTask description: {line[2]}\n")


def view_my_tasks():
    task_numb = 1
    tasks = {}
    # This opens the tasks.txt file, reads it and stores the data into a dictionary.
    with open("tasks.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "").split(", ")
            # If the data in the dictionary matches the user name, it prints the data out.
            tasks[task_numb] = line
            if line[0] == username:
                print(
                    f"Task number {task_numb}\nTask: {line[1]} \nAssigned to: {line[0]} \nDate assigned: {line[4]} "
                    # This asks the user to choose a number or a task or -1 to go to the main menu.
                    f"\nDue date: {line[3]} \nTask complete?: {line[5]} \nTask description: {line[2]}\n")
            # This asks the user to mark the task as complete or edit the task.
            task_numb += 1
    task_choice = int(input("Select either a specific task by entering a number or input -1 to the main menu: "))
    mark_edit_task = input('''Select one of the following Options below:
    mc -Mark task as complete
# If the user selects to mark the task as complete, it changes the value of the task to yes.
    ed - edit task:
    .lower''')
    if mark_edit_task == "mc":
        tasks[task_choice][5] = "Yes"
    # If the task is incomplete and the user selects to edit the task, it asks the user for the new user name and
    # due date, if the user selects that the task is completed, it tells them that they cannot edit it.
    else:
        if line[5] == "No":
            tasks[task_choice][0] = input("Edit user name: ")
            tasks[task_choice][3] = input("Edit due date: ")
        else:
            print("You cant edit completed tasks")
    # This writes the new data into the tasks.txt file.
    with open("tasks.txt", "w") as f:
        for task in tasks.values():
            f.write(f"{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {task[5]}\n")


# This writes the new data into the tasks.txt file.


# this function returns the number of tasks, completed tasks, uncompleted tasks and overdue tasks

def task_overview():
    no_of_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    uncompleted_overdue = 0
    today = date.today()

    # the no of tasks is incremented by 1 for every line in the file for each task

    with open("tasks.txt", "r") as f: # open the file in read mode
        for line in f: # iterate through each line in the file_content variables today and due datetime objects are created
            line = line.replace("\n", "").split(", ") # remove the newline at the end of each line and split each line where there is a comma
            no_of_tasks += 1 # increment the no_of_tasks variable by 1 for each line in the file for each task
            due_date = datetime.strptime(line[-2], "%d %b %Y").date() # convert the due date string to a datetime objects

            if line[-1] == "Yes": # if the task is completed_tasks is incremented by 1 for each line in the file for each tasks
                completed_tasks += 1 # increment the completed_tasks variable by 1 for each line in the file for each task
            elif line[-1] == "No":
                uncompleted_tasks += 1
                if today > due_date:
                    uncompleted_overdue += 1

    # the percentage of the number of uncompleted tasks is calculated and the percentage of the number of uncompleted
    # overdue tasks is calculated

    incomplete_percentage = round(((uncompleted_tasks / no_of_tasks) * 100), 2)
    overdue_percentage = round(((uncompleted_overdue / no_of_tasks) * 100), 2)

    # these are written to a new file

    with open("task_overview.txt", "w") as f:
        f.write(f"The total number of tasks: {no_of_tasks} \n"
                f"The total number  of completed tasks: {completed_tasks} \n"
                f"The total number of  uncompleted tasks: {uncompleted_tasks} \n"
                f"The total number of tasks that have not been completed and overdue: {uncompleted_overdue}%\n"
                f"The percentage of tasks that are incomplete: {incomplete_percentage}% \n"
                f"The percentage of tasks that are overdue: {overdue_percentage}%")


def task_overview():
    # Set variables to 0
    no_of_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    uncompleted_overdue = 0
    today = date.today()

    # Open file in read mode
    with open("tasks.txt", "r") as f:
        for line in f:
            # Replace newline with nothing and split on ", "
            line = line.replace("\n", "").split(", ")

            # Number of tasks is the length of the file
            no_of_tasks += 1

            # Set variable to the due date column, convert to date type
            due_date = datetime.strptime(line[-2], "%d %b %Y").date()

            # If statement to set completed tasks variable based on the completed column

            if line[-1] == "Yes":

                # Else statement to set uncompleted tasks variable and check if they are overdue
                completed_tasks += 1
            elif line[-1] == "No":
                uncompleted_tasks += 1
                if today > due_date:
                    uncompleted_overdue += 1

    # Calculate percentages
    incomplete_percentage = round(((uncompleted_tasks / no_of_tasks) * 100), 2)
    overdue_percentage = round(((uncompleted_overdue / no_of_tasks) * 100), 2)

    # Open file in write mode
    with open("task_overview.txt", "w") as f:
        # Write overview to file
        f.write(f"The total number of tasks: {no_of_tasks} \n"
                f"The total number  of completed tasks: {completed_tasks} \n"
                f"The total number of  uncompleted tasks: {uncompleted_tasks} \n"
                f"The total number of tasks that have not been completed and overdue: {uncompleted_overdue}%\n"
                f"The percentage of tasks that are incomplete: {incomplete_percentage}% \n"
                f"The percentage of tasks that are overdue: {overdue_percentage}%")


def user_overview():
    # Open user file to get number of users
    with open("user.txt", "r") as user_file:
        user_file_content = user_file.readlines()
        no_users = len(user_file_content)

    # Open task file to get number of tasks
    with open("tasks.txt", "r") as task_file:
        task_file_content = task_file.readlines()
        no_of_tasks = len(task_file_content)

    # Open user overview file to write data
    with open("user_overview.txt", "w") as my_file:

        # Loop through user file
        for line in user_file_content:
            # Remove \n and separate user and tasks
            line = line.replace("\n", "").split(", ")

            # Assign user to variable
            user = line[0]

            # Create variables to count users tasks
            user_total_tasks = 0
            user_completed = 0
            user_uncomplete = 0
            user_uncomp_overdue = 0
            # Loop through task file
            for line in task_file_content:

                # Remove \n and separate user, task data

                # Assign task to variable
                line = line.replace("\n", "").split(", ")

                # Check if user and task user match
                task_user = line[0]

                # If match do the following:
                if user == task_user:

                    # Convert todays date and due date to dates
                    todays_date = date.today().strptime(line[-3], "%d %b %Y").date()
                    due_date = datetime.strptime(line[-2], "%d %b %Y").date()

                    # Check if task is completed and count completed, uncompleted and uncompleted and overdue tasks

                    user_total_tasks += 1
                    if line[5] == "Yes":
                        user_completed += 1
                    elif line[5] == "No" and due_date < todays_date:

                        # Calculate task percentages
                        user_uncomp_overdue += 1
                    else:
                        user_uncomplete += 1

            # Write overview to file
            user_task_percentage = round(((user_total_tasks / no_of_tasks) * 100), 2)
            user_task_comp_percent = round(((user_completed / user_total_tasks) * 100), 2)
            user_task_uncomp_percent = round(((user_uncomplete / user_total_tasks) * 100), 2)
            user_task_uncomp_overdue_percent = round(((user_uncomp_overdue / user_total_tasks) * 100), 2)
            my_file.write(f"Number of User: {no_users}\n"
                          f"Number of Tasks: {no_of_tasks}\n"
                          f"Tasks user: {user}\n"
                          f"Total number of user tasks: {user_total_tasks}\n"
                          f"Total number of tasks user completed: {user_completed}\n"
                          f"Total number of tasks user uncompleted: {user_uncomplete}\n"
                          f"Total number of tasks user uncompleted and overdue: {user_uncomp_overdue}\n"
                          f"Percentage of tasks user has: {user_task_percentage}%\n"
                          f"Percentage of tasks user completed: {user_task_comp_percent}%\n"
                          f"Percentage of tasks user uncompleted: {user_task_uncomp_percent}%\n"
                          f"Percentage of tasks user uncompleted and overdue: {user_task_uncomp_overdue_percent}%\n")


def user_overview():

    #Open user file to get number of users
    with open("user.txt", "r") as user_file:
        user_file_content = user_file.readlines()
        no_users = len(user_file_content)

    #Open task file to get number of tasks
    with open("tasks.txt", "r") as task_file:
        task_file_content = task_file.readlines()
        no_of_tasks = len(task_file_content)

    #Open user overview file to write data
    with open("user_overview.txt", "w") as my_file:

        #Loop through user file
        for line in user_file_content:
            #Remove \n and separate user and tasks
            line = line.replace("\n", "").split(", ")

            #Assign user to variable
            user = line[0]

            #Create variables to count users tasks
            user_total_tasks = 0
            user_completed = 0
            user_uncomplete = 0
            user_uncomp_overdue = 0
            #Loop through task file
            for line in task_file_content:


                #Remove \n and separate user, task data

                #Assign task to variable
                line = line.replace("\n", "").split(", ")

                #Check if user and task user match
                task_user = line[0]

                #If match do the following:
                if user == task_user:

                    #Convert todays date and due date to dates
                    todays_date = date.today().strptime(line[-3], "%d %b %Y").date()
                    due_date = datetime.strptime(line[-2], "%d %b %Y").date()

                    #Check if task is completed and count completed, uncompleted and uncompleted and overdue tasks

                    user_total_tasks += 1
                    if line[5] == "Yes":
                        user_completed += 1
                    elif line[5] == "No" and due_date < todays_date:

                    #Calculate task percentages
                        user_uncomp_overdue += 1
                    else:
                        user_uncomplete += 1


            #Write overview to file
            user_task_percentage = round(((user_total_tasks / no_of_tasks) * 100), 2)
            user_task_comp_percent = round(((user_completed / user_total_tasks) * 100), 2)
            user_task_uncomp_percent = round(((user_uncomplete / user_total_tasks) * 100), 2)
            user_task_uncomp_overdue_percent = round(((user_uncomp_overdue / user_total_tasks) * 100), 2)
            my_file.write(f"Number of User: {no_users}\n"
                        f"Number of Tasks: {no_of_tasks}\n"
                        f"Tasks user: {user}\n"
                        f"Total number of user tasks: {user_total_tasks}\n"
                        f"Total number of tasks user completed: {user_completed}\n"
                        f"Total number of tasks user uncompleted: {user_uncomplete}\n"
                        f"Total number of tasks user uncompleted and overdue: {user_uncomp_overdue}\n"
                        f"Percentage of tasks user has: {user_task_percentage}%\n"
                        f"Percentage of tasks user completed: {user_task_comp_percent}%\n"
                        f"Percentage of tasks user uncompleted: {user_task_uncomp_percent}%\n"
                        f"Percentage of tasks user uncompleted and overdue: {user_task_uncomp_overdue_percent}%\n")


# log in section
user_names = {}
with open("user.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "").split(", ")
        user_names[username_f] = password_f
# verify username

username = input("Enter your username:\n")
while username not in user_names:
    print("Invalid username")
    username = input("Enter your username:\n")

# verify password
password = input("Enter your password:\n")
while password != user_names[username]:
    print("Invalid password")
    password = input("Enter your password:\n")

# While loop for program to always be running
while True:
    # If statement to determine if user is admin or not
    if username == "admin":
        # Admin menu
        menu = input("Menu:\n"
                     "r - register user\n"
                     "a - add task\n"
                     "va - view all tasks\n"
                     "vm - view my tasks\n"
                     "e - exit\n")
        # Options for admin to choose
        if menu == "r":
            register_user()
        elif menu == "a":
            add_task()
        elif menu == "va":
            view_all_tasks()
        elif menu == "vm":
            view_my_tasks()
        elif menu == "gr":
            generate_reports()
        elif menu == "ds":
            display_stats()
        elif menu == "e":
            break
        # If user is not admin print this menu
        print("Welcome admin select an option from the menu below")
        print("r - Add user")
        print("a - Add task")
        print("va - View all tasks")
        print("vm - Generate statistics")
        print("e -Exit")
        choice = input("Enter your choice:\n")
        # Menu options
        if choice == "r":
            add_user()
        elif choice == "a":
            add_task()
        elif choice == "va":
            view_all_tasks()
        elif choice == "vm":
            task_overview()
            user_overview()
            display_stats()
        elif choice == "e":
            print("Goodbye")
            exit()
        # If user selects invalid option
        else:
            print("Invalid choice not in menu")
    # If user is not admin
    else:
        # User menu
        menu = input("Welcome user select an option from the menu below:\n"
                     "a - Add task\n"
                     "va - View all tasks\n"
                     "vm - View my tasks\n"
                     "e - Exit\n"
                     "Enter your choice:\n")
        # Menu options
        if menu == "a":
            add_task()
        elif menu == "va":
            view_all_tasks()
        elif menu == "vm":
            view_my_tasks()
        # If user selects exit
        elif menu == "e":
            print("Goodbye user {}".format(username))
            exit()
        # If user selects invalid option
        else:
            print("Invalid choice not in menu")
