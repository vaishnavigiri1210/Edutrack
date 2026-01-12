''' 
Logic module for EduTrack application 
(Backend i.e. handles data processing like calculate average, topper name, total students count) 
it is for all students in the class.
'''
 
import csv
from models import Student

FILE_NAME = "students.csv"

def load_students():
    """
    Load students data from CSV file.
    :return: Dictionary of student objects
    """
    students = {}       # Initialize empty dictionary to hold student objects
    try:
        with open(FILE_NAME, "r") as file:      # Open the CSV file in read mode
            reader = csv.DictReader(file)       # Create a CSV dictionary reader
            for row in reader:             # Iterate through each row in the CSV
                marks = {
                    "Maths": int(row["Maths"]),         # Convert marks to integer
                    "Science": int(row["Science"]),
                    "English": int(row["English"])
                }
                students[row["Name"]] = Student(row["Name"], marks)
    except FileNotFoundError:
        pass
    return students


def save_student(name, marks):
    """
    Save a student record to CSV.
    """
    with open(FILE_NAME, "a", newline="") as file:      # Open the CSV file in append mode
        writer = csv.writer(file)                 # Create a CSV writer beacause we are writing rows
        writer.writerow([name, marks["Maths"], marks["Science"], marks["English"]])     # Write student data as a new row


def class_average(students):
    """
    Calculate class average.
    """
    return sum(s.average() for s in students.values()) / len(students)      # sum of averages divided by number of students

def subject_average(students, subject):
    """
    Calculate average of a specific subject.
    """
    return sum(s.marks[subject] for s in students.values()) / len(students)


def topper(students):
    """
    Identify class topper.
    """
    return max(students.values(), key=lambda s: s.average())    # max function with key as average marks


def weak_students(students):
    """
    Identify students scoring below 40%.
    """
    return [s.name for s in students.values() if s.average() < 40]   # List comprehension to get names of weak students

def result_summary(students):
    """
    Calculate pass and fail count.
    """
    pass_count = sum(1 for s in students.values() if s.average() >= 40)
    fail_count = len(students) - pass_count
    return pass_count, fail_count
