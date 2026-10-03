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

