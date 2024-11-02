# Define three lists with different types of elements
fruits = ["apple", "banana", "cherry"]  # A list of strings representing fruits
numbers = [1, 2, 3, 4, 5]               # A list of integers representing numbers
mixed = [1, "hello", 3.5, True]         # A mixed list containing an integer, a string, a float, and a boolean

# Accessing list elements by index
print(fruits[0])    # Output: "apple" - Accesses the first element of the list
print(fruits[-1])   # Output: "cherry" - Accesses the last element using a negative index

# Modifying elements in a list
fruits[1] = "orange"  # Changes the second element from "banana" to "orange"

# Adding elements to a list
fruits.append("mango")  # Adds "mango" to the end of the list

# Inserting an element at a specific index
fruits.insert(1, "kiwi")  # Inserts "kiwi" at index 1, shifting elements to the right

# Extending a list with another list
fruits.extend(["pineapple", "grapes"])  # Adds "pineapple" and "grapes" to the end of the list

# Removing elements from a list
fruits.remove("banana")  # Removes the first occurrence of "banana" from the list (if it exists)

# Removing elements by index
fruits.pop()      # Removes and returns the last element ("grapes" in this case)
fruits.pop(0)     # Removes and returns the first element ("apple" in this case)

# Deleting elements using the `del` keyword
del fruits[2]     # Deletes the element at index 2
del fruits[1:3]   # Deletes elements from index 1 to index 2 (excluding index 3)

# Clearing all elements from the list
fruits.clear()    # Empties the list, removing all elements

# Combining lists
combined = fruits + numbers  # Creates a new list by adding elements of `fruits` and `numbers`

# Repeating a list
repeated = fruits * 3  # Repeats the list 3 times

# Slicing lists
print(fruits[1:3])   # Returns elements from index 1 to 2 (excluding 3)
print(fruits[:2])    # Returns elements from the start up to index 1 (excluding index 2)
print(fruits[1:])    # Returns elements from index 1 to the end of the list
print(fruits[::-1])  # Reverses the list by slicing with a step of -1

# List comprehensions
squares = [x ** 2 for x in range(10)]  # Creates a list of squares from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]  # Creates a list of even numbers from 0 to 9

# Getting the length of a list
print(len(fruits))  # Outputs the number of elements in `fruits`

# Finding minimum and maximum values
print(min(numbers))  # Outputs the smallest number in `numbers`
print(max(numbers))  # Outputs the largest number in `numbers`

# Summing up all elements in a list
print(sum(numbers))  # Returns the sum of all elements in `numbers`

# Finding the index of an element
print(fruits.index("apple"))  # Outputs the index of the first occurrence of "apple" in `fruits`

# Counting occurrences of an element
print(fruits.count("apple"))  # Outputs the number of times "apple" appears in `fruits`

# Sorting lists
numbers.sort()            # Sorts `numbers` in ascending order (modifies the list)
numbers.sort(reverse=True)  # Sorts `numbers` in descending order (modifies the list)
print(numbers)             # Outputs the sorted list

# Creating a sorted copy without modifying the original list
sorted_list = sorted(numbers)  # Creates a new sorted list from `numbers`

# Reversing the order of elements in a list
fruits.reverse()           # Reverses the order of elements in `fruits` (modifies the list)

# Copying a list
new_list = fruits.copy()   # Creates a copy of `fruits`, equivalent to `fruits[:]`

# Checking if an element is in a list
print("apple" in fruits)      # Outputs True if "apple" is in `fruits`, otherwise False
print("banana" not in fruits) # Outputs True if "banana" is not in `fruits`, otherwise False

# Iterating over a list
for fruit in fruits:
    print(fruit)  # Prints each element in `fruits`

# Using enumerate to get both index and value in a loop
for key, value in enumerate(fruits):
    print(key, value)  # Prints the index and element at each position in `fruits`

# Creating a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Output: 6 - Accesses the element in the 2nd row, 3rd column (index starts at 0)

# Using a list as a stack (LIFO - Last In, First Out)
stack = []
stack.append("apple")  # Adds "apple" to the stack
stack.pop()            # Removes and returns the last item ("apple"), following LIFO order

# Using a list as a queue (FIFO - First In, First Out)
queue = []
queue.append("apple")  # Adds "apple" to the queue
queue.pop(0)           # Removes and returns the first item ("apple"), following FIFO order
