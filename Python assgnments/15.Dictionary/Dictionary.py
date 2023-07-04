# 1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name 
# 1.1. Adding the values in dictionary
# 1.2. Updating the values in dictionary
# 1.3. Accessing the value in dictionary
# 1.4. Create a nested loop dictionary
# 1.5. Access the values of nested loop dictionary 1.6. Print the keys present in a particular dictionary 1.7. Delete a value from a dictionary


# 1. Create a Dictionary with at least 5 key-value pairs of the Student ID and Name
student_dict = {
    101: "Pankaj",
    102: "Manali",
    103: "shilpa",
    104: "Krishana",
    105: "Radha"
}

# 1.1. Adding values to the dictionary
student_dict[106] = "Gaytri"
student_dict[107] = "Mohan"

# 1.2. Updating values in the dictionary
student_dict[103] = "Manu"  # Updated 

# 1.3. Accessing the value in the dictionary
print("Student with ID 104:", student_dict[104])

# 1.4. Create a nested loop dictionary
marks_dict = {
    101: {"Math": 85, "Science": 92, "English": 78},
    102: {"Math": 90, "Science": 88, "English": 92},
    103: {"Math": 75, "Science": 80, "English": 85}
}

# 1.5. Access the values of the nested loop dictionary
for student_id, marks in marks_dict.items():
    print("Student ID:", student_id)
    for subject, score in marks.items():
        print(subject, ":", score)
    print()

# 1.6. Print the keys present in a particular dictionary
print("Keys in student_dict:", student_dict.keys())

# 1.7. Delete a value from a dictionary
del student_dict[105]  # Removing Mike from the dictionary

# Print the updated dictionary
print("Updated student_dict:", student_dict)
