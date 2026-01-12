import tkinter as tk
from tkinter import messagebox
import logic

# -------- STUDENT LOGIN --------
def student_login():
    login = tk.Tk()
    login.title("Student Login")
    login.geometry("350x220")
    login.resizable(False, False)

    tk.Label(
        login,
        text="Student Login",
        font=("Arial", 14, "bold")
    ).pack(pady=15)

    tk.Label(login, text="Enter Student Name").pack()
    name_entry = tk.Entry(login)
    name_entry.pack(pady=5)

    def verify_student():
        name = name_entry.get().strip()
        students = logic.load_students()

        if not name:
            messagebox.showerror("Error", "Please enter student name")
            return

        for student in students.values():
            if student.name.lower() == name.lower():
                login.destroy()
                student_dashboard(student)
                return

        messagebox.showerror("Error", "Student not found")

    tk.Button(
        login,
        text="Login",
        width=15,
        command=verify_student
    ).pack(pady=15)

    login.mainloop()


# -------- STUDENT DASHBOARD --------
def student_dashboard(student):
    root = tk.Tk()
    root.title("Student Dashboard - EduTrack")
    root.geometry("400x300")
    root.resizable(False, False)

    tk.Label(
        root,
        text="Student Dashboard",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    tk.Label(root, text=f"Name: {student.name}", font=("Arial", 11)).pack(pady=5)
    tk.Label(root, text=f"Maths: {student.marks['Maths']}").pack()
    tk.Label(root, text=f"Science: {student.marks['Science']}").pack()
    tk.Label(root, text=f"English: {student.marks['English']}").pack()

    tk.Label(root, text=f"Average: {student.average():.2f}%").pack(pady=5)
    tk.Label(root, text=f"Grade: {student.grade()}", font=("Arial", 11, "bold")).pack(pady=5)

    tk.Button(
        root,
        text="Logout",
        width=15,
        command=root.destroy
    ).pack(pady=15)

    root.mainloop()
