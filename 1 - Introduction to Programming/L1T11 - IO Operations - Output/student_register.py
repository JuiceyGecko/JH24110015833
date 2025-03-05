# Prompt the user to enter the number of students joining
num_students = int(input("How many students are joining? "))

# Open the file 'reg_form.txt' in write mode ('w')
# Using 'with' ensures the file is properly closed after writing
with open('reg_form.txt', 'w') as file:
    # Loop through the number of students to collect their names
    for i in range(num_students):
        # Prompt the user to enter the name of the student
        name = input(f"Enter name of student and student ID number {i + 1}: ")
        # Write the student's name to the file, followed by a newline
        file.write(f"Student Name: {name}\n")
        # Add a separator between students for better readability
        # using a dotted line as requested
        file.write("\n" + "." * 40 + "\n\n")
    # Inform the user that the registration form has been successfully created
    print("Registration form has been successfully created.")
# End of with block, file is automatically closed
# End of program
