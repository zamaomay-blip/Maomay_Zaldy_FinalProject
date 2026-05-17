"""
CLI Student Organizer
A command-line application for students to manage daily school activities
"""

import os
from utils import load_data, save_data, get_valid_input
from models import ClassSchedule, Assignment, GradeRecord, Note


def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    """Display main menu"""
    while True:
        clear_screen()

        print("=" * 50)
        print("📚 CLI STUDENT ORGANIZER".center(50))
        print("=" * 50)
        print("1. Manage Class Schedule")
        print("2. Assignment Tracker")
        print("3. Grade Calculator")
        print("4. Notes Manager")
        print("5. Exit")
        print("-" * 50)

        choice = get_valid_input(
            "Enter your choice: ",
            int,
            [1, 2, 3, 4, 5]
        )

        if choice == 1:
            schedule_menu()

        elif choice == 2:
            assignment_menu()

        elif choice == 3:
            grade_menu()

        elif choice == 4:
            notes_menu()

        elif choice == 5:
            print("\n✅ Data saved successfully!")
            print("Thank you for using CLI Student Organizer!")
            break


# ---------------------- CLASS SCHEDULE MODULE ----------------------
def schedule_menu():
    """Class schedule menu"""
    data = load_data()

    while True:
        print("\n" + "📅 CLASS SCHEDULE".center(50, "-"))
        print("1. Add New Schedule")
        print("2. View Schedule")
        print("3. Delete Schedule")
        print("4. Back")

        choice = get_valid_input(
            "Enter choice: ",
            int,
            [1, 2, 3, 4]
        )

        if choice == 4:
            break

        elif choice == 1:
            subject = input("Enter subject: ")
            day = input("Enter day: ")
            time = input("Enter time: ")
            room = input("Enter room: ")
            instructor = input("Enter instructor: ")

            sched = ClassSchedule(
                subject,
                day,
                time,
                room,
                instructor
            )

            data["schedules"].append(sched.to_dict())

            save_data(data)

            print("✅ Schedule added successfully!")

        elif choice == 2:
            schedules = sorted(
                data["schedules"],
                key=lambda x: x["day"]
            )

            if not schedules:
                print("No schedules available.")
                continue

            print("\n" + "=" * 50)

            for i, s in enumerate(schedules, 1):
                print(f"\n{i}. 📖 {s['subject']}")
                print(f"📅 {s['day']}")
                print(f"⏰ {s['time']}")
                print(f"📍 Room: {s['room']}")
                print(f"👨‍🏫 Instructor: {s['instructor']}")

        elif choice == 3:
            if not data["schedules"]:
                print("No schedules to delete.")
                continue

            for i, s in enumerate(data["schedules"], 1):
                print(f"{i}. {s['subject']}")

            idx = get_valid_input(
                "Enter number to delete: ",
                int
            ) - 1

            if 0 <= idx < len(data["schedules"]):
                deleted = data["schedules"].pop(idx)

                save_data(data)

                print(f"✅ {deleted['subject']} deleted!")


