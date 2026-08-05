# Task 1 : Writing and Testing a Decorator

import logging

# ---------------------------
# Logging Setup
# ---------------------------
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


# ---------------------------
# Decorator
# ---------------------------
def logger_decorator(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
    
        log_message = (
            f"function: {func.__name__}, "
            f"positional parameters: {list(args) if args else 'none'}, "
            f"keyword parameters: {kwargs if kwargs else 'none'}, "
            f"return: {result}"
        )

        logger.info(log_message)

        return result

    return wrapper


# ---------------------------
# Function 1: No parameters, no return value
# ---------------------------
@logger_decorator
def hello():
    print("Hello, World!")


# ---------------------------
# Function 2: Variable positional arguments
# ---------------------------
@logger_decorator
def numbers(*args):
    print(args)
    return True


# ---------------------------
# Function 3: Variable keyword arguments
# ---------------------------
@logger_decorator
def keywords(**kwargs):
    print(kwargs)
    return logger_decorator


# ---------------------------
# Main Program
# ---------------------------
hello()
numbers(10, 20, 30)
keywords(name="Jennifer", course="Python", lesson=3)