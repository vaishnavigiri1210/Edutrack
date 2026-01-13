'''
Logic module for managing student data and performing calculations like
average marks and result summaries
'''

import csv          # for handling CSV file operations
from models import Student      # importing the Student class from models module

FILE = "students.csv"       # defining the file name for storing student data

def load_students():        # function to load student data from the CSV file
    students = {}       # initializing an empty dictionary to store student objects
    try:
        with open(FILE, "r") as f:      # opening the CSV file in read mode
            reader = csv.DictReader(f)  # creating a CSV dictionary reader
            for r in reader:        # iterating through each row in the CSV file
                marks = {k: int(r[k]) for k in ["Maths", "Science", "English"]} # extracting marks and converting them to integers
                students[r["Name"]] = Student(r["Name"], marks)     # creating a Student object and adding it to the dictionary
    except:
        pass    # handling exceptions (e.g., file not found) by doing nothing
    return students     # returning the dictionary of student objects

def save_student(name, marks):      # function to save a student's data to the CSV file
    try:
        open(FILE, "r")     # checking if the file exists by trying to open it in read mode
        file_exists = True  # setting the flag to True if the file exists
    except:
        file_exists = False # setting the flag to False if the file does not exist

    with open(FILE, "a", newline="") as f:   # opening the CSV file in append mode
        writer = csv.writer(f)   # creating a CSV writer object for writing data
        if not file_exists:     # if the file does not exist, write the header row
            writer.writerow(["Name", "Maths", "Science", "English"])    # writing the header row
        writer.writerow([name, marks["Maths"], marks["Science"], marks["English"]])  # writing the student's data

def subject_average(students, subject):   # function to calculate the average marks for a given subject
    return sum(s.marks[subject] for s in students.values()) / len(students)  # calculating and returning the average marks

def result_summary(students):   # function to summarize the number of students who passed and failed
    pass_count = sum(1 for s in students.values() if s.average() >= 40)  # counting the number of students who passed
    fail_count = len(students) - pass_count # calculating the number of students who failed
    return pass_count, fail_count   # returning the counts of passed and failed students
