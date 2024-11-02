# Defining a set with unique elements
fruits = {"apple", "banana", "cherry"}  # Creates a set of fruits; sets store only unique values

# Creating an empty set
empty_set = set()  # An empty set; `empty_set = {}` would create an empty dictionary, not a set

# Removing duplicate elements in set definition
numbers = {1, 2, 2, 3, 4}  # Sets automatically remove duplicates, resulting in {1, 2, 3, 4}

# Adding a single element to a set
fruits.add("orange")  # Adds "orange" to the set `fruits`

# Adding multiple elements to a set
fruits.update(["mango", "grapes"])  # Adds "mango" and "grapes" to the set (elements from a list)

# Removing an element from a set (raises error if element not found)
fruits.remove("banana")  # Removes "banana" from the set; raises a KeyError if "banana" is missing

# Removing an element from a set safely
fruits.discard("banana")  # Removes "banana" from the set; does nothing if "banana" is not present

# Removing a random element from a set
random_element = fruits.pop()  # Removes and returns an arbitrary element from the set

# Clearing all elements from a set
fruits.clear()  # Empties the set, removing all elements

# Set operations: Union, Intersection, Difference, Symmetric Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
union_set = set1 | set2  # Output: {1, 2, 3, 4, 5} - combines all unique elements from both sets
# Alternative syntax
union_set = set1.union(set2)  # Also creates the union of set1 and set2

# Intersection of two sets
intersection_set = set1 & set2  # Output: {3} - only elements common to both sets
# Alternative syntax
intersection_set = set1.intersection(set2)

# Difference of two sets
difference_set = set1 - set2  # Output: {1, 2} - elements in set1 but not in set2
# Alternative syntax
difference_set = set1.difference(set2)

# Symmetric difference of two sets
sym_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5} - elements in either set but not both
# Alternative syntax
sym_diff_set = set1.symmetric_difference(set2)

# Checking subset and superset relationships
print({1, 2}.issubset({1, 2, 3}))  # Output: True - checks if {1, 2} is a subset of {1, 2, 3}

print({1, 2, 3}.issuperset({1, 2}))  # Output: True - checks if {1, 2, 3} is a superset of {1, 2}

# Checking if two sets have no elements in common
print({1, 2}.isdisjoint({3, 4}))  # Output: True - returns True if {1, 2} and {3, 4} share no elements

# Creating an immutable set
frozen = frozenset([1, 2, 3])  # `frozenset` creates an immutable set that cannot be changed
# frozen.add(4)  # Raises an AttributeError, as `frozenset` does not support adding/removing elements

# Iterating over elements in a set
for fruit in fruits:
    print(fruit)  # Prints each element in the set `fruits`

# Removing duplicates from a list by converting it to a set
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = list(set(numbers))  # Converts to a set to remove duplicates, then back to a list; Output: [1, 2, 3, 4]

# Checking if an element is in a set
print("apple" in fruits)  # Output: True if "apple" is in `fruits`, otherwise False

# Summary of set methods:
# add(elem) - Adds an element to the set
# update(iterable) - Adds multiple elements from an iterable
# remove(elem) - Removes an element, raises error if element is not present
# discard(elem) - Removes an element, does nothing if element is not present
# pop() - Removes and returns an arbitrary element
# clear() - Removes all elements from the set
# union(set) - Returns a new set with all unique elements from both sets
# intersection(set) - Returns a new set with elements common to both sets
# difference(set) - Returns a new set with elements in the first set but not in the second
# symmetric_difference(set) - Returns a new set with elements in either of the sets but not both
# issubset(set) - Returns True if all elements of this set are in another
# issuperset(set) - Returns True if all elements of another set are in this set
# isdisjoint(set) - Returns True if two sets have no elements in common
