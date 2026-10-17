# Task 2: read a csv file
import csv
import traceback

def read_employees():
    employees = {}
    rows = []

    try:
        with open("../csv/employees.csv") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    employees["fields"] = row
                else:
                    rows.append(row)
        employees["rows"] = rows
        return employees
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()
print(employees)

# Task 3: find column index
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4: find employee first name
def first_name(row_number):
    first_name_column = column_index("first_name")

    employee_row = employees["rows"][row_number]

    first_name_value = employee_row[first_name_column]

    return first_name_value

# Task 5: find the employee; a function in a function
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: find the employee with a lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# Task 7: sort the rows by last name using a lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")

    employees["rows"].sort(
        key=lambda row: row[last_name_column]
    )

    return employees["rows"]

sort_by_last_name()
print(employees)

# Task 8: create a dict for an employee
def employee_dict(row):
    employee_info = {}

    for i, field in enumerate(employees["fields"]):
        if i == 0:
            continue
        else:
            employee_info[field] = row[i]

    return employee_info

employee_row = employees["rows"][0]
print(employee_dict(employee_row))

