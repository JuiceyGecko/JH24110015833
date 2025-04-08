from datetime import datetime
import os

# ====== File Paths ======
USER_FILE = "user.txt"
TASK_FILE = "tasks.txt"

# ====== Initialize Program ======


def initialize_files():
    # Create user and task files if they do not exist
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            f.write("admin, password")
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            pass

# ====== Login Section ======


def load_users():
    # Load users from the user file into a dictionary
    users = {}
    try:
        with open(USER_FILE, "r") as f:
            for line in f:
                if line.strip():
                    username, password = line.strip().split(", ")
                    users[username] = password
    except FileNotFoundError:
        initialize_files()
        return load_users()
    return users


def login():
    # Login function to authenticate users
    users = load_users()
    while True:
        print("\n" + "="*20)
        print("TASK MANAGER LOGIN")
        print("="*20)
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        if username in users and users[username] == password:
            print(f"\nWelcome, {username}!")
            return username
        print("\nInvalid credentials. Please try again.")

# ====== User Registration ======


def register_user(current_user):
    # Register a new user
    if current_user != "admin":
        print("\nOnly admin can register new users.")
        return
    users = load_users()
    print("\n" + "="*20)
    print("REGISTER NEW USER")
    print("="*20)
    while True:
        new_username = input("Enter new username: ").strip()
        if not new_username:
            print("Username cannot be empty.")
            continue
        if new_username in users:
            print("Username already exists.")
            continue
        break
    while True:
        new_password = input("Enter new password: ").strip()
        confirm_password = input("Confirm password: ").strip()
        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
        if not new_password:
            print("Password cannot be empty.")
            continue
        break
    with open(USER_FILE, "a") as f:
        f.write(f"\n{new_username}, {new_password}")
    print(f"\nUser '{new_username}' registered successfully!")

# ====== Task Functions ======


def add_task():
    # Add a new task
    users = load_users()
    print("\n" + "="*20)
    print("ADD NEW TASK")
    print("="*20)
    # Get assigned user
    while True:
        assigned_to = input("Enter username of assigned person: ").strip()
        if assigned_to not in users:
            print("User does not exist. Please try again.")
            continue
        break
    # Get task details
    title = input("Enter task title: ").strip()
    while not title:
        print("Title cannot be empty.")
        title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    while not description:
        print("Description cannot be empty.")
        description = input("Enter task description: ").strip()
    # Get and validate due date
    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    current_date = datetime.now().strftime("%Y-%m-%d")
    # Write to file
    with open(TASK_FILE, "a") as f:
        f.write(
            (
                f"\n{assigned_to}, {title}, {description}, "
                f"{current_date}, {due_date}, No"
            )
        )
    print("\nTask added successfully!")


def view_all_tasks():
    # View all tasks
    print("\n" + "="*20)
    print("ALL TASKS")
    print("="*20)
    try:
        with open(TASK_FILE, "r") as f:
            tasks = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("No tasks found.")
        return
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        assigned_to, title, description, assigned_date, due_date, completed = (
            task.split(", "))
        print(f"""
Task {i}:
Assigned to: {assigned_to}
Title: {title}
Description: {description}
Date Assigned: {assigned_date}
Due Date: {due_date}
Completed: {completed}
""")


def view_my_tasks(current_user):
    # View tasks assigned to the current user
    print("\n" + "="*20)
    print(f"TASKS ASSIGNED TO {current_user.upper()}")
    print("="*20)
    try:
        with open(TASK_FILE, "r") as f:
            tasks = [
                line.strip() for line in f
                if line.strip() and line.startswith(current_user)
            ]
    except FileNotFoundError:
        print("No tasks found.")
        return
    if not tasks:
        print("You have no tasks assigned.")
        return
    for i, task in enumerate(tasks, 1):
        (
            _, title, description,
            assigned_date, due_date, completed
        ) = task.split(", ")
        print(f"""
Task {i}:
Title: {title}
Description: {description}
Date Assigned: {assigned_date}
Due Date: {due_date}
Completed: {completed}
""")


def show_statistics():
    # Show statistics of tasks
    print("\n" + "="*20)
    print("TASK STATISTICS")
    print("="*20)
    try:
        with open(TASK_FILE, "r") as f:
            tasks = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("No tasks found.")
        return
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.split(", ")[-1] == "Yes")
    incomplete_tasks = total_tasks - completed_tasks
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Incomplete tasks: {incomplete_tasks}")


# ====== Main Program ======


def main():
    initialize_files()
    current_user = login()

    while True:
        print("\n" + "="*20)
        print("MAIN MENU")
        print("="*20)
        # Admin-specific menu
        if current_user == "admin":
            menu = input('''Select one of the following options:
r - Register a user
a - Add task
va - View all tasks
vm - View my tasks
s - Show statistics
e - Exit
: ''').lower().strip()
            if menu == 'r':
                register_user(current_user)
            elif menu == 'a':
                add_task()
            elif menu == 'va':
                view_all_tasks()
            elif menu == 'vm':
                view_my_tasks(current_user)
            elif menu == 's':
                show_statistics()
            elif menu == 'e':
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid option. Please try again.")
        # Regular user menu
        else:
            menu = input('''Select one of the following options:
a - Add task
va - View all tasks
vm - View my tasks
e - Exit
: ''').lower().strip()
            if menu == 'a':
                add_task()
            elif menu == 'va':
                view_all_tasks()
            elif menu == 'vm':
                view_my_tasks(current_user)
            elif menu == 'e':
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()
# This code is a simple task manager that allows users to register, login,
# and manage tasks.
