def adding_up_to(numbers, index):
    # Base case.
    if index == 0:
        return numbers[0]

    # Recursive case.
    return numbers[index] + adding_up_to(numbers, index - 1)

# Test cases


print(adding_up_to([1, 2, 3], 2))              # Output: 6
print(adding_up_to([1, 2, 3, 4], 3))           # Output: 10
print(adding_up_to([1, 4, 5, 3, 12, 16], 4))  # Output: 25
print(adding_up_to([4, 3, 1, 5], 1))          # Output: 7
