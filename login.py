import tkinter as tk
from tkinter import messagebox
import admin_ui
import student_ui

def open_admin_login():
    admin_ui.admin_login()

def open_student_login():
    student_ui.student_login()

def login_home():
    root = tk.Tk()
    root.title("EduTrack Login")
    root.geometry("400x300")
    root.resizable(False, False)

    tk.Label(
        root,
        text="EduTrack – Student Performance System",
        font=("Arial", 14, "bold")
    ).pack(pady=30)

    tk.Button(
        root,
        text="Admin Login",
        width=20,
        height=2,
        command=open_admin_login
    ).pack(pady=10)

    tk.Button(
        root,
        text="Student Login",
        width=20,
        height=2,
        command=open_student_login
    ).pack(pady=10)

    root.mainloop()
