def calculate_total(marks):
    return sum(marks)


def calculate_average(total, subject_count):
    return total / subject_count


def check_pass_all(marks, pass_mark=50):
    for mark in marks:
        if mark < pass_mark:
            return False
    return True


def determine_grade(average, passed):
    if not passed:
        return "F (Failed)"
    elif average >= 80:
        return "A (Distinction)"
    elif average >= 65:
        return "B (Credit)"
    else:
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
    for i in range(len(subjects)):
        subject = subjects[i]
        mark = marks[i]
        if mark >= 50:
            status = "Pass"
        else:
            status = "Fail"
        print(f"{subject}: {mark} ({status})")
    print("--------------------------------")
    print(f"Total Marks : {total}")
    print(f"Average     : {average:.2f}")
    print(f"Final Result: {grade}")
    print("================================\n")


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
                score = int(input(f"Enter marks for {subject} (0-100): "))
                marks.append(score)

            display_report_card(name, subjects, marks)

            total = calculate_total(marks)
            average = calculate_average(total, len(marks))
            passed = check_pass_all(marks)

            students.append({
                "name": name,
                "total": total,
                "average": average,
                "passed": passed
            })

        elif choice == "2":
            if len(students) == 0:
                print("\nNo student records found.\n")
            else:
                print("\n--- SAVED STUDENTS ---")
                for i in range(len(students)):
                    s = students[i]
                    if s["passed"]:
                        status = "Passed"
                    else:
                        status = "Failed"
                    print(f"{i + 1}. {s['name']} | Total: {s['total']} | Avg: {s['average']:.2f} | Status: {status}")
                print()

        elif choice == "3":
            print("Exiting Student Grade System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
