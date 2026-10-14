# Student Information System

students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course Name: ")
    marks = input("Enter Student Marks: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
    else:
        print("\n--- Student Information ---")
        for student in students:
            print(student)


def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["ID"] == student_id:
            print("Student Found:", student)
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== Student Information System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
