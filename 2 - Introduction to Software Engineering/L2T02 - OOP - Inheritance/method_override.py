""" Inheritance and method overriding example."""


class Adult:
    """Represents an adult with driving capability information."""

    def __init__(self, name, age, eye_color, hair_color):
        """Initialize adult attributes."""
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

    def __str__(self):
        """Return string representation of the adult."""
        return (
            f"{self.name}, {self.age}, "
            f"{self.eye_color} eyes, "
            f"{self.hair_color} hair"
        )

    def can_drive(self):
        """Check if adult is old enough to drive."""
        return (
            f"{self.name} can drive."
            if self.age >= 18
            else f"{self.name} cannot drive."
        )


class Child(Adult):
    """Represents a child (inherits from Adult but cannot drive)."""

    def can_drive(self):
        """Override to indicate child cannot drive."""
        return f"{self.name} is too young to drive."


if __name__ == "__main__":
    # Get user input for adult attributes
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    user_eye_color = input("Enter your eye color: ")
    user_hair_color = input("Enter your hair color: ")

    # Create an Adult object
    if user_age >= 18:
        person = Adult(user_name, user_age, user_eye_color, user_hair_color)
    else:
        person = Child(user_name, user_age, user_eye_color, user_hair_color)

    # Print the person's details and driving capability
    print(person)
    print(person.can_drive())
