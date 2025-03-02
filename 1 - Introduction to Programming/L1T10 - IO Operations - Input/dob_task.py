with open('c:/Users/steez/OneDrive/Desktop/JH24110015833-main/JH24110015833-main/1 - Introduction to Programming/L1T10 - IO Operations - Input/10-018 IO Operations - Input/Task file/DOB.txt', 'r') as file:
    # Initialize two empty lists to store names and birthdates
    names = []
    birthdates = []

    # Read each line in the file
    for line in file:
        # Split the line into parts 
        parts = line.strip().split()  # Remove leading/trailing spaces 
        # The name consists of the first name and last name
        name = ' '.join(parts[:2])  # Join the first two parts with a space
        # The birthdate consists of the remaining parts
        birthdate = ' '.join(parts[2:])  # Join the remaining parts with a space

        # Append the name and birthdate to their respective lists
        names.append(name)
        birthdates.append(birthdate)

# Print the names section
print("Name")
for name in names:
    print(name)

# Print the birthdates section
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)
