'''
Models module for student representation. i.e. defines the Student class.
for identifying student and calculating average and grade.
it is for particular only one student.
'''

# Creates a class named Student to represent a student.

class Student:
    """
    Represents a student with marks and provides utility methods.
    """

    def __init__(self, name, marks):
        """
        Initialize student object.
        """
        self.name = name        # Student name
        self.marks = marks      # Dictionary of subject:marks

    def average(self):
        """
        Calculate average marks.
        :return: Average percentage
        """
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        """
        Calculate grade based on average.
        :return: Grade string
        """
        avg = self.average()
        if avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"
