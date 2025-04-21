"""Compulsory Task 1"""


class Course:
    """
    Displays a Course for Computer Science enthusiasts.
    """
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        """Prints the contact website."""
        print("Please contact us by visiting", self.contact_website)

    def course_name(self):
        """Prints the course name."""
        print("The course name is:", self.name)

    def location(self):
        """Prints the location of the course."""
        print("The location is: Cape Town")


class OOPCourse(Course):
    """
    Represents an OOP course, inheriting from the Course class.
    Adds attributes for description and trainer.
    """

    def __init__(self, description="OOP Fundamentals",
                 trainer="Mr Anon A. Mouse"):
        """Constructor to initialize attributes: description, trainer."""
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        """Prints trainer details."""
        print("Trainer:", self.trainer)
        print("Description:", self.description)

    def show_course_id(self):
        """ Prints the Available course ID """
        print("Course ID: 12345")


if __name__ == "__main__":
    # Create a Course object
    my_course = Course()

    # Call the methods
    my_course.contact_details()
    my_course.location()

    # Create an OOPCourse object
    course_1 = OOPCourse()
    course_1.trainer_details()
    course_1.contact_details()
