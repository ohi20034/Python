""" 
try:
    # Code that might raise an exception
    risky_code()
except SomeSpecificException:
    # Code to handle the exception
    handle_exception()
except AnotherException as e:
    # Handle a different exception and access the exception object
    print(f"An error occurred: {e}")
else:
    # This block runs if no exceptions are raised in the try block
    print("No exceptions occurred!")
finally:
    # This block runs no matter what (whether an exception occurred or not)
    print("This will always execute.")

"""



def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Inputs must be numbers.")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Execution of divide_numbers() completed.")

#atching Multiple Exceptions
try:
    # Some code that may raise multiple types of exceptions
    result = int(input("Enter a number: ")) / int(input("Enter another number: "))
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")


# Test the function
print(divide_numbers(10, 2))   # Output: 5.0
print(divide_numbers(10, 0))   # Output: Error: Cannot divide by zero.
print(divide_numbers(10, 'a')) # Output: Error: Inputs must be numbers.


