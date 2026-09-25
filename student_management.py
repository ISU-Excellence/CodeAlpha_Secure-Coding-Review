import sqlite3
import os

# Database connection
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    grade TEXT
)
""")
conn.commit()

# Hardcoded credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


def login():
    print("\n=== Admin Login ===")

    username = input("Username: ")
    password = input("Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful!")
        return True

    print("Invalid username or password.")
    return False


def add_student():
    print("\n=== Add Student ===")

    name = input("Student name: ")
    email = input("Student email: ")
    grade = input("Student grade: ")

    # Direct SQL construction
    query = f"""
    INSERT INTO students (name, email, grade)
    VALUES ('{name}', '{email}', '{grade}')
    """

    try:
        cursor.execute(query)
        conn.commit()
        print("Student added successfully.")
    except Exception as e:
        print("Database error:", e)


def view_students():
    print("\n=== Student List ===")

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    for student in students:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Email: {student[2]} | "
            f"Grade: {student[3]}"
        )


def search_student():
    print("\n=== Search Student ===")

    name = input("Enter student name: ")

    query = f"SELECT * FROM students WHERE name = '{name}'"

    try:
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            for student in results:
                print(
                    f"ID: {student[0]} | "
                    f"Name: {student[1]} | "
                    f"Email: {student[2]} | "
                    f"Grade: {student[3]}"
                )
        else:
            print("No student found.")

    except Exception as e:
        print("Database error:", e)


def delete_student():
    print("\n=== Delete Student ===")

    student_id = input("Enter student ID: ")

    query = f"DELETE FROM students WHERE id = {student_id}"

    try:
        cursor.execute(query)
        conn.commit()
        print("Student deleted successfully.")
    except Exception as e:
        print("Database error:", e)


def main():
    print("===================================")
    print("   Student Management System")
    print("===================================")

    if not login():
        return

    while True:
        print("\n=== Main Menu ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

conn.close()