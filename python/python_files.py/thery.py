"""
====================================================
PYTHON MASTER DEMO
Covers:
- Variables
- Data types
- Conditions
- Loops
- Functions
- Classes & Objects
- Modules concept
- Error handling
- File handling
- Real logic
====================================================
"""

# =========================
# GLOBAL VARIABLES
# =========================
APP_NAME = "Python Learning App"
VERSION = "1.0"


# =========================
# BASIC FUNCTION
# =========================
def welcome():
    """
    This function prints welcome message
    """
    print("Welcome to", APP_NAME)
    print("Version:", VERSION)


# =========================
# FUNCTION WITH PARAMETERS
# =========================
def add(a, b):
    """
    Adds two numbers
    """
    return a + b


def subtract(a, b):
    """
    Subtracts two numbers
    """
    return a - b


# =========================
# CONDITIONAL LOGIC
# =========================
def check_even_odd(num):
    """
    Checks if number is even or odd
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# =========================
# LOOP LOGIC
# =========================
def print_numbers(n):
    """
    Prints numbers from 1 to n
    """
    for i in range(1, n + 1):
        print(i)


def sum_numbers(n):
    """
    Returns sum of numbers from 1 to n
    """
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total


# =========================
# LIST OPERATIONS
# =========================
def process_list(items):
    """
    Processes a list
    """
    for item in items:
        print("Item:", item)


# =========================
# DICTIONARY OPERATIONS
# =========================
def show_student(student):
    """
    Prints dictionary values
    """
    for key, value in student.items():
        print(key, ":", value)


# =========================
# CLASS & OBJECT (OOP)
# =========================
class Student:
    """
    Student class
    """

    def __init__(self, name, age, sid):
        self.name = name
        self.age = age
        self.sid = sid

    def display(self):
        """
        Displays student details
        """
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.sid)

    def is_adult(self):
        """
        Checks if student is adult
        """
        return self.age >= 18


# =========================
# INHERITANCE
# =========================
class GraduateStudent(Student):
    """
    Child class inherits Student
    """

    def __init__(self, name, age, sid, degree):
        super().__init__(name, age, sid)
        self.degree = degree

    def display(self):
        super().display()
        print("Degree:", self.degree)


# =========================
# ERROR HANDLING
# =========================
def safe_division(a, b):
    """
    Handles division safely
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except Exception as e:
        return str(e)


# =========================
# FILE HANDLING
# =========================
def write_log(message):
    """
    Writes log to file
    """
    with open("app.log", "a") as file:
        file.write(message + "\n")


def read_log():
    """
    Reads log file
    """
    try:
        with open("app.log", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Log file not found")


# =========================
# MAIN EXECUTION (MODULE CONTROL)
# =========================
if __name__ == "__main__":

    # Welcome
    welcome()

    # Math operations
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))

    # Conditions
    print("7 is", check_even_odd(7))

    # Loops
    print_numbers(5)
    print("Sum:", sum_numbers(5))

    # List
    fruits = ["apple", "banana", "mango"]
    process_list(fruits)

    # Dictionary
    student_data = {
        "name": "Suresh",
        "age": 30,
        "id": 1
    }
    show_student(student_data)

    # OOP
    s1 = Student("Suresh", 30, 1)
    s1.display()
    print("Adult:", s1.is_adult())

    # Inheritance
    g1 = GraduateStudent("Ravi", 24, 2, "MCA")
    g1.display()

    # Error handling
    print("Division:", safe_division(10, 0))

    # File handling
    write_log("Application started")
    read_log()
