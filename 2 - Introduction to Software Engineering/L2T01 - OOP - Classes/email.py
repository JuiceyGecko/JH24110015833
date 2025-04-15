### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

 # Create Email Class
class Email:
    # Class Variable 
    has_been_read = False 

    # Constructor method
    def __init__(self, email_address, subject_line, sender):
        # Instance variables
        self.email_address = email_address
        self.subject_line = subject_line
        self.sender = sender
    
    def mark_as_read(self):
        # Change has_been_read to True 
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.

inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
# Create 3 sample emails and add it to the Inbox list. 


  email1 = Email("joe@gmail.comn", "Hyperion Dev Project", "Joseph Holmes")
  email2 = Email("Sars@gmail.com", "Tax Return", "South African Revenue Service")
  email3 = Email("AfricanBank@gmail.com", "Loan Application", "African Bank")

  # Emails Added to inbox
  inbox.append(email1)
  inbox.append(email2)
  inbox.append(email3)

def list_emails():

    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for index, email in enumerate(inbox):
        print(f"{index + 1}. {email.subject_line}")

def read_email(index):

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Email from {email.email_address} has been read.")
    else:
        print("Invalid email number.")

# --- Email Program --- #
populate_inbox()  # Call the function 

# Call the function to populate the Inbox list with the sample emails.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
    if user_choice == 1:
        # add logic here to read an email
        print("\nSelect an email number to read:")
        list_emails()
        try:
            email_number = int(input("Enter email number: ")) - 1
            read_email(email_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif user_choice == 2:
        # add logic here to view unread emails
            print("\nUnread Emails:")
            unread_found = False
            for email in inbox:
                if not email.has_been_read:
                    print(f"- {email.subject_line}")
                    unread_found = True
            if not unread_found:
                print("No unread emails found.")

    elif user_choice == 3:
        # add logic here to quit appplication
        print("Exiting application.")
        break # ends loop
    else:
        print("Oops - incorrect input.")
