Student Record Manager

A simple Python-based Student Record Manager that uses file handling to store and manage student information.

Features
Add new students
View all student records
Search for a student by name
Delete a student using their ID
Update student information
Store student records in a text file
Handle invalid user input using exception handling
Student Record Format

Each student is stored in students.txt in the following format:

Student ID,Name,Marks

Example:

101,Karthik,85
102,Rahul,72
103,Arun,91
Concepts Used
Python functions
Conditional statements
While loops
Match-case
User input
Lists
String methods
File handling
File modes (r, w, a)
read()
readlines()
write()
writelines()
Exception handling
try and except
raise
List traversal
Basic CRUD operations
Project Structure
student-record-manager/
│
├── main.py
├── student.py
├── students.txt
└── README.md
main.py

Contains the main menu and handles user interaction.

student.py

Contains the functions for adding, viewing, searching, deleting, and updating student records.

students.txt

Stores the student records.

How to Run

Make sure Python is installed on your system.

Run the following command in the project directory:

python main.py

Then use the menu displayed in the terminal to manage student records.

Purpose

This project was created as a Python practice project to learn and apply file handling, functions, CRUD operations, loops, string manipulation, and exception handling.