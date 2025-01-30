name = input("Please provide your full name and surname: ").strip()

if len(name) == 0:
    print("You haven’t entered anything. Please enter your full name.")
elif len(name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(name.split()) < 2:
    print("Please make sure to enter both your name and surname.")
elif len(name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Thank you for providing your full name.")










