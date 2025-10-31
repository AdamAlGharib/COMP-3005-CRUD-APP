from CRUD import getAllStudents, deleteStudent, addStudent, updateStudentEmail

def main():
    print("Welcome to your CRUD application!")

    while True:
        print("\nPlease choose an option:")
        print("1. Get all students")
        print("2. Delete a student")
        print("3. Add a student")
        print("4. Update a student's email")
        print("5. Exit")

        choice = input("Enter choice (1–5): ").strip().lower()

        if choice in ("1", "getallstudents"):
            getAllStudents()

        elif choice in ("2", "deletestudent"):
            student_id = input("Enter the student ID to delete: ").strip()
            deleteStudent(student_id)

        elif choice in ("3", "addstudent"):
            f = input("First name: ").strip()
            l = input("Last name: ").strip()
            e = input("Unique email: ").strip()
            d = input("Enrollment date (YYYY-MM-DD): ").strip()
            addStudent(f, l, e, d)

        elif choice in ("4", "updatestudentemail"):
            student_id = input("Enter the student ID to update: ").strip()
            new_email = input("Enter the new email: ").strip()
            updateStudentEmail(student_id, new_email)

        elif choice in ("5", "exit", "quit"):
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice — please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
