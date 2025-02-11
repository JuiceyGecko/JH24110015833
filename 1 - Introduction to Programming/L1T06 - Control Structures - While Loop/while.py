def get_number():
    # Initialize variables to keep track of the total sum and the count of valid numbers 
    total = 0  
    count = 0  

    # Continuously prompt the user for input until they choose to exit by entering -1
    while True:  
        # Prompt the user to enter a number between 1 and 10, or -1 to exit
        num = int(input("Enter a number between 1-10 (or -1 to exit): "))
        
        # Check if the user wants to exit the loop
        if num == -1: 
            break  # Exit the loop if -1 is entered

        # Validate that the number is within the acceptable range (1-10)
        elif 1 <= num <= 10:
            total += num 
            count += 1 
        else:
            # Inform the user if the number is invalid and prompt them to try again
            print("Invalid number. Please try again") 

    # Check if at least one valid number was entered
    if count > 0: 
        # Calculate the average of the valid numbers entered
        average = total / count 
        # Display the average to the user
        print(f"The average of the numbers the user has entered is: {average}")
    else:
        # Inform the user if no valid numbers were entered
        print("No valid numbers were entered") 

# Displays average for user
number = get_number()
