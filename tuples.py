# Basic tuple creation with parentheses
point = (3, 5)  # A tuple with two elements, 3 and 5, representing a point

# Tuple creation without parentheses
numbers = 1, 2, 3  # A tuple can be created without parentheses; this creates (1, 2, 3)

# Creating an empty tuple
empty_tuple = ()  # An empty tuple, which contains no elements

# Single-element tuple (note the comma is necessary)
single_element_tuple = (5,)  # Creates a tuple with a single element, 5; without the comma, it would be an integer

# Accessing elements in a tuple by index
colors = ("red", "green", "blue")  # A tuple of color names
print(colors[0])      # Output: "red" - accesses the first element of the tuple
print(colors[-1])     # Output: "blue" - accesses the last element using negative indexing

# Attempting to modify a tuple (will raise an error)
colors = ("red", "green", "blue")
# colors[0] = "yellow"  # Raises a TypeError because tuples are immutable and cannot be changed

# Nested tuples and modifying a mutable element within a tuple
nested_tuple = (1, [2, 3], 4)  # A tuple containing an integer, a list, and another integer
nested_tuple[1][0] = "changed"  # Modifies the first element of the list at index 1 of `nested_tuple`
print(nested_tuple)  # Output: (1, ['changed', 3], 4) - the list within the tuple is mutable

# Concatenating two tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2  # Combines `tuple1` and `tuple2` into a new tuple (1, 2, 3, 4)

# Repeating elements in a tuple
repeated = tuple1 * 3  # Repeats the elements of `tuple1` three times, creating (1, 2, 1, 2, 1, 2)

# Tuple unpacking
point = (3, 5)
x, y = point  # Unpacks the values in `point` into variables `x` and `y`
print(x)  # Output: 3
print(y)  # Output: 5

# Function returning a tuple and unpacking the result
def get_coordinates():
    return 10, 20  # Returns a tuple (10, 20)

x, y = get_coordinates()  # Unpacks the returned tuple into `x` and `y`

# Accessing elements in a nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))  # A tuple of tuples
print(nested_tuple[1][1])  # Output: 4 - accesses the second element of the second tuple

# Using tuples as dictionary keys
locations = {
    (40.7128, -74.0060): "New York",  # A tuple representing New York's coordinates as a key
    (34.0522, -118.2437): "Los Angeles"  # A tuple representing Los Angeles's coordinates as a key
}

# Tuple methods: count and index
numbers = (1, 2, 3, 2, 4)  # A tuple containing integers with some duplicates
print(numbers.count(2))  # Output: 2 - counts how many times the value 2 appears in the tuple
print(numbers.index(3))  # Output: 2 - finds the index of the first occurrence of 3 in the tuple

# Tuple vs. List comparison table
# Tuple         vs                            List
# Feature	    Tuple	                      List
# Syntax	    () or comma-separated items   [] for list
# Mutability	Immutable	                    Mutable - can be changed
# Methods	    Limited (count, index)	      Many methods (append, pop, remove, etc.)
# Usage	        Used for fixed data, hashable requirement	Flexible, general-purpose collections
# Performance	Slightly faster than lists	  Slower due to the overhead of mutability
