import tkinter as tk
from tkinter import messagebox, ttk
import logic
from tkinter import scrolledtext

def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

# ---------- ADMIN LOGIN ----------
def admin_login():
    login_window = tk.Tk()
    login_window.title("Admin Login - EduTrack")
    login_window.configure(bg="#f0f8ff")
    login_window.resizable(False, False)
    center_window(login_window, 400, 300)

    tk.Label(login_window, text="Admin Login", font=("Arial", 18, "bold"), bg="#f0f8ff").pack(pady=20)
    tk.Label(login_window, text="Username", bg="#f0f8ff").pack()
    username = tk.Entry(login_window)
    username.pack(pady=5)
    tk.Label(login_window, text="Password", bg="#f0f8ff").pack()
    password = tk.Entry(login_window, show="*")
    password.pack(pady=5)

    def verify():
        if username.get() == "admin" and password.get() == "admin123":
            login_window.destroy()
            admin_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(login_window, text="Login", width=20, height=2, bg="#339966", fg="white", font=("Arial", 12, "bold"),
              command=verify).pack(pady=15)
    login_window.mainloop()


# ---------- ADMIN DASHBOARD ----------
def admin_dashboard():
    root = tk.Tk()
    root.title("Admin Dashboard - EduTrack")
    root.state("zoomed")
    root.configure(bg="#f0f8ff")

    tk.Label(root, text="Admin Dashboard", font=("Arial", 24, "bold"), bg="#f0f8ff").pack(pady=20)

    frame = tk.Frame(root, bg="#f0f8ff")
    frame.pack(pady=40)

    buttons = [
        ("Add Student", add_student_ui),
        ("View Students", view_students_ui),
        ("Weak Students", show_weak_students),
        ("Logout", lambda: root.destroy())
    ]

    for text, func in buttons:
        tk.Button(frame, text=text, width=25, height=2, bg="#339966", fg="white",
                  font=("Arial", 14, "bold"), command=func).pack(pady=15)

    root.mainloop()


# ---------- ADD STUDENT ----------
def add_student_ui():
    add_window = tk.Tk()
    add_window.title("Add Student - EduTrack")
    add_window.configure(bg="#f0f8ff")
    add_window.resizable(False, False)
    center_window(add_window, 500, 400)

    tk.Label(add_window, text="Add Student", font=("Arial", 18, "bold"), bg="#f0f8ff").pack(pady=20)

    entries = {}
    for field in ["Name", "Maths", "Science", "English"]:
        tk.Label(add_window, text=field, bg="#f0f8ff").pack()
        e = tk.Entry(add_window)
        e.pack(pady=5)
        entries[field] = e

    def save():
        try:
            name = entries["Name"].get()
            marks = {subj: int(entries[subj].get()) for subj in ["Maths", "Science", "English"]}
            logic.save_student(name, marks)
            messagebox.showinfo("Success", "Student Added Successfully")
            add_window.destroy()
        except:
            messagebox.showerror("Error", "Invalid input")

    tk.Button(add_window, text="Save", width=20, height=2, bg="#339966", fg="white",
              font=("Arial", 12, "bold"), command=save).pack(pady=15)
    add_window.mainloop()


# ---------- VIEW STUDENTS ----------
def view_students_ui():
    view_window = tk.Tk()
    view_window.title("All Students - EduTrack")
    view_window.configure(bg="#f0f8ff")
    view_window.resizable(False, False)
    center_window(view_window, 700, 500)

    tk.Label(view_window, text="All Students", font=("Arial", 18, "bold"), bg="#f0f8ff").pack(pady=20)

    cols = ("Name", "Maths", "Science", "English", "Average", "Grade")
    table = ttk.Treeview(view_window, columns=cols, show="headings", height=15)
    for col in cols:
        table.heading(col, text=col)
        table.column(col, width=100)
    table.pack(expand=True, fill="both")

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

    view_window.mainloop()


# ---------- WEAK STUDENTS ----------
def show_weak_students():
    students = logic.load_students()
    weak = logic.weak_students(students)
    if weak:
        messagebox.showinfo("Weak Students", "\n".join(weak))
    else:
        messagebox.showinfo("Weak Students", "No weak students found")
