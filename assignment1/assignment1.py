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

print("=====task 3 completed=====")

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

print("=====task 4 completed=====")

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

print("=====task 5 completed=====")

# Task 6: create repeat function using a for loop with a range
def repeat(string, count):
    result = ""
    for i in range(count):
         result += string
    return result

print("=====task 6 completed=====")

# Task 7: student scores using **kwargs
def student_scores(metric, **kwargs):
    if metric == "mean":
        avg = sum(kwargs.values()) / len(kwargs.values())
        return avg
    
    elif metric == "best":
        top_score = 0
        top_student = ""

        for student_name, score in kwargs.items():
            if score > top_score:
                top_score = score
                top_student = student_name
        return top_student

print("=====task 7 completed=====")

# Task 8: titleize, with string and list operations
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    new_string = []

    for i, word in enumerate(words):
        lowercase_word = word.lower()

        if i == 0 or i == len(words) - 1:
            new_string.append(word.capitalize())

        elif lowercase_word in little_words:
            new_string.append(lowercase_word)

        else:
            new_string.append(word.capitalize())
    return " ".join(new_string)

print("=====task 8 completed=====")

# Task 9: Hangman, with more string operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

print("=====task 9 completed=====")

# Task 10: Pig Latin, another string manipulation exercise
def pig_latin(string):
    vowels = "aeiou"
    words = string.split()
    new_words = []

    for word in words:

        if word[0] in vowels:
            new_words.append(word + "ay")

        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    if letter == "u" and i > 0 and word[i - 1] == "q":
                        rearranged_word = word[i + 1:] + word[:i + 1] + "ay"
                    else:
                        rearranged_word = word[i:] + word[:i] + "ay"

                    new_words.append(rearranged_word)

                    break

    return " ".join(new_words)

print("=====task 10 completed=====")