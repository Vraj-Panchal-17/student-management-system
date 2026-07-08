from managers.student_manager import StudentManager

manager = StudentManager()

while True:
    print("="*5, "Student Management System", "="*5)
    print("1. Add Student")
    print("2. View Student")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Search Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        manager.add_student()

    elif choice == 2:
        manager.view_students()

    elif choice == 3:
        manager.delete_student()

    elif choice == 4:
        manager.update_student()

    elif choice == 5:
        manager.search_student()

    elif choice == 6:
        print("Exiting the program....")
        break

    else:
        print("Please enter valid choice.")