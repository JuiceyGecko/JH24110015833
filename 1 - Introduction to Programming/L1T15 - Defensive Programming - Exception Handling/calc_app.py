# Description: A simple calculator app.

import os
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "equations.txt")


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Define the arithmetic functions


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    while b == 0:  # Loop until a valid divisor is entered
        print("Error! Division by zero.")
        try:
            b = int(input("Please re-enter a non-zero divisor: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            b = 0  # Reset to ensure the loop continues
    return a / b


# Take input from the user
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:
        break
    else:
        print("Invalid Input! Please enter a valid choice.")

# Take input from the user for the two numbers
while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input! Please enter integers only.")

result = None  # Initialize result variable
if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif choice == '3':
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif choice == '4':
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")

else:
    print("Invalid Input! Please enter a valid choice.")

# Save the result to a file
try:
    with open(file_path, "a") as file:  # Use the correct file path
        if choice == '1':
            file.write(f"{num1} + {num2} = {result}\n")
        elif choice == '2':
            file.write(f"{num1} - {num2} = {result}\n")
        elif choice == '3':
            file.write(f"{num1} * {num2} = {result}\n")
        elif choice == '4':
            file.write(f"{num1} / {num2} = {result}\n")
    print("Calculation saved to file.")
except IOError:
    print("Error: Unable to write to file.")

print("Would you like to print previous calculations? (y/n)")
while True:
    print_choice = input("Enter choice (y/n): ").lower()  # Convert to lowercase for consistency
    if print_choice in ['y', 'n']:
        if print_choice == 'n':
            print("Exiting the program.")
            break
        if print_choice == 'y':
            try:
                # Open the file and read its contents
                with open(file_path, "r") as file:
                    print("Previous Calculations:")
                    print(file.read())  # Print the contents of the file
            except FileNotFoundError:
                print("No previous calculations found. The file does not exist.")
            except IOError:
                print("Error: Unable to read the file.")
        break
    else:
        print("Invalid Input! Please enter 'y' or 'n'.")
