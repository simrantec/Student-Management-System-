import csv
import os

FILE_NAME = "students.csv"


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(
                ["Student_ID", "Name", "Age", "Course", "Marks"]
            )

        writer.writerow([student_id, name, age, course, marks])

    print("Student added successfully!")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))


def search_student():
    student_id = input("Enter Student ID to search: ")

    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Student_ID"] == student_id:
                print("Student Found:", student)
                return

    print("Student not found.")


def main():
    while True:
        print("\n--- Student Information System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
