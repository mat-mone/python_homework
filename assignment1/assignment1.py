# Task 1: write a hello function that returns Hello!
def hello():
    return "Hello!"

print(hello())
print("=====task 1 completed=====")

# Task 2: write a greet function using a formatted string
def greet(name):
    return (f"Hello, {name}!")

print(greet("Femi"))
print("=====task 2 completed=====")

# Task 3: write a calc function
def calc(a, b, arithmetic_operator = "multiply"):

    try:
        match arithmetic_operator:
            case "add":
                return (a + b)
            case "subtract":
                return (a - b)
            case "multiply":
                return (a * b)
            case "divide":
                return (a / b)
            case "modulo":
                return (a % b)
            case "int_divide":
                return (a // b)
            case "power":
                return (a ** b)
            case _:
                return "invalid operation"
            
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

# Task 4: Data Type Conversion
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)

    except ValueError:
        return f"You can't convert {value} into a {data_type}."

# Task 5: grading system using *args
def grade (*args):
    try:
        avg = sum(args) / len(args)

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    except Exception:
        return "Invalid data was provided."   

# Task 6: create repeat function using a for loop with a range
def repeat(string, count):
    result = ""
    for i in range(count):
         result += string
    return result