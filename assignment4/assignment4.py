# Task 1 : Introduction to Pandas - Creating and Manipulating DataFrames
# Test 1
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)

print(task1_data_frame)

# Test 2
task1_with_salary = task1_data_frame.copy()

task1_with_salary["Salary"] = [70000, 80000, 90000]

print(task1_with_salary)

# Test 3
task1_older = task1_with_salary.copy()

task1_older["Age"] = task1_older["Age"] + 1

print(task1_older)

# Test 4
task1_older.to_csv("employees.csv", index=False)

# Task 2 : Loading Data from CSV and JSON
# Test 1
task2_employees = pd.read_csv("employees.csv")

print(task2_employees)

# Test 2
json_employees = pd.read_json("additional_employees.json")

print(json_employees)

# Test 3
more_employees = pd.concat(
    [task2_employees, json_employees],
    ignore_index=True
)

print(more_employees)

# Task 3 : Data Inspection - Using Head, Tail, and Info Methods
# Test 1
first_three = more_employees.head(3)

print(first_three)

# Test 2
last_two = more_employees.tail(2)

print(last_two)

# Test 3

employee_shape = more_employees.shape

print(employee_shape)

more_employees.info()


# Task 4 : Data cleaning
# Test 4
dirty_data = pd.read_csv("dirty_data.csv")

print(dirty_data)

# Test 5
clean_data = dirty_data.copy()

clean_data = clean_data.drop_duplicates()

print(clean_data)

# Test 6
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")

print(clean_data)

# Salary Conversion
# Test 7
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")

print(clean_data)

# Test 8
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())

clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())

print(clean_data)

# Test 9
clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"],
    format="mixed",
    errors="coerce"
)

print(clean_data)

# Test 10
clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Name"] = clean_data["Name"].str.upper()
clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Department"] = clean_data["Department"].str.upper()

print(clean_data)