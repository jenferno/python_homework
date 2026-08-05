# Task 3: List Comprehensions Practice

import csv

# Read employees from CSV file
with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    employees = list(reader)


# Create list of employee full names
names = [
    employee[1] + " " + employee[2]
    for employee in employees
]

print(names)


# Create list of names containing the letter "e"
names_with_e = [
    name
    for name in names
    if "e" in name.lower()
]

print(names_with_e)