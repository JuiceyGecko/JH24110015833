# Compulsory Task 1#

print("Please enter the following sentence: The quick brown fox jumps over the lazy dog")
my_string = input()
print("The!quick!brown!fox!jumps!over!the!lazy!dog.", my_string)
modified_string = my_string.replace("!", " ")
print(modified_string)
print(modified_string.upper())
print(modified_string[::-1])

# Something thats bothering me, in the terminal the output prints out !The!quick!brown!fox!jumps!over!the!lazy!dog. The quick brown fox jumps over the lazy dog. 
# I dont know why its priting out that and the other one because if i dont identify it is a string it gives me syntax error, 
# just want to make the terminal outut neater and struggling to figure that out
# then i tried a different approac and asked the user to enter the sentence in the begging just to see if it flows better.... 