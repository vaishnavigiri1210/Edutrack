import tkinter as tk
from tkinter import messagebox, ttk
import logic
import matplotlib.pyplot as plt

BG = "#f4f6f9"
PRIMARY = "#1f3c88"     # blue buttons
SECONDARY = "#4caf50"   # green buttons
LOGOUT = "#e53935"      # red only for logout


# ---------- ADMIN LOGIN ----------
def admin_login(parent):
    win = tk.Toplevel(parent)
    win.title("Admin Login")
    win.geometry("400x300")
    win.configure(bg=BG)

    tk.Label(
        win, text="Admin Login",
        font=("Arial", 18, "bold"),
        bg=BG
    ).pack(pady=20)

    tk.Label(win, text="Username", bg=BG).pack()
    user = tk.Entry(win, width=25)
    user.pack(pady=5)

    tk.Label(win, text="Password", bg=BG).pack()
    pwd = tk.Entry(win, show="*", width=25)
    pwd.pack(pady=5)

    def verify():
        if user.get() == "admin" and pwd.get() == "admin123":
            win.destroy()
            admin_dashboard(parent)
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    tk.Button(
        win, text="Login",
        width=15, height=1,
        bg=PRIMARY, fg="white",
        font=("Arial", 12, "bold"),
        command=verify
    ).pack(pady=20)


# ---------- ADMIN DASHBOARD ----------
def admin_dashboard(parent):
    dash = tk.Toplevel(parent)
    dash.title("Admin Dashboard")
    dash.state("zoomed")
    dash.configure(bg=BG)

    tk.Label(
        dash, text="Admin Dashboard",
        font=("Arial", 26, "bold"),
        bg=BG
    ).pack(pady=25)

    frame = tk.Frame(dash, bg=BG)
    frame.pack(pady=30)

    tk.Button(
        frame, text="Add Student",
        width=20, height=1,
        bg=PRIMARY, fg="white",
        font=("Arial", 14, "bold"),
        command=lambda: add_student_ui(dash)
    ).pack(pady=10)

    tk.Button(
        frame, text="View Students",
        width=20, height=1,
        bg=PRIMARY, fg="white",
        font=("Arial", 14, "bold"),
        command=lambda: view_students_ui(dash)
    ).pack(pady=10)

    tk.Button(
        frame, text="Performance Chart",
        width=20, height=1,
        bg=PRIMARY, fg="white",
        font=("Arial", 14, "bold"),
        command=show_subject_chart
    ).pack(pady=10)

    tk.Button(
        frame, text="Result Summary",
        width=20, height=1,
        bg=PRIMARY, fg="white",
        font=("Arial", 14, "bold"),
        command=show_result_pie
    ).pack(pady=10)

    # 🔴 ONLY LOGOUT BUTTON RED
    tk.Button(
        frame, text="Logout",
        width=15, height=1,
        bg=LOGOUT, fg="white",
        font=("Arial", 14, "bold"),
        command=dash.destroy
    ).pack(pady=30)


# ---------- ADD STUDENT ----------
def add_student_ui(parent):
    win = tk.Toplevel(parent)
    win.title("Add Student")
    win.geometry("420x420")
    win.configure(bg=BG)

    tk.Label(
        win, text="Add Student",
        font=("Arial", 18, "bold"),
        bg=BG
    ).pack(pady=20)

    entries = {}
    for field in ["Name", "Maths", "Science", "English"]:
        tk.Label(win, text=field, bg=BG).pack()
        e = tk.Entry(win, width=30)
        e.pack(pady=5)
        entries[field] = e

    def save():
        try:
            name = entries["Name"].get()
            marks = {s: int(entries[s].get()) for s in ["Maths", "Science", "English"]}
            logic.save_student(name, marks)
            messagebox.showinfo("Success", "Student Added Successfully")
            win.destroy()
        except:
            messagebox.showerror("Error", "Invalid Input")

    tk.Button(
        win, text="Save",
        width=18, height=1,
        bg=SECONDARY, fg="white",
        font=("Arial", 12, "bold"),
        command=save
    ).pack(pady=25)


# ---------- VIEW STUDENTS ----------
def view_students_ui(parent):
    win = tk.Toplevel(parent)
    win.title("All Students")
    win.geometry("750x500")
    win.configure(bg=BG)

    cols = ("Name", "Maths", "Science", "English", "Average", "Grade")
    table = ttk.Treeview(win, columns=cols, show="headings", height=15)

    for col in cols:
        table.heading(col, text=col)
        table.column(col, width=120)

    table.pack(expand=True, fill="both", padx=20, pady=20)

    students = logic.load_students()
    for s in students.values():
        table.insert("", "end", values=(
            s.name,
            s.marks["Maths"],
            s.marks["Science"],
            s.marks["English"],
            f"{s.average():.2f}",
            s.grade()
        ))


# ---------- CHARTS ----------
def show_subject_chart():
    students = logic.load_students()
    subjects = ["Maths", "Science", "English"]
    averages = [logic.subject_average(students, s) for s in subjects]

    plt.figure()
    plt.bar(subjects, averages)
    plt.title("Subject-wise Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()


def show_result_pie():
    students = logic.load_students()
    p, f = logic.result_summary(students)

    plt.figure()
    plt.pie(
        [p, f],
        labels=["Pass", "Fail"],
        colors=["#4caf50", "#e53935"],  # green pass, red fail
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Result Summary")
    plt.show()
