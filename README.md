# student-placement-tracker
A Python OOP project for managing student placement profiles.
# Student Placement Tracker

A Python-based console application that helps manage student placement records. The application allows users to add students, update mock interview scores, track placement readiness, and manage student profiles using Object-Oriented Programming (OOP) concepts.

---

# Project Overview

Student Placement Tracker is a menu-driven Python application developed to simplify the process of managing placement preparation records. It stores student information such as Student ID, Name, Branch, and Mock Interview Score, and automatically determines each student's placement readiness based on their score.

The project demonstrates core Python OOP concepts including classes, objects, encapsulation, properties, class methods, static methods, and constructors.

---

# Features Implemented

* Add a new student using a comma-separated input.
* Prevent duplicate Student IDs.
* Automatically normalize student names.
* Validate scores between **0 and 100**.
* Update student scores safely using property setters.
* Display placement status automatically.
* Display all student profiles.
* Change platform name for all students.
* Track total number of students using a class variable.
* Menu-driven interface for easy interaction.

---

# Python Concepts Used

This project covers the following Python concepts:

| Concept                | Usage                                                         |
| ---------------------- | ------------------------------------------------------------- |
| Class                  | `StudentProfile`                                              |
| Object                 | Student records                                               |
| Constructor            | `__init__()`                                                  |
| Encapsulation          | Private variable `__score`                                    |
| Property               | `@property` getter                                            |
| Setter                 | `@score.setter`                                               |
| Static Method          | `is_valid_score()`, `normalize_name()`                        |
| Class Method           | `from_string()`, `change_platform()`, `show_total_students()` |
| Class Variable         | `platform`, `total_students`                                  |
| Instance Method        | `display_profile()`, `get_placement_status()`                 |
| Loops                  | Menu system                                                   |
| Conditional Statements | Placement status logic                                        |
| Lists                  | Store student objects                                         |

---

# Placement Status Logic

| Score    | Status              |
| -------- | ------------------- |
| 80 – 100 | Placement Ready     |
| 60 – 79  | Needs More Practice |
| Below 60 | Not Ready           |

---

# Project Structure

```text
Student-Placement-Tracker/
│
├── main.py
└── README.md
```

---

# How to Run the Program

### Step 1

Make sure Python 3 is installed.

Check using:

```bash
python --version
```

### Step 2

Open the project folder.

### Step 3

Run the program.

```bash
python main.py
```

### Step 4

Choose options from the menu.

Example:

```text
===== Student Placement Tracker =====
1. Add Student
2. Display All Students
3. Update Student Score
4. Change Platform
5. Show Total Students
6. Exit
```

---

# Sample Input

```text
Enter student details:
K101,Aarav Sharma,CSE,85
```

---

# Sample Output

```text
Student added successfully.

Student ID: K101
Name: Aarav Sharma
Branch: CSE
Mock Score: 85
Placement Status: Placement Ready
Platform: KodNest
```

---

# Test Result Summary

| Test Case               | Result |
| ----------------------- | ------ |
| Add Student             | Passed |
| Duplicate Student ID    | Passed |
| Score Validation        | Passed |
| Name Normalization      | Passed |
| Update Score            | Passed |
| Placement Status Update | Passed |
| Display Profiles        | Passed |
| Change Platform         | Passed |
| Student Counter         | Passed |
| Exit Program            | Passed |

All required functionalities were tested successfully.

---

# Individual Contribution

* Designed the `StudentProfile` class.
* Implemented encapsulation using a private variable.
* Created property getter and setter for score validation.
* Implemented class methods and static methods.
* Built the menu-driven application.
* Added duplicate Student ID validation.
* Implemented automatic placement status calculation.
* Tested all features.

---

# Code Review Completed

Code was reviewed for:

* Proper OOP implementation.
* Correct use of private variables.
* Input validation.
* Duplicate Student ID handling.
* Menu flow and readability.

---

# Feedback Received

* Improve input validation.
* Prevent duplicate Student IDs.
* Avoid direct access to private variables.
* Display updated placement status immediately after score updates.
* Keep the code organized using methods.

---

# Improvements Made After Review

* Added duplicate Student ID validation.
* Used property setters instead of directly modifying `__score`.
* Improved error handling for invalid input.
* Added automatic name normalization.
* Displayed updated placement status after score updates.
* Improved overall code readability and structure.

---

# Future Improvements

This project can be extended by adding:

* File storage using CSV or JSON.
* SQLite database support.
* Search student by name.
* Delete student records.
* Sort students by score.
* Export reports.
* Graphical User Interface using Tkinter.

---

# Learning Outcome

Through this project, I learned how to build a real-world Python application using Object-Oriented Programming. I gained practical experience with encapsulation, properties, class methods, static methods, validation techniques, and menu-driven program design, making the application more secure, reusable, and maintainable.
