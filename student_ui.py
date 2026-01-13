import tkinter as tk
from tkinter import messagebox
import logic

def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

# ---------- STUDENT LOGIN ----------
def student_login():
    login_window = tk.Tk()
    login_window.title("Student Login - EduTrack")
    login_window.configure(bg="#f0f8ff")
    login_window.resizable(False, False)
    center_window(login_window, 400, 300)

    tk.Label(login_window, text="Student Login", font=("Arial", 18, "bold"), bg="#f0f8ff").pack(pady=20)
    tk.Label(login_window, text="Enter Name", bg="#f0f8ff").pack()
    name_entry = tk.Entry(login_window, width=30)
    name_entry.pack(pady=10)

    def verify():
        name = name_entry.get().strip()
        students = logic.load_students()
        for s in students.values():
            if s.name.lower() == name.lower():
                login_window.destroy()
                student_dashboard(s)
                return
        messagebox.showerror("Error", "Student not found")

    tk.Button(login_window, text="Login", width=20, height=2, bg="#3366cc", fg="white",
              font=("Arial", 12, "bold"), command=verify).pack(pady=15)

    login_window.mainloop()


# ---------- STUDENT DASHBOARD ----------
def student_dashboard(student):
    dash = tk.Tk()
    dash.title(f"Student Dashboard - {student.name}")
    dash.configure(bg="#e6f7ff")
    dash.resizable(False, False)
    center_window(dash, 500, 400)

    tk.Label(dash, text=f"Welcome, {student.name}", font=("Arial", 20, "bold"), bg="#e6f7ff").pack(pady=20)

    frame = tk.Frame(dash, bg="#e6f7ff")
    frame.pack(pady=20)

    tk.Label(frame, text=f"Maths: {student.marks['Maths']}", font=("Arial", 14), bg="#e6f7ff").pack(pady=5)
    tk.Label(frame, text=f"Science: {student.marks['Science']}", font=("Arial", 14), bg="#e6f7ff").pack(pady=5)
    tk.Label(frame, text=f"English: {student.marks['English']}", font=("Arial", 14), bg="#e6f7ff").pack(pady=5)
    tk.Label(frame, text=f"Average: {student.average():.2f}%", font=("Arial", 14), bg="#e6f7ff").pack(pady=5)
    tk.Label(frame, text=f"Grade: {student.grade()}", font=("Arial", 14, "bold"), bg="#e6f7ff").pack(pady=10)

    tk.Button(dash, text="Logout", width=20, height=2, bg="#cc3333", fg="white",
              font=("Arial", 12, "bold"), command=dash.destroy).pack(pady=20)

    dash.mainloop()
