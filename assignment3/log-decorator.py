## Task 1 : Writing and Test a Decorator

import logging

#logging Setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


#Decorator
def logger_decorator(func):

    def wrapper(*args, **kwargs):

        # Call the original function
        result = func(*args, **kwargs)

        # Function name
        logger.info(f"function: {func.__name__}")

        # Positional parameters
        if args:
            logger.info(f"positional parameters: {args}")
        else:
            logger.info("positional parameters: none")

        # Keyword parameters
        if kwargs:
            logger.info(f"keyword parameters: {kwargs}")
        else:
            logger.info("keyword parameters: none")

        # Return value
        logger.info(f"return: {result}")
        logger.info("---------------------------")

        return result

    return wrapper


# Function 1 
@logger_decorator
def hello():
    print("Hello, World!")


# Function 2
@logger_decorator
def numbers(*args):
    print(args)
    return True


# Function 3
@logger_decorator
def keywords(**kwargs):
    print(kwargs)
    return logger_decorator


# Main Program 
hello()
numbers(10, 20, 30)
keywords(name="Jennifer", course="Python", lesson=3)