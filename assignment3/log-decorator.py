import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {args or 'none'}")
        logger.info(f"keyword parameters: {kwargs or 'none'}")
        logger.info(f"return: {result}")

        return result
    return wrapper


@logger_decorator
def hello():
    print("Hello, World!")

@logger_decorator
def return_true(*args):
    return True

@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator


hello()
return_true("Tuesday", "Thursday", 2)
return_decorator(name = "Super Mario", age = "Unknown", gender = "Male")