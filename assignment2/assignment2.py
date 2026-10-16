# Task 2
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
