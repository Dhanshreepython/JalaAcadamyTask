# 4. Define the local and Global variables with the same name and print both variables and
# understand the scope of the variables

# Local variable
def greet():
    # local variable
    message = 'Hello'
    print('Local', message)
greet()
# try to access message variable 
# outside greet() function
# print(message)
# Here, the message variable is local to the greet() function, so it can only be accessed within the function.
# That's why we get an error when we try to access it outside the greet() function.
# To fix this issue, we can make the variable named message global.

# -----------------------------------------------------------
# global  variable 
# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)

# This time we can access the message variable from outside of the greet() function. This is because we have created the message variable as the global variable.
# declare global variable
# message = 'Hello'
# Now, message will be accessible from any scope (region) of the program.