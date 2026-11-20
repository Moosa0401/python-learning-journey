import sys


def main():
    
    students = {}

    while True:
        show_menu()

        try:
            choice = int(input("\nEnter your choice: "))

            match choice:
                case 1:
                    add_student(students)

                case 2:
                    view_all_students(students)

                case 3:
                    calculate_avg(students)

                case 4:
                    highest_grade(students)

                case 5:
                    print("Goodbye!")
                    sys.exit()

                case _:
                    print("Invalid choice. Please enter a number between 1 and 5.\n")

        except ValueError:
            print("Invalid input. Please enter a number.\n")


def show_menu():
    print("\n===== Student Grade Manager =====\n")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Calculate Class Average")
    print("4. Find Highest Grade")
    print("5. Exit")


def add_student(students):
    name = input("Student name: ").strip()

    if not name:
        print("Student name cannot be empty.\n")
        return

    if name in students:
        print("Student already exists.\n")
        return

    try:
        grade = int(input("Grade (0-100): "))

        if not 0 <= grade <= 100:
            print("Grade must be between 0 and 100.\n")
            return

        students[name] = grade
        print("Student added successfully!\n")

    except ValueError:
        print("Invalid grade. Please enter a number.\n")


def view_all_students(students):
    if not students:
        print("No students found.\n")
        return

    print("\n===== All Students =====")

    for name, grade in students.items():
        print(f"{name}: {grade}")

    print()


def calculate_avg(students):
    if not students:
        print("No students available.\n")
        return

    total = 0

    for grade in students.values():
        total += grade

    average = total / len(students)

    print(f"Class Average: {average:.2f}\n")


def highest_grade(students):
    if not students:
        print("No students available.\n")
        return

    highest_score = -1
    top_student = ""

    for name, grade in students.items():
        if grade > highest_score:
            highest_score = grade
            top_student = name

    print(f"Highest Grade: {top_student} ({highest_score})\n")


if __name__ == "__main__":
    main()