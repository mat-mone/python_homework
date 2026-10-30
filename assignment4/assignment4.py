# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

import pandas as pd

data = {
    "Name" : ['Alice', 'Bob', 'Charlie'],
    "Age" : [25, 30, 35],
    "City" : ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]

print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older["Age"] += 1

print(task1_older)

task1_older.to_csv("employees.csv", index=False)


# Task 2: Loading Data from CSV and JSON

    # read csv
task2_employees = pd.read_csv("employees.csv")

print(task2_employees)

    # new employee data
add_data = {
    "Name" : ['Eve', 'Frank'],
    "Age" : [28, 40],
    "City" : ['Miami', 'Seattle'],
    "Salary" : [60000, 95000]
}

    #convert data to df
add_data_df = pd.DataFrame(add_data)

    # save df to json file
add_data_df.to_json("additional_employees.json", orient="records")

    # read json
json_employees = pd.read_json("additional_employees.json")

print(json_employees)

    # combine data
more_employees = pd.concat(
    [task2_employees, json_employees],
    ignore_index=True
)

print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
first_three = more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape = more_employees.shape
print(employee_shape)

more_employees.info()

# Task 4: Data Cleaning
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)

    # create copy
clean_data = dirty_data.copy()

    # remove duplicates
clean_data = clean_data.drop_duplicates()

    # convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")

print(clean_data)

    # Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)

clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")

print(clean_data)

    # Fill missing numeric values (use fillna). Fill Age with the mean and Salary with the median
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())

clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())

print(clean_data)

    # Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format="mixed")

print(clean_data)

    # Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()

clean_data["Department"] = clean_data["Department"].str.strip().str.upper()

print(clean_data)