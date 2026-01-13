'''
This file contains admin login contents which include:
- Admin Login Screen
- Admin Dashboard
- Add Student Screen
- View Students Screen
- Subject-wise Performance Chart
- Result Summary Pie Chart
'''

import tkinter as tk        # importing tkinter module for GUI development
from tkinter import messagebox, ttk # importing messagebox and ttk from tkinter module
import logic        # importing logic module for backend operations
import matplotlib.pyplot as plt     # importing matplotlib.pyplot module for creating charts

BG = "#f4f6f9"
PRIMARY = "#1f3c88"     # blue buttons
SECONDARY = "#4caf50"   # green buttons
LOGOUT = "#e53935"      # red only for logout


# ---------- ADMIN LOGIN ----------
def admin_login(parent):        # Admin Login Window
    win = tk.Toplevel(parent)   # it is used to create a new window
    win.title("Admin Login")
    win.geometry("400x300")
    win.configure(bg=BG)

    tk.Label(                       # styling of label 
        win, text="Admin Login",
        font=("Arial", 18, "bold"),
        bg=BG
    ).pack(pady=20) 

    ''' What pack() does:
        Arranges widgets automatically
        Places widgets top, bottom, left, or right
        Adds spacing using padx and pady 
    '''  

    ''' here pack is used for to keep the label in the center with padding of 20
    padx and pady are the options used in tkinter pack method to provide padding around widgets.
    padx: horizontal padding (left and right)
    pady: vertical padding (top and bottom)
    '''

    tk.Label(win, text="Username", bg=BG).pack()        # styling of label
    user = tk.Entry(win, width=25)                  # entry widget to take input from user
    user.pack(pady=5)                         # packing the entry widget with padding of 5

    tk.Label(win, text="Password", bg=BG).pack()    # styling of label
    pwd = tk.Entry(win, show="*", width=25)     # entry widget to take password input from user
    pwd.pack(pady=5)                 # packing the entry widget with padding of 5 (padding between username entry and password label)

    def verify():           # function to verify the username and password
        if user.get() == "admin" and pwd.get() == "admin123":   # checking the credentials
            win.destroy()        # destroying the login window
            admin_dashboard(parent)     # calling the admin dashboard function
        else:
            messagebox.showerror("Error", "Invalid Credentials")    # showing error message if credentials are invalid

    tk.Button(
        win, text="Login",          # styling of button
        width=15, height=1,         # size of button
        bg=PRIMARY, fg="white",     # background and foreground color of button
        font=("Arial", 12, "bold"), # font style of button
        command=verify        # command to be executed on button click mainly calling verify function
    ).pack(pady=20)           # packing the button with padding of 20(padding between password entry and login button)


# ---------- ADMIN DASHBOARD ----------
def admin_dashboard(parent):            # Admin Dashboard Window
    dash = tk.Toplevel(parent)          # it is used to create a new window
    dash.title("Admin Dashboard")       # title of the window
    dash.geometry("600x500")         # size of the window
    dash.configure(bg=BG)         # background color of the window

    tk.Label(
        dash, text="Admin Dashboard",       # styling of label
        font=("Arial", 26, "bold"),
        bg=BG
    ).pack(pady=25)

    frame = tk.Frame(dash, bg=BG)   # creating a frame inside the admin dashboard window this frame is used for organizing buttons
    frame.pack(pady=30)            # packing the frame with padding of 30 (padding between admin dashboard title and Add Student button)

    tk.Button(
        frame, text="Add Student",      # styling of Add Student button
        width=20, height=1,         # size of button
        bg=PRIMARY, fg="white",     # background and foreground color of button
        font=("Arial", 14, "bold"),     # font style of button
        command=lambda: add_student_ui(dash)        # command to be executed on button click mainly calling add_student_ui function
    ).pack(pady=10)     # packing the button with padding of 10 (padding between Add Student button and View Students button)

    tk.Button(                          
        frame, text="View Students",     # styling of View Students button
        width=20, height=1,     # size of button
        bg=PRIMARY, fg="white",     # background and foreground color of button
        font=("Arial", 14, "bold"),     # font style of button
        command=lambda: view_students_ui(dash)      # command to be executed on button click mainly calling view_students_ui function
    ).pack(pady=10)     # packing the button with padding of 10 (padding between View Students button and Performance Chart button) 

    tk.Button(
        frame, text="Performance Chart",        # styling of Performance Chart button
        width=20, height=1,     # size of button
        bg=PRIMARY, fg="white",     # background and foreground color of button
        font=("Arial", 14, "bold"),     # font style of button
        command=show_subject_chart      # command to be executed on button click mainly calling show_subject_chart function
    ).pack(pady=10)     # packing the button with padding of 10 (padding between Performance Chart button and Result Summary button)

    tk.Button( 
        frame, text="Result Summary",       # styling of Result Summary button
        width=20, height=1,    # size of button 
        bg=PRIMARY, fg="white",     # background and foreground color of button
        font=("Arial", 14, "bold"),     # font style of button
        command=show_result_pie     # command to be executed on button click mainly calling show_result_pie function
    ).pack(pady=10)     # packing the button with padding of 10 (padding between Result Summary button and Logout button)

    tk.Button(
        frame, text="Logout",       # styling of Logout button
        width=15, height=1,     # size of button
        bg=LOGOUT, fg="white",          # background and foreground color of button
        font=("Arial", 14, "bold"),     # font style of button
        command=dash.destroy        # command to be executed on button click mainly to destroy the admin dashboard window
    ).pack(pady=30)         # packing the button with padding of 30 (padding between Logout button and bottom of the window)


