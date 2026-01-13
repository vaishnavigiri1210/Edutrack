import tkinter as tk
from admin_ui import admin_login
from student_ui import student_login

BG = "#f4f6f9"
PRIMARY = "#1f3c88"

def login_home():
    root = tk.Tk()
    root.title("EduTrack - Login")
    root.state("zoomed")
    root.configure(bg=BG)

    tk.Label(
        root, text="EduTrack",
        font=("Arial", 30, "bold"),
        bg=BG, fg=PRIMARY
    ).pack(pady=30)

    tk.Label(
        root, text="Student Performance Management System",
        font=("Arial", 16),
        bg=BG, fg="#333"
    ).pack(pady=10)

    tk.Button(
        root, text="Admin Login",
        width=28, height=2,
        bg=PRIMARY, fg="white",
        font=("Arial", 14, "bold"),
        command=lambda: admin_login(root)
    ).pack(pady=25)

    tk.Button(
        root, text="Student Login",
        width=28, height=2,
        bg="#4caf50", fg="white",
        font=("Arial", 14, "bold"),
        command=lambda: student_login(root)
    ).pack(pady=10)

    root.mainloop()
