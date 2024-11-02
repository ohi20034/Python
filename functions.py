# Function definition syntax
# def function_name(parameters):
#     # Code block
#     return value  # Optional

# Function to add two numbers
def add_numbers(a, b):
    return a + b  # Returns the sum of a and b

# Calling the function with arguments 5 and 3
result = add_numbers(5, 3)
print(result)  # Output: 8

# Function to greet a user
def greet(name):
    return f"Hello, {name}!"  # Returns a greeting string with the provided name

# Calling the greet function with "Alice"
print(greet("Alice"))  # Output: Hello, Alice!

# Function with a default parameter
def greet(name="Guest"):
    return f"hello, {name}"  # Returns a greeting; defaults to "Guest" if no name is provided

# Calling the greet function without arguments
print(greet())  # Output: hello, Guest
# Calling the greet function with "Bob"
print(greet("Bob"))  # Output: hello, Bob

# Function with default parameter value
def describe_pet(pet_name, animal_type="hamster"):
    return f"I have a {animal_type} named {pet_name}."  # Describes a pet with a default animal type

# Calling the function with a pet name
print(describe_pet(pet_name="Harry"))  # Output: I have a hamster named Harry.


# Function to calculate the sum of any number of arguments
def calculate_sum(*args):  # *args allows passing a variable number of arguments
    return sum(args)  # Returns the sum of all arguments

# Calling the function with four arguments
print(calculate_sum(1, 2, 3, 4))  # Output: 10


# Function to print key-value pairs
def print_info(**kwargs):  # **kwargs allows passing a variable number of keyword arguments
    for key, value in kwargs.items():  # Iterate over the dictionary of key-value pairs
        print(f"{key}: {value}")  # Print each key-value pair

# Calling the function with named arguments
print_info(name="Alice", age=30)  
# Output:
# name: Alice
# age: 30

# Function to return a tuple of coordinates
def get_coordinates():
    return (10, 20)  # Returns a tuple

# Unpacking the returned tuple into x and y
x, y = get_coordinates()
print(x, y)  # Output: 10 20


# Function to multiply two numbers
def multiply(a, b):
    """Multiply two numbers and return the result."""  # Function documentation string
    return a * b  # Returns the product of a and b

# Printing the documentation of the multiply function
print(multiply.__doc__)  # Output: Multiply two numbers and return the result.


# Global variable x
x = 10  # Global variable

# Function that modifies the global variable
def my_function():
    global x  # Declare x as global to modify it
    x += 5  # Increments the global variable x by 5

# Calling the function to modify x
my_function()
print(x)  # Output: 15


# Lambda function to add two numbers
add = lambda a, b: a + b  # Defines a lambda function that adds a and b
print(add(2, 3))  # Output: 5

# Lambda function used for sorting a list of points
points = [(1, 2), (3, 1), (5, 0)]  # List of tuples
# Sorting the list of points by the second element of each tuple (y-coordinate)
points_sorted = sorted(points, key=lambda point: point[1])  
print(points_sorted)  # Output: [(5, 0), (3, 1), (1, 2)]


# Function that applies a given function to a value
def apply_function(func, value):
    return func(value)  # Calls the passed function with the given value

# Calling apply_function with a lambda that squares its input
print(apply_function(lambda x: x ** 2, 5))  # Output: 25
