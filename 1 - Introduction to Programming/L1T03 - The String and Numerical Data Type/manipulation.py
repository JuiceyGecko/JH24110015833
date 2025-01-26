# Compulsory Task 2#

# Ask the user to enter a sentence using the input() method 
# Save the users response in a variable called str_manip.
# Calculate and print the length of str_manip. 
# Find the last letter in str_manip. 
# Replace every occurrence of this letter in str_manip with ‘@’.
# Print the last 3 characters in str_manip backwards.
# Create a five-letter word that is made up of the first three characters and the last two characters in str_manip.

str_manip = input("Enter a sentence: ")
print(len(str_manip))
last_letter = str_manip[-1]
print(last_letter)
str_manip = str_manip.replace(last_letter, '@')
print(str_manip[-3:][::-1])
new_word = str_manip[:3] + str_manip[-2:]
print(new_word)

# End of Compulsory Task 2#

























