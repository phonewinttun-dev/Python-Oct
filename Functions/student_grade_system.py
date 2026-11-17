def calculate_total(marks):
    return sum(marks)


def calculate_average(total, subject_count):
    return total / subject_count


def check_pass_all(marks, pass_mark=50):
    return all(mark >= pass_mark for mark in marks)


def determine_grade(average, passed):
    if not passed:
        return "F (Failed)"
    if average >= 80:
        return "A (Distinction)"
    if average >= 65:
        return "B (Credit)"
    return "C (Pass)"


def display_report_card(name, subjects, marks):
    total = calculate_total(marks)
    # total = sum(marks)
    average = calculate_average(total, len(marks))
    passed = check_pass_all(marks)
    grade = determine_grade(average, passed)

    print("\n================================")
    print("      STUDENT REPORT CARD       ")
    print("================================")
    print(f"Student Name: {name}")
    print("--------------------------------")
    for subject, mark in zip(subjects, marks):
        status = "Pass" if mark >= 50 else "Fail"
        print(f"{subject:<15}: {mark} ({status})")
    print("--------------------------------")
    print(f"Total Marks    : {total}")
    print(f"Average        : {average:.2f}")
    print(f"Final Result   : {grade}")
    print("================================\n")

    return total, average, passed, grade


def main():
    students = []

    while True:
        print("--- STUDENT GRADE SYSTEM ---")
        print("1. Add Student & Calculate Grade")
        print("2. View All Saved Students")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            name = input("Enter student name: ")
            subjects = ["Myanmar", "English", "Math", "Science"]
            marks = []

            for subject in subjects:
                while True:
                    try:
                        score = int(input(f"Enter marks for {subject} (0-100): "))
                        if 0 <= score <= 100:
                            marks.append(score)
                            break
                        else:
                            print("Marks must be between 0 and 100.")
                    except ValueError:
                        print("Please enter a valid number.")

            total, average, passed, _ = display_report_card(name, subjects, marks)
            students.append({
                "name": name,
                "total": total,
                "average": average,
                "passed": passed
            })

        elif choice == "2":
            if not students:
                print("\nNo student records found.\n")
            else:
                print("\n--- SAVED STUDENTS ---")
                for idx, s in enumerate(students, 1):
                    status = "Passed" if s["passed"] else "Failed"
                    print(f"{idx}. {s['name']} | Total: {s['total']} | Avg: {s['average']:.2f} | Status: {status}")
                print()

        elif choice == "3":
            print("Exiting Student Grade System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