# ---------------------- ASSIGNMENT MODULE ----------------------
def assignment_menu():
    """Assignment tracker"""
    data = load_data()

    while True:
        print("\n" + "📝 ASSIGNMENT TRACKER".center(50, "-"))
        print("1. Add Assignment")
        print("2. View Pending Assignments")
        print("3. View Completed Assignments")
        print("4. Mark Assignment as Complete")
        print("5. Delete Assignment")
        print("6. Back")

        choice = get_valid_input(
            "Enter choice: ",
            int,
            [1, 2, 3, 4, 5, 6]
        )

        if choice == 6:
            break

        elif choice == 1:
            title = input("Enter assignment title: ")
            subject = input("Enter subject: ")
            deadline = input("Enter deadline: ")

            task = Assignment(
                title,
                subject,
                deadline
            )

            data["assignments"].append(task.to_dict())

            save_data(data)

            print("✅ Assignment added!")

        elif choice == 2:
            pending = [
                t for t in data["assignments"]
                if not t["is_completed"]
            ]

            if not pending:
                print("🎉 No pending assignments!")
                continue

            pending_sorted = sorted(
                pending,
                key=lambda x: x["deadline"]
            )

            print("\n" + "=" * 50)

            for i, t in enumerate(pending_sorted, 1):
                print(f"\n{i}. [{t['subject']}] {t['title']}")
                print(f"⏰ Deadline: {t['deadline']}")

        elif choice == 3:
            completed = [
                t for t in data["assignments"]
                if t["is_completed"]
            ]

            if not completed:
                print("No completed assignments.")
                continue

            print("\n" + "=" * 50)

            for i, t in enumerate(completed, 1):
                print(f"{i}. ✅ {t['title']}")

        elif choice == 4:
            pending = [
                t for t in data["assignments"]
                if not t["is_completed"]
            ]

            if not pending:
                print("No pending tasks.")
                continue

            for i, t in enumerate(pending, 1):
                print(f"{i}. {t['title']}")

            idx = get_valid_input(
                "Select assignment: ",
                int
            ) - 1

            if 0 <= idx < len(pending):
                pending[idx]["is_completed"] = True

                save_data(data)

                print("✅ Assignment marked as completed!")

        elif choice == 5:
            if not data["assignments"]:
                print("No assignments available.")
                continue

            for i, t in enumerate(data["assignments"], 1):
                print(f"{i}. {t['title']}")

            idx = get_valid_input(
                "Enter number to delete: ",
                int
            ) - 1

            if 0 <= idx < len(data["assignments"]):
                deleted = data["assignments"].pop(idx)

                save_data(data)

                print(f"✅ {deleted['title']} deleted!")


# ---------------------- GRADE MODULE ----------------------
def grade_menu():
    """Grade calculator"""
    data = load_data()

    while True:
        print("\n" + "📊 GRADE CALCULATOR".center(50, "-"))
        print("1. Add Grade")
        print("2. View Grades")
        print("3. Calculate GWA")
        print("4. Back")

        choice = get_valid_input(
            "Enter choice: ",
            int,
            [1, 2, 3, 4]
        )

        if choice == 4:
            break

        elif choice == 1:
            subject = input("Enter subject: ")

            grade = float(
                input("Enter grade: ")
            )

            record = GradeRecord(subject, grade)

            data["grades"].append(record.to_dict())

            save_data(data)

            print("✅ Grade added!")

        elif choice == 2:
            if not data["grades"]:
                print("No grades available.")
                continue

            print("\n" + "=" * 50)

            for g in data["grades"]:
                print(f"{g['subject']} : {g['grade']}")

        elif choice == 3:
            if not data["grades"]:
                print("No grades to calculate.")
                continue

            grades = [
                g["grade"]
                for g in data["grades"]
            ]

            gwa = sum(grades) / len(grades)

            print(f"\n🎓 Your GWA is: {gwa:.2f}")


# ---------------------- NOTES MODULE ----------------------
def notes_menu():
    """Notes manager"""
    data = load_data()

    while True:
        print("\n" + "🗒️ NOTES MANAGER".center(50, "-"))
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Back")

        choice = get_valid_input(
            "Enter choice: ",
            int,
            [1, 2, 3, 4]
        )

        if choice == 4:
            break

        elif choice == 1:
            title = input("Enter note title: ")
            content = input("Enter note content: ")

            note = Note(title, content)

            data["notes"].append(note.to_dict())

            save_data(data)

            print("✅ Note added!")

        elif choice == 2:
            if not data["notes"]:
                print("No notes available.")
                continue

            print("\n" + "=" * 50)

            for i, n in enumerate(data["notes"], 1):
                print(f"\n{i}. 📝 {n['title']}")
                print(f"{n['content']}")

        elif choice == 3:
            if not data["notes"]:
                print("No notes to delete.")
                continue

            for i, n in enumerate(data["notes"], 1):
                print(f"{i}. {n['title']}")

            idx = get_valid_input(
                "Enter note number: ",
                int
            ) - 1

            if 0 <= idx < len(data["notes"]):
                deleted = data["notes"].pop(idx)

                save_data(data)

                print(f"✅ {deleted['title']} deleted!")


# ---------------------- MAIN PROGRAM ----------------------
if  '__name__ == "__main__":
    main_menu()