''' 
main file for EduTrack application 
(Frontend i.e. handles GUI using tkinter for adding student and viewing analytics dashboard)
'''

import tkinter as tk
from tkinter import messagebox
import logic
from tkinter import ttk
import matplotlib.pyplot as plt
import login

login.login_home()



# students = logic.load_students()

# def add_student():
#     """
#     Add student after validating input.
#     """
#     try:
#         name = name_entry.get()     # entry.get() used for user input
#         marks = {
#             "Maths": int(maths_entry.get()),
#             "Science": int(science_entry.get()),
#             "English": int(english_entry.get())
#         }

#         if any(m < 0 or m > 100 for m in marks.values()):       
#             raise ValueError

#         logic.save_student(name, marks)
#         messagebox.showinfo("Success", "Student added successfully")
#     except ValueError:
#         messagebox.showerror("Error", "Invalid marks entered")


# def show_dashboard():
#     """
#     Display analytics dashboard.
#     """
#     students = logic.load_students()
#     if not students:
#         messagebox.showwarning("Warning", "No student data available")
#         return

#     avg = logic.class_average(students)
#     top = logic.topper(students)

#     pass_count, fail_count = logic.result_summary(students)

#     # Class result status
#     if avg >= 75:
#         result = "Excellent Performance"
#     elif avg >= 60:
#         result = "Good Performance"
#     elif avg >= 40:
#         result = "Average Performance"
#     else:
#         result = "Poor Performance"

#     messagebox.showinfo(
#         "Dashboard",
#         f"Total Students: {len(students)}\n"
#         f"Class Average: {avg:.2f}%\n\n"
#         f"Pass Students: {pass_count}\n"
#         f"Fail Students: {fail_count}\n"
#         f"Class Result: {result}\n\n"
#         f"Topper: {top.name}\n"
#         f"Average: {top.average():.2f}%\n"
#         f"Grade: {top.grade()}"
#     )



# def show_weak():
#     """
#     Show students scoring below 40%.
#     """
#     students = logic.load_students()
#     weak = logic.weak_students(students)    # weak is a list of names
#     messagebox.showinfo("Weak Students", "\n".join(weak) if weak else "No weak students") 
#     # .join() joins list elements with newline character for display

# def view_students():
#     """
#     Display all students in a professional table using Treeview.
#     """
#     students = logic.load_students()
#     if not students:
#         messagebox.showwarning("Warning", "No student data available")
#         return

#     window = tk.Toplevel(root)
#     window.title("All Students Performance Report")
#     window.geometry("750x350")

#     title = tk.Label(
#         window,
#         text="All Students Performance Report",
#         font=("Arial", 14, "bold")
#     )
#     title.pack(pady=10)

#     # -------- Table Frame --------
#     frame = tk.Frame(window)
#     frame.pack(padx=10, pady=10, fill="both", expand=True)

#     columns = ("Name", "Maths", "Science", "English", "Average", "Grade")

#     table = ttk.Treeview(
#         frame,
#         columns=columns,
#         show="headings"
#     )

#     # Define headings
#     for col in columns:
#         table.heading(col, text=col)
#         table.column(col, anchor="center", width=110)

#     # Insert data
#     for student in students.values():
#         table.insert(
#             "",
#             "end",
#             values=(
#                 student.name,
#                 student.marks["Maths"],
#                 student.marks["Science"],
#                 student.marks["English"],
#                 f"{student.average():.2f}",
#                 student.grade()
#             )
#         )

#     # Scrollbar
#     scrollbar = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
#     table.configure(yscrollcommand=scrollbar.set)

#     table.pack(side="left", fill="both", expand=True)
#     scrollbar.pack(side="right", fill="y")


# def search_student():
#     """
#     Search student by name and display details.
#     """
#     students = logic.load_students()

#     if not students:
#         messagebox.showwarning("Warning", "No student data available")
#         return

#     name = name_entry.get().strip().lower()

#     if not name:
#         messagebox.showerror("Error", "Please enter student name")
#         return

#     for student in students.values():
#         if student.name.lower() == name:
#             messagebox.showinfo(
#                 "Student Found",
#                 f"Name: {student.name}\n"
#                 f"Maths: {student.marks['Maths']}\n"
#                 f"Science: {student.marks['Science']}\n"
#                 f"English: {student.marks['English']}\n\n"
#                 f"Average: {student.average():.2f}%\n"
#                 f"Grade: {student.grade()}"
#             )
#             return

#     messagebox.showerror("Not Found", "Student not found")

# def show_chart():
#     """
#     Display subject-wise average bar chart.
#     """
#     students = logic.load_students()
#     if not students:
#         messagebox.showwarning("Warning", "No student data available")
#         return

#     maths_avg = logic.subject_average(students, "Maths")
#     science_avg = logic.subject_average(students, "Science")
#     english_avg = logic.subject_average(students, "English")

#     subjects = ["Maths", "Science", "English"]
#     averages = [maths_avg, science_avg, english_avg]

#     plt.figure()
#     plt.bar(subjects, averages)
#     plt.xlabel("Subjects")
#     plt.ylabel("Average Marks")
#     plt.title("Subject-wise Average Performance")
#     plt.ylim(0, 100)
#     plt.show()


# # GUI Window
# root = tk.Tk()
# root.title("EduTrack - Student Analytics")
# root.geometry("450x350")

# # -------- Title --------
# title = tk.Label(
#     root,
#     text="EduTrack – Student Performance Analytics",
#     font=("Arial", 14, "bold")
# )
# title.grid(row=0, column=0, columnspan=2, pady=10)

# # -------- Form Frame --------
# form_frame = tk.Frame(root)
# form_frame.grid(row=1, column=0, padx=20, pady=10)

# tk.Label(form_frame, text="Student Name").grid(row=0, column=0, sticky="w")
# name_entry = tk.Entry(form_frame)
# name_entry.grid(row=0, column=1, pady=5)

# tk.Label(form_frame, text="Maths Marks").grid(row=1, column=0, sticky="w")
# maths_entry = tk.Entry(form_frame)
# maths_entry.grid(row=1, column=1, pady=5)

# tk.Label(form_frame, text="Science Marks").grid(row=2, column=0, sticky="w")
# science_entry = tk.Entry(form_frame)
# science_entry.grid(row=2, column=1, pady=5)

# tk.Label(form_frame, text="English Marks").grid(row=3, column=0, sticky="w")
# english_entry = tk.Entry(form_frame)
# english_entry.grid(row=3, column=1, pady=5)

# # -------- Button Frame --------
# button_frame = tk.Frame(root)
# button_frame.grid(row=1, column=1, padx=20)

# tk.Button(button_frame, text="Add Student", width=15, command=add_student)\
#     .grid(row=0, column=0, pady=5)

# tk.Button(button_frame, text="Dashboard", width=15, command=show_dashboard)\
#     .grid(row=1, column=0, pady=5)

# tk.Button(button_frame, text="Below 40%", width=15, command=show_weak)\
#     .grid(row=2, column=0, pady=5)

# tk.Button(
#     button_frame,
#     text="View Students",
#     width=15,
#     command=view_students
# ).grid(row=3, column=0, pady=5)

# tk.Button(
#     button_frame,
#     text="Search Student",
#     width=15,
#     command=search_student
# ).grid(row=4, column=0, pady=5)

# tk.Button(
#     button_frame,
#     text="Performance Chart",
#     width=15,
#     command=show_chart
# ).grid(row=5, column=0, pady=5)

# root.mainloop()

