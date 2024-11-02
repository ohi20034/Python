# Defining a dictionary with keys and values
person = {"name": "Alice", "age": 25, "city": "New York"}  # A dictionary representing a person with name, age, and city

# Alternative way to create a dictionary
person = dict(name="Alice", age=25, city="New York")  # Another way to define the same dictionary using `dict()`

# Accessing values by key
print(person["name"])  # Output: "Alice" - Accesses the value associated with the key "name"

# Using `get()` method to access values
print(person.get("name"))      # Output: "Alice" - Safely gets the value for "name"
print(person.get("country"))   # Output: None - Returns None because "country" key does not exist
print(person.get("country", "Not Found"))  # Output: "Not Found" - Returns "Not Found" if the key is missing

# Modifying and adding key-value pairs
person["age"] = 30            # Changes the value for the "age" key to 30
person["country"] = "USA"     # Adds a new key "country" with value "USA" to the dictionary

# Removing elements from a dictionary
age = person.pop("age")  # Removes the "age" key from the dictionary and returns its value (30)

# Removing the last inserted key-value pair (for Python 3.7+)
last_item = person.popitem()  # Removes and returns the last key-value pair as a tuple

# Deleting specific keys or the entire dictionary
del person["city"]    # Deletes the "city" key from the dictionary
del person            # Deletes the entire dictionary `person`

# Clearing all items in a dictionary
person.clear()        # Empties the dictionary, removing all key-value pairs

# Getting the number of items in the dictionary
print(len(person))  # Output: 2 - Prints the number of key-value pairs in `person`

# Checking if a key is in the dictionary
print("name" in person)  # Output: True - Checks if "name" key exists in the dictionary

# Iterating over dictionary keys
for key in person:
    print(key, person[key])  # Prints each key and its associated value

# Iterating over dictionary values
for value in person.values():
    print(value)  # Prints each value in the dictionary

# Iterating over dictionary keys and values
for key, value in person.items():
    print(key, value)  # Prints each key-value pair in the dictionary

# Dictionary comprehension to create a dictionary of squares
squared_numbers = {x: x**2 for x in range(5)}  # Creates a dictionary of squares {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Accessing dictionary keys, values, and items as views
print(person.keys())     # Returns a view of all keys in `person`
print(person.values())   # Returns a view of all values in `person`
print(person.items())    # Returns a view of all key-value pairs as tuples

# Updating a dictionary with new key-value pairs
person.update({"city": "Boston"})  # Updates the dictionary with key "city" set to "Boston" (overwrites if "city" exists)

# Nested dictionaries
company = {
    "employee_1": {"name": "Alice", "age": 25},
    "employee_2": {"name": "Bob", "age": 30}
}
print(company["employee_1"]["name"])  # Output: "Alice" - Accesses the "name" of "employee_1" in the nested dictionary

# Using `defaultdict` from `collections` for automatic default values
from collections import defaultdict

# Creates a defaultdict with default type `int` (default value is 0)
counts = defaultdict(int)
counts["apple"] += 1  # Adds "apple" key with value 1 (if "apple" was missing, it would initialize with 0 and then add 1)

# Using `Counter` from `collections` to count occurrences
from collections import Counter

# Creates a Counter object to count occurrences in a list
word_count = Counter(["apple", "banana", "apple", "orange", "banana"])
print(word_count)  # Output: Counter({'apple': 2, 'banana': 2, 'orange': 1}) - Counts the occurrences of each element
