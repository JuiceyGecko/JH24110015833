# Pyramid Pattern using a single for loop

# Loop from 1 to 9
for i in range(1,10) :
    if i <= 5 :
        # Print stars in increasing order for the first 5 rows
        print("*" * i) # Prints the asterix i times.
    else: 
        # Print stars in decreasing order for the last 4 rows
        print("*" * (10 - i))  # Ensures that the number of stars decreases as I increases.
   