# ---------- ADD STUDENT ----------
def add_student_ui(parent):     # Add Student Window
    win = tk.Toplevel(parent)       # it is used to create a new window
    win.title("Add Student")        # title of the window
    win.geometry("420x420")     # size of the window
    win.configure(bg=BG)        # background color of the window

    tk.Label(
        win, text="Add Student",        # styling of label
        font=("Arial", 18, "bold"),        #  font style of label
        bg=BG                               # background color of label
    ).pack(pady=20)       # packing the label with padding of 20 (padding between Add Student title and Name label)

    entries = {}           # empty dictionary to store the entry widgets
    for field in ["Name", "Maths", "Science", "English"]:      
        tk.Label(win, text=field, bg=BG).pack()   
        e = tk.Entry(win, width=30)
        e.pack(pady=5)
        entries[field] = e
    '''
        for loop is used to create labels and entry widgets for Name, Maths, Science, and English fields.
        in membership operator is used to iterate over the list of fields.
        win: parent window where the widgets will be placed.
        text=field: text of the label will be the current field in the loop.
        bg=BG: background color of the label.
        pack(): method to place the label in the window.
        e: entry widget to take input from user for the current field.
        entries[field] = e: storing the entry widget in the dictionary with the field name as the key.

    '''
    def save():     # function to save the student details
        try:
            name = entries["Name"].get()    # getting the name from the entry widget
            marks = {s: int(entries[s].get()) for s in ["Maths", "Science", "English"]}     
            '''
                here dictionary comprehension used to create a dictionary of marks for each subject.
                s is used to iterate over the list of subjects.
                int(entries[s].get()): getting the marks from the entry widget and converting it to integer.
            '''
            logic.save_student(name, marks)     # calling the save_student function from logic module to save the student details
            messagebox.showinfo("Success", "Student Added Successfully")
            win.destroy()
        except:
            messagebox.showerror("Error", "Invalid Input")

    tk.Button(
        win, text="Save",       # styling of Save button
        width=18, height=1,     
        bg=SECONDARY, fg="white",
        font=("Arial", 12, "bold"),
        command=save        # command to be executed on button click mainly calling save function
    ).pack(pady=25)     # packing the button with padding of 25 (padding between Save button and bottom of the window)


# ---------- VIEW STUDENTS ----------
def view_students_ui(parent):       # View Students Window
    win = tk.Toplevel(parent)
    win.title("All Students")
    win.geometry("750x500")
    win.configure(bg=BG)

    cols = ("Name", "Maths", "Science", "English", "Average", "Grade")  # columns for the table
    table = ttk.Treeview(win, columns=cols, show="headings", height=15) 
    # creating a treeview widget to display the student details in tabular format

    for col in cols:        # setting the headings and column widths
        table.heading(col, text=col)    # it sets the heading of each column in the table
        table.column(col, width=120)    # it sets the width of each column in the table

    table.pack(expand=True, fill="both", padx=20, pady=20)
    '''
        packing the table with expand, fill, padx, and pady options.
        expand=True: allows the table to expand and fill any extra space in the window.
        fill="both": allows the table to fill both horizontally and vertically within its allocated space.
        padx=20: adds horizontal padding of 20 pixels on both sides of the table.
        pady=20: adds vertical padding of 20 pixels on both top and bottom of the table.
    '''

    students = logic.load_students()        # loading the student details from the logic module
    for s in students.values():
        table.insert("", "end", values=(
            s.name,
            s.marks["Maths"],
            s.marks["Science"],
            s.marks["English"],
            f"{s.average():.2f}",
            s.grade()
        ))
        '''
            inserting the student details into the table.
            "" : indicates that the item is to be inserted at the root level of the treeview.
            "end": specifies that the new item should be added at the end of the existing items in the treeview.
            values: a tuple containing the values for each column in the table for the current student.
        '''

# ---------- CHARTS ----------
def show_subject_chart():       # Subject-wise Performance Chart
    students = logic.load_students()        # loading the student details from the logic module
    subjects = ["Maths", "Science", "English"]      # list of subjects
    averages = [logic.subject_average(students, s) for s in subjects]
    '''
        list comprehension to create a list of average marks for each subject.
        s is used to iterate over the list of subjects.
        logic.subject_average(students, s): calling the subject_average function from logic
        module to get the average marks for the subject s.
    '''

    #  plt is matplotlib.pyplot module used for creating static, animated, and interactive visualizations in Python.
    plt.figure()     # creates a new figure for the plot.   
    plt.bar(subjects, averages)   # creates a bar chart with subjects on the x-axis and their corresponding average marks on the y-axis.
    plt.title("Subject-wise Average Marks")  # sets the title of the chart.
    plt.xlabel("Subjects")    # sets the label for the x-axis.
    plt.ylabel("Marks")     # sets the label for the y-axis.
    plt.show()      # displays the chart.

def show_result_pie():      # Result Summary Pie Chart
    students = logic.load_students()     # loading the student details from the logic module
    p, f = logic.result_summary(students)   # calling the result_summary function from logic module to get the number of pass and fail students  

    plt.figure()        # creates a new figure for the plot.
    plt.pie(        # creates a pie chart with pass and fail students
        [p, f],     # data for the pie chart
        labels=["Pass", "Fail"],    # labels for the pie chart
        colors=["#4caf50", "#e53935"],  # green pass, red fail
        autopct="%1.1f%%",      # format for displaying percentage on the pie chart means 1 digit before decimal and 1 digit after decimal
        startangle=90       # starting angle for the pie chart
    )
    plt.title("Result Summary")     # sets the title of the chart
    plt.show()    # displays the chart
