import tkinter as tk
from tkinter import messagebox
import logic

BG = "#f4f6f9"
PRIMARY = "#1f3c88"
LOGOUT = "#e53935"


def student_login(parent):
    win = tk.Toplevel(parent)
    win.title("Student Login")
    win.geometry("400x300")
    win.configure(bg=BG)

    tk.Label(
        win, text="Student Login",
        font=("Arial", 18, "bold"),
        bg=BG
    ).pack(pady=20)

    entry = tk.Entry(win, width=30)
    entry.pack(pady=10)

    def verify():
        students = logic.load_students()
        for s in students.values():
            if s.name.lower() == entry.get().lower():
                win.destroy()
                student_dashboard(parent, s)
                return
        messagebox.showerror("Error", "Student Not Found")

    tk.Button(
        win, text="Login",
        width=18, height=2,
        bg=PRIMARY, fg="white",
        font=("Arial", 12, "bold"),
        command=verify
    ).pack(pady=20)


def student_dashboard(parent, student):
    dash = tk.Toplevel(parent)
    dash.title("Student Dashboard")
    dash.geometry("500x420")
    dash.configure(bg=BG)

    tk.Label(
        dash, text=f"Welcome, {student.name}",
        font=("Arial", 20, "bold"),
        bg=BG
    ).pack(pady=20)

    for sub, mark in student.marks.items():
        tk.Label(
            dash, text=f"{sub}: {mark}",
            font=("Arial", 14),
            bg=BG
        ).pack(pady=3)

    tk.Label(
        dash, text=f"Average: {student.average():.2f}",
        font=("Arial", 14),
        bg=BG
    ).pack(pady=5)

    tk.Label(
        dash, text=f"Grade: {student.grade()}",
        font=("Arial", 16, "bold"),
        bg=BG
    ).pack(pady=10)

    # 🔴 ONLY LOGOUT RED
    tk.Button(
        dash, text="Logout",
        width=22, height=2,
        bg=LOGOUT, fg="white",
        font=("Arial", 12, "bold"),
        command=dash.destroy
    ).pack(pady=25)
