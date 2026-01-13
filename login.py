'''
login.py - This module creates the login home screen for the EduTrack application,
allowing users to choose between Admin and Student login options.
'''

import tkinter as tk            # GUI library for creating the application window
from admin_ui import admin_login        # Function to handle admin login
from student_ui import student_login    # Function to handle student login

BG = "#f4f6f9"
PRIMARY = "#1f3c88"

def login_home():       # Function to create the login home screen
    root = tk.Tk()      # Initialize the main application window
    root.title("EduTrack - Login")  # Set window title
    root.state("zoomed")        # Maximize window to full screen
    root.configure(bg=BG)   # Set background color

    tk.Label(           # Create and place the main title label
        root, text="EduTrack",      # Application title
        font=("Arial", 30, "bold"),     # Font settings
        bg=BG, fg=PRIMARY       # Background and foreground colors
    ).pack(pady=30)     # Add vertical padding

    tk.Label(           # Create and place the subtitle label
        root, text="Student Performance Management System",     # Subtitle text
        font=("Arial", 16),     # Font settings
        bg=BG, fg="#333"        # Background and foreground colors
    ).pack(pady=10)     # Add vertical padding

    tk.Button(
        root, text="Admin Login",          # Admin login button
        width=28, height=2,
        bg=PRIMARY, fg="white",
        font=("Arial", 14, "bold"),
        command=lambda: admin_login(root)       # Call admin login function on click which is present in admin_ui module
    ).pack(pady=25)   # Add vertical padding(between admin login and student login button)

    tk.Button(
        root, text="Student Login",     # Student login button
        width=28, height=2,
        bg="#4caf50", fg="white",
        font=("Arial", 14, "bold"),
        command=lambda: student_login(root)     # Call student login function on click which is present in student_ui module
    ).pack(pady=10)  # Add vertical padding(between student login button and bottom of the window)

    root.mainloop()
