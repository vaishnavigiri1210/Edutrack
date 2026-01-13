import csv
from models import Student

FILE = "students.csv"

def load_students():
    students = {}
    try:
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            for r in reader:
                marks = {k: int(r[k]) for k in ["Maths", "Science", "English"]}
                students[r["Name"]] = Student(r["Name"], marks)
    except:
        pass
    return students

def save_student(name, marks):
    try:
        open(FILE, "r")
        file_exists = True
    except:
        file_exists = False

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Maths", "Science", "English"])
        writer.writerow([name, marks["Maths"], marks["Science"], marks["English"]])

def subject_average(students, subject):
    return sum(s.marks[subject] for s in students.values()) / len(students)

def result_summary(students):
    pass_count = sum(1 for s in students.values() if s.average() >= 40)
    fail_count = len(students) - pass_count
    return pass_count, fail_count
