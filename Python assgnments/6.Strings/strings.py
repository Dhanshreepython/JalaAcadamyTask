# 1. Different ways creating a string

# create string type variables
name = "Python"
print(name)
message = "I love Python."
print(message)

# Access String Characters in Python
greet = 'hello'
print(greet[1])

greet = 'hello'
print(greet[-4]) 

# Python Strings are immutable
# message = 'Hola Amigos'
# message[0] = 'H'
# print(message)

message = 'Hola Amigos'
# assign new string to message variable
message = 'Hello Friends'
print(message); # prints "Hello Friends"

# multiline string 
message = """
Never gonna give you up
Never gonna let you down
"""

print(message)


greet = 'Hello'

# iterating through greet string
for letter in greet:
    print(letter)



# 2. Concatenating two strings using + operator
p1='I'
p2='love'
p3='python'
p4=p1+ " "+p2+" "+ p3
print(p4)


# 3. Finding the length of the  string
counter = 0
for c in "python": # traverse the string python
    counter+=1 #increment the counter
print (counter) 


# 4. Extract a string using Substring(slicing)

text = 'Python is easy to learn and use.'
substring = text[9:23]
print(substring) 


# 5.Searching in strings using index()
string = 'random'
print("index of 'and' in string:", string.index('and'))



# 7. Comparing strings

fruit1 = input('Enter the name of the first fruit:\n')
fruit2 = input('Enter the name of the second fruit:\n')

if fruit1 < fruit2:
    print(fruit1 + " comes before " + fruit2 + " in the dictionary.")
elif fruit1 > fruit2:
    print(fruit1 + " comes after " + fruit2 + " in the dictionary.")
else:
    print(fruit1 + " and " + fruit2 + " are the same.")

# 8. startsWith(), endsWith() and compareTo()
text = "Welcome to pythonhint"

print("Output-1:", text.startswith('Welcome'))
print("Output-2:", text.startswith('python', 10, 16))



# 9. Trimming strings with strip()
phrase = "Hello world?"
stripped_phrase = phrase.strip("Hed?")
print(stripped_phrase)


# 10. Replacing characters in strings with replace()
string = "Bubblegum"

# replacing the 'b' character with 'B'
changed_string = string.replace("b", "B")

print("Original string: ", string)
print("New string: ", changed_string)



# 11. Splitting strings with split()
txt = "welcome to the jungle"
x = txt.split()
print(x)


# 12. Converting integer objects to Strings

integer_year = 2019
string_year = str(2019)
print("This is " + string_year + ".")
print(str())

# 13. Converting to uppercase and lowercase
# Checking for lowercase characters
string = 'GEEKSFORGEEKS'
print(string.lower())

string = 'GeeksforGeeks'
print(string.upper())



