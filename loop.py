# List of fruits
fruits = ["apple", "banana", "cherry"]
# Iterating over each fruit in the list
for fruit in fruits:
    print(fruit)  # Prints each fruit on a new line

# Tuple of colors
colors = ("red", "green", "blue")
# Iterating over each color in the tuple
for color in colors:
    print(color)  # Prints each color on a new line

# Iterating over each character in the string "hello"
for char in "hello":
    print(char)  # Prints each character in "hello" on a new line

# Iterating over a range of numbers from 0 to 4
for i in range(5):
    print(i)  # Prints numbers 0 to 4, one per line

# Iterating over a range of numbers starting from 1 to 9, stepping by 2
for i in range(1, 10, 2):  # Start at 1, end before 10, step by 2
    print(i)  # Prints 1, 3, 5, 7, 9, one per line

# Creating a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterating over each row in the matrix
for row in matrix:
    # Iterating over each number in the current row
    for num in row:
        print(num, end=' ')  # Print numbers in the same row on the same line, separated by space
    print()  # Print a newline after finishing a row

# List of fruits
fruits = ["apple", "banana", "cherry"]
# Using enumerate to get both index and fruit
for index, fruit in enumerate(fruits):
    print(index, fruit)  # Prints the index and the corresponding fruit

# List comprehension to generate squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Prints the list of squares [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Iterating over a range of numbers from 0 to 9
for i in range(10):
    if i == 5:
        break  # Exit the loop if i equals 5
    print(i)  # Prints numbers 0 to 4

# Iterating over a range of numbers from 0 to 4
for i in range(5):
    if i == 2:
        continue  # Skip the current iteration when i equals 2
    print(i)  # Prints 0, 1, 3, 4 (skips printing 2)

# Iterating over a range of numbers from 0 to 2
for i in range(3):
    print(i)  # Prints numbers 0 to 2
else:
    print("Loop completed!")  # This will execute after the loop finishes without any interruption
