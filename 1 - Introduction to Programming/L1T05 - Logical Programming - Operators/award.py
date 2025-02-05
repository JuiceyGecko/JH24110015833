
# Compulsory Task 1

# I am first making sure that the numbers inputed are valid numbers and not any other characters are input
# I am then asking the user to input the number of minutes they spent swimming, cycling and running
# I am then adding the total time of the three activities
# I am then printing the total time spent by the candidate
# I am then checking if the candidate qualifies for the award


def validate_numbers(value): # This lets me check if the input is a number 
    try:
        int(value)   # This will check if the input is a number
        return True  # If the input is a number it will return True
    except ValueError: # If the input is not a number it will return False
        return False  # If the input is not a number it will return False

swimming = input("Enter the number of minutes the candidate spent swimming: ") # This will prompt the user to enter the number of minutes
if validate_numbers(swimming): # This will check if the input is a number
    minutes = int(swimming) # This will convert the input to an integer
    print(f"{swimming} minutes ") # this will place the minutes entered by the user easier with the f string
else:
    print("Invalid input. Please enter a valid number without any special characters;.") # This will print if the input is not a number
    
cycling = input("Enter the number of minutes the candidate spent cycling: ") # This will prompt the user to enter the number of minutes
if validate_numbers(cycling): # This will check if the input is a number
    minutes = int(cycling) # This will convert the input to an integer
    print(f"{cycling} minutes ") # this will place the minutes entered by the user easier with the f string
else:
    print("Invalid input. Please enter a valid number without any special characters;.")

running = input("Enter the number of minutes the candidate spent running: ") # This will prompt the user to enter the number of minutes
if validate_numbers(running): # This will check if the input is a number
    minutes = int(running) # This will convert the input to an integer
    print(f"{running} minutes ") # this will place the minutes entered by the user easier with the f string
else:
    print("Invalid input. Please enter a valid number without any special characters;.")

total_time = int(swimming) + int(cycling) + int(running) # This will add the total time of the three activities
print(f"The total time spent by the candidate to complete the triathalon is {total_time} minutes") # This will print the total time spent by the candidate
if total_time == 100:
    print("The candidate qualifies for the award") #If the candidate is within 100 minutes they recieve a award
elif 95 <= total_time < 100:
    print("The candidate will recievce provincial half colours") # If the candidate is within 5 minutes of 100 they recieve provincial half colours                                                        
elif 90 <= total_time < 100:
    print("The candidate will recieve a provincial scroll") #If Its within 10 minutes the candidate will get a provinical scroll
elif 110 >= total_time > 100:
    print("The candidate will get no reward") #If a number is between 101-infinity the output is no reward
else:
    print("Better luck next time ★") #I added this for candidates that took a little longer than usual :) 
    #if the candidates are way out the range between 111-infinity then they get a comforting response. 
    