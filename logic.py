import csv
from models import Student

FILE_NAME = "students.csv"

def load_students():
    students = {}
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                marks = {
                    "Maths": int(row["Maths"]),
                    "Science": int(row["Science"]),
                    "English": int(row["English"])
                }
                students[row["Name"]] = Student(row["Name"], marks)
    except FileNotFoundError:
        pass
    return students

def save_student(name, marks):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, marks["Maths"], marks["Science"], marks["English"]])

def class_average(students):
    return sum(s.average() for s in students.values()) / len(students)

def subject_average(students, subject):
    return sum(s.marks[subject] for s in students.values()) / len(students)

def topper(students):
    return max(students.values(), key=lambda s: s.average())

def weak_students(students):
    return [s.name for s in students.values() if s.average() < 40]

def result_summary(students):
    pass_count = sum(1 for s in students.values() if s.average() >= 40)
    fail_count = len(students) - pass_count
    return pass_count, fail_count
