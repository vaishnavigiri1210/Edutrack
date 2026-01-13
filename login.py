import tkinter as tk
from admin_ui import admin_login
from student_ui import student_login

def center_window(win, width, height):
    # Center window on the screen
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

def login_home():
    root = tk.Tk()
    root.title("EduTrack – Login")
    root.configure(bg="#e6f0ff")

    # Main screen maximizable
    root.state("zoomed")

    tk.Label(root, text="EduTrack", font=("Arial", 28, "bold"), bg="#e6f0ff", fg="#003366").pack(pady=30)
    tk.Label(root, text="Student Performance Management System", font=("Arial", 16), bg="#e6f0ff", fg="#003366").pack(pady=10)

    tk.Button(root, text="Admin Login", width=25, height=2, bg="#3366cc", fg="white", font=("Arial", 14, "bold"),
              command=admin_login).pack(pady=30)
    
    tk.Button(root, text="Student Login", width=25, height=2, bg="#339966", fg="white", font=("Arial", 14, "bold"),
              command=student_login).pack(pady=20)

    root.mainloop()
