# Task 3
import csv

with open("../csv/employees.csv") as file:
    reader = csv.reader(file)
    employees = list(reader)

employee_names = [
    row[1] + " " + row[2]
    for row in employees[1:]
]

print(employee_names)

e_employee_names = [
    name
    for name in employee_names
    if "e" in name
]

print(e_employee_names)