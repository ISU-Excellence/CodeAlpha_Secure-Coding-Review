# CodeAlpha Task 3 — Secure Coding Review

## Python Student Management System

A secure coding review of a Python-based Student Management System developed for the CodeAlpha Cyber Security Internship.

## Student Information

- **Name:** Mozumder Aktia Pableha
- **University:** Huzhou University
- **Major:** Computer Science
- **Internship:** CodeAlpha Cyber Security Internship
- **Task:** Task 3 — Secure Coding Review

---

## 1. Project Overview

This project demonstrates a secure coding review of a Python Student Management System using SQLite.

The project contains two versions:

1. **Vulnerable Version** — contains intentionally insecure coding practices for security analysis.
2. **Secure Version** — addresses the identified vulnerabilities using secure coding practices.

The review combines:

- Static analysis
- Manual code inspection
- Vulnerability identification
- Security remediation
- Functional testing
- Final security verification

---

## 2. Technologies Used

- Python 3.13.14
- SQLite
- Bandit 1.9.4
- Windows CMD
- Git / GitHub

---

## 3. Application Features

The Student Management System provides:

- Administrator authentication
- Add student
- View students
- Search student
- Delete student
- SQLite database storage

---

## 4. Project Structure

```text
Secure-Coding-Review/
│
├── student_management.py
├── secure_student_management.py
├── bandit-report.txt
├── README.md
├── requirements.txt
├── students_secure.db
├── reports/
└── screenshots/