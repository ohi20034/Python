# Define a class named Dog
class Dog:
    # Class attribute: species that is shared by all instances of Dog
    species = "Canis familiaris"  # This is a constant value representing the species of the dog

    # Constructor method to initialize instance attributes
    def __init__(self, name, age):  # Takes two parameters: name and age
        self.name = name  # Instance attribute: name of the dog, unique for each instance
        self.age = age    # Instance attribute: age of the dog, unique for each instance

    # Method for the dog to bark
    def bark(self):  # This method does not take additional parameters
        return f"{self.name} says woof!"  # Returns a string indicating the dog is barking

    # Method to get the age of the dog
    def get_age(self):  # This method does not take additional parameters
        return f"{self.name} is {self.age} years old."  # Returns a string indicating the dog's age

# Creating instances (objects) of the Dog class
dog1 = Dog("Buddy", 3)  # dog1 is an instance of Dog with name 'Buddy' and age 3
dog2 = Dog("Max", 5)    # dog2 is another instance of Dog with name 'Max' and age 5

# Accessing and printing the name attribute of dog1
print(dog1.name)  # Output: Buddy (prints the name of dog1)
# Accessing and printing the age attribute of dog2
print(dog2.age)   # Output: 5 (prints the age of dog2)

# Calling the bark method for dog1 and printing the result
print(dog1.bark())  # Output: Buddy says woof! (prints the barking message for dog1)
# Calling the get_age method for dog2 and printing the result
print(dog2.get_age())  # Output: Max is 5 years old. (prints the age message for dog2)

print("**************")  # Print a separator line for clarity in output

# Inheritance example: Define a class named Puppy that inherits from Dog
class Puppy(Dog):  # Puppy is a subclass of Dog, inheriting its attributes and methods
    # Constructor method for Puppy
    def __init__(self, name, age, training_level):  # Takes parameters: name, age, and training_level
        super().__init__(name, age)  # Call the constructor of the parent class (Dog) to initialize name and age
        self.training_level = training_level  # Instance attribute specific to Puppy: training level

    # Method to indicate the training level of the puppy
    def train(self):  # This method does not take additional parameters
        return f"{self.name} is at training level {self.training_level}."  # Returns training level message

# Creating an instance of Puppy
puppy1 = Puppy("Charlie", 1, "Beginner")  # puppy1 is an instance of Puppy with name 'Charlie', age 1, and training level 'Beginner'

# Calling the bark method for puppy1 and printing the result
print(puppy1.bark())  # Output: Charlie says woof! (prints the barking message for puppy1)
# Calling the train method for puppy1 and printing the result
print(puppy1.train())  # Output: Charlie is at training level Beginner. (prints training level message for puppy1)

# Encapsulation example: Define a class named Cat
class Cat:
    # Constructor method to initialize instance attributes
    def __init__(self, name, age):  # Takes parameters: name and age
        self.__name = name  # Private instance attribute: name of the cat (cannot be accessed directly outside this class)
        self.age = age  # Instance attribute: age of the cat, accessible outside the class

    # Method for the cat to meow
    def meow(self):  # This method does not take additional parameters
        return f"{self.__name} says meow!"  # Returns a string indicating the cat is meowing

# Creating an instance of Cat
cat1 = Cat("Whiskers", 2)  # cat1 is an instance of Cat with name 'Whiskers' and age 2
# Attempt to access the private attribute (commented out)
# print(cat1.__name)  # This will raise an AttributeError (uncommenting will show the error)
# Calling the meow method for cat1 and printing the result
print(cat1.meow())  # Output: Whiskers says meow! (prints the meowing message for cat1)

# Polymorphism example: Define a base class named Animal
class Animal:
    def sound(self):  # Method that will be overridden in subclasses
        pass  # This is a placeholder method, does nothing

# Define a subclass Cat that inherits from Animal
class Cat(Animal):
    def sound(self):  # Overriding the sound method
        return "Meow!"  # Returns the sound made by the cat

# Define a subclass Dog that inherits from Animal
class Dog(Animal):
    def sound(self):  # Overriding the sound method
        return "Woof!"  # Returns the sound made by the dog

# Function to demonstrate polymorphism
def make_sound(animal):  # Takes an instance of Animal (or its subclasses) as a parameter
    print(animal.sound())  # Calls the sound method of the passed animal and prints the result

# Creating instances of Cat and Dog
cat = Cat()  # cat is an instance of Cat
dog = Dog()  # dog is an instance of Dog

# Calling make_sound with the cat instance
make_sound(cat)  # Output: Meow! (prints the sound made by the cat)
# Calling make_sound with the dog instance
make_sound(dog)  # Output: Woof! (prints the sound made by the dog)
