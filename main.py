'''
main.py this is the main file that runs the application.
It imports the login module and calls the login_home function to start the login process.
'''

import login        # importing the login module

def main():         # defining the main function
    login.login_home()      # calling the login_home function from the login module

if __name__ == "__main__":
    main()


'''
    __name__ is a special built-in variable in Python that represents the name of the current module.
    __main__ is means the name of the top-level script environment.
    When a Python file is run directly, __name__ is set to "__main__".
    means when this file is executed directly, the condition will be true, and main() will be called.

    so it calls the main() function to start the application.
    here used to ensure that main() runs only when this file is executed as the main program.
    if it's is not written output will not generated because main() will not be called.

    in this project, main.py serves as the entry point to the EduTrack application,
    and it contains lots of other modules like login.py, admin_ui.py, student_ui.py etc.
    so when main.py is run, it starts the login process by calling login.login_home().
    and it avoids other modules being executed unintentionally when they are imported.
'''