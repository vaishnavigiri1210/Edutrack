'''
    models.py contains a Student class that represents a student with methods to calculate
    average marks and determine the grade based on those marks.
    it represent a one student entity means calculate only one student data
'''


class Student:                  # Student class to represent a student
    def __init__(self, name, marks):        # Initialize with name and marks
        self.name = name           # Student's name
        self.marks = marks      # Dictionary of subject marks

    def average(self):            # Calculate average marks
        return sum(self.marks.values()) / len(self.marks)       # Return average

    def grade(self):        # Determine grade based on average marks
        avg = self.average()    # Get average marks
        if avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"
