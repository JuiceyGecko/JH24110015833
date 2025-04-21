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
    # Create an Adult instance
    adult = Adult("Joseph Holmes", 30, "blue", "brown")
    print(adult)  # Output: Joseph Holmes, 30, blue eyes, brown hair
    print(adult.can_drive())  # Output: Joseph Holmes can drive.

    # Create a Child instance
    child = Child("Kerry Holmes", 8, "green", "blonde")
    print(child)  # Output: Kerry Holmes, 8, green eyes, blonde hair
    print(child.can_drive())  # Output: Kerry Holmes is too young to drive.
