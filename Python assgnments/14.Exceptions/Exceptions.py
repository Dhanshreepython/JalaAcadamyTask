# 1. Write a program to generate Arithmetic Exception without exception handling# Perform division by zero to generate Arithmetic Exception
result = 10 / 0

# the unhandled exception
print("Result:", result)


# 2. Handle the Arithmetic exception using try-catch block

try:
    result = 10 / 0
    print("Result:", result) 

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")





# 3. Write a method which throws exception, Call that method in main class without try block
def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero")
    return a / b

#  method without a try block
result = divide_numbers(10, 0)
print("Result:", result)  



# 4. Write a program with multiple catch blocks

try:
    # Code that may raise exceptions
    a = 10 / 0
    b = int("abc")
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid conversion to integer")
except Exception as e:
    print("Error:", str(e))



# 5. Write a program to throw exception with your own message

# raise Exception("This is my custom exception message")


# 6. Write a program to create your own exception

try:
    # Code that may raise an exception
    print("Try block")
except Exception:
    print("Exception occurred")
finally:
    print("Finally block")



# 8. Write a program to generate Arithmetic Exception
try:
    result = 10 / 0
    print("Result:", result)  # This line won't be executed if an exception occurs
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


# 9. Write a program to generate FileNotFoundException

try:
    file = open("nonexistent_file.txt", "r")
    file.close()
except FileNotFoundError:
    print("Error: File not found")


# 10. Write a program to generate ClassNotFoundException

class ClassNotFoundException(Exception):
    pass

# Example usage
class_name = "NonexistentClass"

try:
    raise ClassNotFoundException(f"Class not found: {class_name}")
except ClassNotFoundException as e:
    print("Error:", str(e))




# 11. Write a program to generate IOException
try:
    file = open("file.txt", "r")
    #Operations on the file
    file.close()
except IOError:
    print("Error: I/O operation failed")


# 12. Write a program to generate NoSuchFieldException
class MyClass:
    def __init__(self):
        self.field = 10

try:
    obj = MyClass()
    value = obj.nonexistent_field
except AttributeError:
    print("Error: Field not found")
