# ASk user to enter all three sides of a triangle
# Calculate the Area of the triangle 
# Print out the area of the triangle

side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
print(area)
# End of Compulsory Task 4#

