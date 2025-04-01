def largest_number(numbers):
    # Base case.
    if len(numbers) == 1:
        return numbers[0]

    # Recursive case: find the largest number in the rest of the list
    largest = largest_number(numbers[1:])
    return numbers[0] if numbers[0] > largest else largest


print(largest_number([1, 2, 3]))              # Output: 3
print(largest_number([1, 2, 3, 4]))           # Output: 4
print(largest_number([1, 4, 5, 3, 12, 16]))  # Output: 16
print(largest_number([4, 3, 1, 5]))          # Output: 5
