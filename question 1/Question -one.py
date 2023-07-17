#  created a function to read student registration number and name then store in a dictionary

# Initialize an empty dictionary
students = {}

# Read student details and store them in the dictionary
while True:
    reg_no = input("Enter registration number (or 'end' to stop): ")
    if reg_no == "end":
        break
    name = input("Enter name: ")
    students[reg_no] = name

# Display the registration numbers
print("Registration numbers:")
for reg_no in students:
    print(reg_no)

# Display the names of students
print("Names of students:")
for reg_no, name in students.items():
    print(name)