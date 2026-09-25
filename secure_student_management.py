import os
import sqlite3


DB_NAME = "students_secure.db"


def get_database_connection():
    """Create and return a connection to the SQLite database."""
    return sqlite3.connect(DB_NAME)


def initialize_database():
    """Create the students table if it does not already exist."""
    connection = get_database_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade TEXT NOT NULL
            )
        """)

        connection.commit()

    except sqlite3.Error:
        print("Database initialization failed.")

    finally:
        connection.close()


def admin_login():
    """Authenticate the administrator using environment variables."""

    admin_username = os.getenv("ADMIN_USERNAME")
    admin_password = os.getenv("ADMIN_PASSWORD")

    if not admin_username or not admin_password:
        print("Administrator credentials are not configured.")
        return False

    print("\n=== Admin Login ===")

    username = input("Username: ")
    password = input("Password: ")

    if username == admin_username and password == admin_password:
        print("\nLogin successful.")
        return True

    print("\nInvalid username or password.")
    return False


def add_student():
    """Add a new student using a parameterized SQL query."""

    print("\n=== Add Student ===")

    student_id = input("Student ID: ").strip()

    if not student_id.isdigit():
        print("Student ID must contain only numbers.")
        return

    name = input("Name: ").strip()
    age = input("Age: ").strip()
    grade = input("Grade: ").strip()

    if not name or not age or not grade:
        print("All fields are required.")
        return

    if not age.isdigit():
        print("Age must contain only numbers.")
        return

    connection = get_database_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO students (student_id, name, age, grade)
            VALUES (?, ?, ?, ?)
            """,
            (int(student_id), name, int(age), grade)
        )

        connection.commit()
        print("Student added successfully.")

    except sqlite3.IntegrityError:
        print("A student with this ID already exists.")

    except sqlite3.Error:
        print("Unable to add student.")

    finally:
        connection.close()


def view_students():
    """Display all students."""

    print("\n=== Student List ===")

    connection = get_database_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT student_id, name, age, grade
            FROM students
            ORDER BY student_id
        """)

        students = cursor.fetchall()

        if not students:
            print("No students found.")
            return

        print("\nID\tName\tAge\tGrade")
        print("-" * 35)

        for student in students:
            print(
                f"{student[0]}\t"
                f"{student[1]}\t"
                f"{student[2]}\t"
                f"{student[3]}"
            )

    except sqlite3.Error:
        print("Unable to retrieve student records.")

    finally:
        connection.close()


def search_student():
    """Search for a student by ID using a parameterized query."""

    print("\n=== Search Student ===")

    student_id = input("Enter Student ID: ").strip()

    if not student_id.isdigit():
        print("Student ID must contain only numbers.")
        return

    connection = get_database_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT student_id, name, age, grade
            FROM students
            WHERE student_id = ?
            """,
            (int(student_id),)
        )

        student = cursor.fetchone()

        if student:
            print("\nStudent Found")
            print(f"ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Age: {student[2]}")
            print(f"Grade: {student[3]}")
        else:
            print("Student not found.")

    except sqlite3.Error:
        print("Unable to search student records.")

    finally:
        connection.close()


def delete_student():
    """Delete a student using a parameterized SQL query."""

    print("\n=== Delete Student ===")

    student_id = input("Enter Student ID: ").strip()

    if not student_id.isdigit():
        print("Student ID must contain only numbers.")
        return

    connection = get_database_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM students
            WHERE student_id = ?
            """,
            (int(student_id),)
        )

        connection.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    except sqlite3.Error:
        print("Unable to delete student.")

    finally:
        connection.close()


def main_menu():
    """Display the main application menu."""

    while True:
        print("\n===================================")
        print("      Student Management Menu")
        print("===================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please select 1-5.")


def main():
    print("===================================")
    print("   Secure Student Management System")
    print("===================================")

    initialize_database()

    if not admin_login():
        return

    main_menu()


if __name__ == "__main__":
    main()