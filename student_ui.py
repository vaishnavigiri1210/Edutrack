'''
    student_ui.py contains the UI components for student login and dashboard using Tkinter.
    which interacts with the logic module to fetch and display student data.
'''


import tkinter as tk        # Tkinter for GUI components
from tkinter import messagebox  # For displaying message boxes
import logic        # Importing the logic module for student data handling

BG = "#f4f6f9"
PRIMARY = "#1f3c88"
LOGOUT = "#e53935"


def student_login(parent):      # Student Login Window
    win = tk.Toplevel(parent)   # Create a new top-level window
    win.title("Student Login")  # Set window title
    win.geometry("400x300")     # Set window size
    win.configure(bg=BG)    # Set background color

    tk.Label(
        win, text="Student Login",      # Title Label
        font=("Arial", 18, "bold"),     # font style
        bg=BG
    ).pack(pady=20)     # Add some vertical padding(between student login and name entry box)

    entry = tk.Entry(win, width=30)     # Entry box for student name
    entry.pack(pady=10)     # Add some vertical padding(between name entry box and login button)

    def verify():       # Verify student name and open dashboard
        students = logic.load_students()        # Load student data from logic module
        for s in students.values():     # Check if entered name matches any student
            if s.name.lower() == entry.get().lower():       # case-insensitive comparison i.e. VAISHU==vaishu
                win.destroy()           # Close login window
                student_dashboard(parent, s)        # Open student dashboard
                return      # Exit the function after successful login
        messagebox.showerror("Error", "Student Not Found")      # Show error if student not found

    tk.Button(
        win, text="Login",      # Login Button
        width=18, height=2,
        bg=PRIMARY, fg="white",
        font=("Arial", 12, "bold"),
        command=verify      # Call verify function on button click
    ).pack(pady=20)     # Add some vertical padding(between login button and bottom of the window)


def student_dashboard(parent, student):     # Student Dashboard Window
    dash = tk.Toplevel(parent)          # Create a new top-level window
    dash.title("Student Dashboard")     # Set window title
    dash.geometry("500x420")        # Set window size
    dash.configure(bg=BG)       # Set background color

    tk.Label(
        dash, text=f"Welcome, {student.name}",   # Welcome Label with student name
        font=("Arial", 20, "bold"),         # font style
        bg=BG                               # background color
    ).pack(pady=20)     # Add some vertical padding(between welcome label and marks section)

    for sub, mark in student.marks.items():    # Display each subject and its corresponding mark
        tk.Label(
            dash, text=f"{sub}: {mark}",   
            font=("Arial", 14),
            bg=BG
        ).pack(pady=3)      # Add some vertical padding(between each subject mark)

        '''
            here student.marks is a dictionary containing subject names as keys and their corresponding marks as values.
            the for loop iterates over each subject-mark pair in the dictionary,
            creating a label for each subject and its mark, and packing it into the dashboard window with some vertical padding.
            tk.Label is used to create text labels in the Tkinter GUI.
            dash is the parent window where the labels will be placed.
            text=f"{sub}: {mark}" formats the label to show the subject name and its mark.
        '''

    tk.Label(
        dash, text=f"Average: {student.average():.2f}",     # Display average mark formatted to 2 decimal places
        font=("Arial", 14),
        bg=BG
    ).pack(pady=5)      # Add some vertical padding(between average and grade section)

    tk.Label(
        dash, text=f"Grade: {student.grade()}",     # Display grade based on average mark
        font=("Arial", 16, "bold"),
        bg=BG
    ).pack(pady=10)     # Add some vertical padding(between grade and logout button)

    tk.Button(
        dash, text="Logout",        # Logout Button
        width=22, height=2,
        bg=LOGOUT, fg="white",
        font=("Arial", 12, "bold"),
        command=dash.destroy        # Close dashboard window on logout
    ).pack(pady=25)     # Add some vertical padding(between logout button and bottom of the window)
