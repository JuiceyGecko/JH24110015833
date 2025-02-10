
# Compulsory Task 1

def validate_numbers(value): 
    try:
        int(value)  # Help convert input to an integer
        return True  # If successful, return True
    except ValueError: 
        return False  # If conversion fails, return False
    
# The above code will help me validate the user's input so that it's processed as an integer.

swimming = input("Enter the number of minutes the candidate spent swimming: ")
if validate_numbers(swimming): 
    minutes_swimming = int(swimming)  # Convert input to integer
    print(f"{swimming} minutes") 
else:
    print("Invalid input. Please enter a valid number without any special characters.")

cycling = input("Enter the number of minutes the candidate spent cycling: ")
if validate_numbers(cycling): 
    minutes_cycling = int(cycling)  # Convert input to integer
    print(f"{cycling} minutes") 
else:
    print("Invalid input. Please enter a valid number without any special characters.")

running = input("Enter the number of minutes the candidate spent running: ") 
if validate_numbers(running): 
    minutes_running = int(running)  # Convert input to integer
    print(f"{running} minutes")
else:
    print("Invalid input. Please enter a valid number without any special characters.")

# The above code will prompt the user for the number of minutes spent on each activity (swimming, cycling, running),
# validate the input, convert it to an integer, and calculate the total time spent.

total_time = minutes_swimming + minutes_cycling + minutes_running 
print(f"The total time spent by the candidate to complete the triathlon is {total_time} minutes") 

if total_time <= 100:
    print("Provincial Colours")
elif 101 <= total_time <= 105:
    print("Provincial Half Colours") 
elif 106 <= total_time <= 110:
    print("Provincial Scroll")
else: 
    print("No Award")

# The above code will calculate total time spent on the three activities, then give out the corresponding rewards.