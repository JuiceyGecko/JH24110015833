# Capitalize every other letter in a string
character_name = "Joseph Holmes"
capitalized_character_name = ""

# Loop through the string and capitalize every other letter
for index in range(len(character_name)):
    if index % 2 == 0: 
        capitalized_character_name += character_name[index].upper()
    else:
        capitalized_character_name += character_name[index].lower()

print(capitalized_character_name)

# Capitalize every other word in the string
character_name = "Joseph Holmes is the main character of the story."

# Split the string into a list of words, and capatilize every other word 
# starting from the second word.
words = character_name.split()
words[1::2] = map(str.upper, words[1::2])
character_name = " ".join(words)

# Print the new string
print(character_name)
