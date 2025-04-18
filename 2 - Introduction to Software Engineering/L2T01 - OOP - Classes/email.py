"""Email Simulator"""


class Email:
    """A class to represent an email message.

    Attributes:
        has_been_read (bool): Class variable indicating if email has been read.
        email_address (str): The sender's email address.
        subject_line (str): The email's subject line.
        email_content (str): The body content of the email.
    """
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        """Initialize an Email instance.

        Args:
            email_address (str): Sender's email address
            subject_line (str): Email subject line
            email_content (str): Main content of email
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        """Mark the email as read by setting has_been_read to True."""
        self.has_been_read = True


# Initialize empty inbox list
inbox = []


def populate_inbox():
    """Create sample emails and add them to the inbox.

    Creates 3 sample Email objects with different subjects and content.
    """
    sample_emails = [
        Email("joe@gmail.com", "Don't forget to submit assignment",
              "Your submission is due tomorrow."),
        Email("Therapy@gmail.com", "Your account has been charged",
              "Your account has been charged R500."),
        Email("MTV@gmail.com", "Wacth MTV TONIGHT",
              "MTV is showing a new episode at 8pm."),
    ]
    inbox.extend(sample_emails)


def list_emails():
    """Display all emails in inbox with their index numbers.

    Prints:
        A numbered list of email subject lines.
    """
    for index, email in enumerate(inbox):
        print(f"{index}: {email.subject_line}")


def read_email(index):
    """Display a specific email and mark it as read.

    Args:
        index (int): The position of the email in the inbox list

    Prints:
        The full email content and updates its read status.
    """
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"\nContent:\n{email.email_content}\n")
        email.mark_as_read()
        print("Email marked as read.\n")
    else:
        print("Invalid email index.\n")


def display_unread_emails():
    """Show only unread emails from the inbox.

    Prints:
        A list of unread email subjects or a message if none exist.
    """
    unread_emails = [email for email in inbox if not email.has_been_read]

    if not unread_emails:
        print("\nNo unread emails.\n")
        return

    print("\nUnread Emails:")
    for email in unread_emails:
        print(f"- {email.subject_line}")


def main():
    """Run the email simulator program."""
    populate_inbox()

    while True:
        try:
            user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

Enter selection: '''))

            if user_choice == 1:
                print("\nAvailable emails:")
                list_emails()
                try:
                    email_index = int(input("\nEnter email number: "))
                    read_email(email_index)
                except ValueError:
                    print("Please enter a valid number.")

            elif user_choice == 2:
                display_unread_emails()

            elif user_choice == 3:
                print("Goodbye!")
                break

            else:
                print("Please enter 1, 2 or 3.")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
