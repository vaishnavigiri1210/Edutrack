import tkinter as tk
from tkinter import messagebox
import logic
from tkinter import ttk
import matplotlib.pyplot as plt

# -------- ADMIN LOGIN --------
def admin_login():
    login = tk.Tk()
    login.title("Admin Login")
    login.geometry("350x250")
    login.resizable(False, False)

    tk.Label(login, text="Admin Login", font=("Arial", 14, "bold")).pack(pady=15)

    tk.Label(login, text="Username").pack()
    username_entry = tk.Entry(login)
    username_entry.pack(pady=5)

    tk.Label(login, text="Password").pack()
    password_entry = tk.Entry(login, show="*")
    password_entry.pack(pady=5)

    def verify_admin():
        username = username_entry.get()
        password = password_entry.get()

        if username == "admin" and password == "admin123":
            login.destroy()
            admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid Admin Credentials")

    tk.Button(login, text="Login", width=15, command=verify_admin).pack(pady=15)

    login.mainloop()

def admin_dashboard():
    root = tk.Tk()
    root.title("Admin Dashboard - EduTrack")
    root.geometry("500x400")

    tk.Label(
        root,
        text="Admin Dashboard",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    # -------- Buttons --------
    tk.Button(root, text="Add Student", width=20).pack(pady=5)
    tk.Button(root, text="View Students", width=20).pack(pady=5)
    tk.Button(root, text="Dashboard Analytics", width=20).pack(pady=5)
    tk.Button(root, text="Weak Students", width=20).pack(pady=5)
    tk.Button(root, text="Performance Chart", width=20).pack(pady=5)

    root.mainloop()
