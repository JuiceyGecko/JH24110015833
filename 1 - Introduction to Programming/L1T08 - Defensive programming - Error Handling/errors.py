print("Welcome to the error program") # Syntax Error, fix by adding parentheses around the string.

print("\n") # Syntax Error, there was a indentation that was not needed, fix by removing it.

age = 24 # Runtime error, i removed the above code and just made the age equal to 24 so its more simple and trasferrable to the next sections
print("I'm " + str(age) + " years old.") # Logical error, the code wont print age unless its been cast with a string, just felt simpler to do. I added a string statement to age as its an integer.

years_from_now = 3 # Logical error, i removed the quotation marks around the 3. 
total_years = age + years_from_now 

print(f"The total number of years: {age} + {years_from_now}") # Logical error. It wasnt calculating the valuees, so i added the f string to calculate the actual value of "total_years". I also added the age variable into the formula so that it uses the above code in the equation.

total_months = total_years * 12 + 6 # Logical error. There wasnt a "6" added for the 6 months so the below total wouldnt have added, so i just added 6.

print(f"In 3 years and 6 months, I'll be {total_months} months old") # Syntax error, I fixed it by adding the f string so that the total_months would be calculated.
