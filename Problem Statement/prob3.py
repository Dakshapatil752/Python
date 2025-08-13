"""
Simple Student Grade Management System
"""

# Dictionary to store student names and grades
students = {}

while True:
    print("\n--- Student Grade Management ---")
    print("1. Add new student and grade")
    print("2. Update grade of existing student")
    print("3. Remove student")
    print("4. Calculate and display average grade")
    print("5. Display highest and lowest grade")
    print("6. Display all students and grades")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        students[name] = grade
        print(f"Added {name} with grade {grade}.")

    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in students:
            grade = float(input("Enter new grade: "))
            students[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print("Student not found.")

    elif choice == '3':
        name = input("Enter student name to remove: ")
        if name in students:
            del students[name]
            print(f"Removed {name} from the list.")
        else:
            print("Student not found.")

    elif choice == '4':
        if students:
            avg = sum(students.values()) / len(students)
            print(f"Average grade of the class: {avg:.2f}")
        else:
            print("No students in the list.")

    elif choice == '5':
        if students:
            highest = max(students.values())
            lowest = min(students.values())
            print(f"Highest grade: {highest}")
            print(f"Lowest grade: {lowest}")
        else:
            print("No students in the list.")

    elif choice == '6':
        if students:
            print("Students and their grades:")
            for name, grade in students.items():
                print(f"{name}: {grade}")
        else:
            print("No students in the list.")

    elif choice == '7':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
