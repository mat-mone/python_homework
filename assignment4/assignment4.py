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