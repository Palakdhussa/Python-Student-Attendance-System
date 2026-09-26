students = {}

while True:
    print("\n--- Attendance Management System ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students[name] = 0
        print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            present = input("Present? (yes/no): ").lower()

            if present == "yes":
                students[name] += 1
                print("Attendance marked.")
            else:
                print("Marked absent.")
        else:
            print("Student not found.")

    elif choice == "3":
        print("\n--- Attendance Report ---")

        for name, attendance in students.items():
            print(f"{name}: {attendance} days present")

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
