# Task 1 : Hello

def hello ():
    return "Hello!"

print (hello())

# Task 2 : Greet with a Formatted String

def greet (name):
    return f"Hello, {name}!"

print(greet("Jennifer"))

# Task 3 : Calculator

def calc(x, y, operation= "multiply"):
    try:
        if operation == "add":
            return x + y
        elif operation == "subtract":
            return x - y
        elif operation == "multiply":
            return x * y
        elif operation == "divide":
            return x / y
        elif operation == "modulo":
            return x % y
        elif operation == "int_divide":
            return x // y
        elif operation == "power":
            return x ** y
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
print (calc(24,8))
print (calc(24,8, "add"))
print (calc(24,8, "subtract"))
print (calc(24,8, "multiply"))
print (calc(24,8, "divide"))
print (calc(24,8, "modulo"))
print (calc(24,8, "int_divide"))
print (calc(24,8, "power"))

# Task 4 : Data Type Conversion

def data_type_conversion (value, data_type):
    try:
        if data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        elif data_type == "int":
            return int(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    
print (data_type_conversion("8.88", "float"))
print (data_type_conversion(888, "str"))
print (data_type_conversion("888", "int"))
print (data_type_conversion("nonsense", "float"))

# Task 5 : Grading System, Using *args

def grade (*args):
    try:
        total = sum(args)
        grade_count = len(args)
        average = total / grade_count

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else :
            return "F"
    except TypeError:
        return "Invalid data was provided."
    
print (grade (98, 96, 92))
print (grade (88, 86, 82))
print (grade (78, 76, 72))
print (grade (68, 66, 62))
print (grade ( 58, 56, 52))
print (grade (89, "A", 95))

# Task 6 : Use a For Loop with a Range

def repeat (string, count):
    new_string = ""

    for i in range(count):
        new_string = new_string + string

    return new_string

print (repeat("Happy", 4))

# Task 7 : Student Scores, Using **kwargs

def student_scores(option, **kwargs):
    if option == "best":
        if len(kwargs) == 0:
            return None

        students = list(kwargs.items())
        best_student, highest_score = students[0]

        for student, score in students[1:]:
            if score > highest_score:
                highest_score = score
                best_student = student

        return best_student

    elif option == "mean":
        if len(kwargs) == 0:
            return 0

        total_score = 0

        for score in kwargs.values():
            total_score = total_score + score

        average = total_score / len(kwargs)

        return average


print(student_scores("best", Jennifer=98, Alex=88, Sarah=92))
print(student_scores("mean", Jennifer=98, Alex=88, Sarah=92))

# Task 8 : Titleize, with String and List Operations

def titleize (book_title):
    little_words = ["a","on","an","the","of","and","is","in"]

    words = book_title.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word in little_words:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()
    return " ".join(words)

print(titleize("the giver"))
print(titleize("how to kill a mockingbird"))

# Task 9 : Hangman, with more String Operations

def hangman (secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result = result + letter
        else: 
            result = result + "_"
    return result

print(hangman("pineapple", "pe"))
print(hangman("saxophone", "ap"))

# Task 10 : Pig Latin, Another String Manipulation Exercise

def pig_latin(english):
    vowels = "aeiou"
    words = english.split()
    new_words = []

    for word in words:
        if word[0] in vowels:
            new_word = word + "ay"
        else: 
            index = 0
            while index < len(word) and word[index] not in vowels:
                if word [index:index + 2] == "qu":
                    index = index + 2
                    break
                index = index + 1
            new_word = word[index:] + word[:index] + "ay"
        new_words.append(new_word)
    return " ".join(new_words)

print(pig_latin("apple"))
print(pig_latin("watermelon"))
print(pig_latin("strong"))
# %%
