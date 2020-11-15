import functions as func

print("""Welcome to Progress Prediction Application
    -> Press 1 - If you are a student
    -> Press 2 - If you are a member of staff
""")  # Prompting the menu for the user

menu_choice = func.CharInput("Enter Number", (1, 2)).int_input()  # The question, The set of parameter in a tuple
if menu_choice == 1:
    print("""
For Students =>
    """)
    print(func.student_progress_cal())

if menu_choice == 2:
    print("""
For Staff =>
    -> Press 1 - Manual Input
    -> Press 2 - Automatic Input
    """)
    staff_choice = func.CharInput("Enter Number", (1, 2)).int_input()
    if staff_choice == 1:
        func.ForStaff.manual()

    if staff_choice == 2:
        func.ForStaff.automatic()

    else:
        pass

else:
    pass
