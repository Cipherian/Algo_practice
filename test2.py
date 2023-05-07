"""
Problem Statement
You are given a list of student records, where each record contains the following information:

student ID (an integer)
student name (a string)
student GPA (a float)
Write a program that implements the following operations:

add_student(id: int, name: str, gpa: float) - adds a new student record to the list
delete_student(id: int) - deletes the student record with the given ID from the list
update_gpa(id: int, gpa: float) - updates the GPA of the student with the given ID
get_top_students(num: int) -> List[Tuple[int, str, float]] - returns the top num students based on GPA, sorted in descending order
Your program should store the student records in a SQLite database.

Solution
To solve this problem, we'll define a StudentDB class that will interact with the database. The class will have methods to perform the operations specified in the problem statement. We'll use the sqlite3 module to interact with the database.
"""

import sqlite3
import unittest
from typing import List, Tuple

class StudentDB:
    def __init__(self, db_file: str):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY, name TEXT, gpa REAL)
        ''')

    def add_student(self, id: int, name: str, gpa: float):
        self.cursor.execute('''
            INSERT INTO students (id, name, gpa)
            VALUES (?, ?, ?)
        ''', (id, name, gpa))
        self.conn.commit()

    def delete_student(self, id: int):
        self.cursor.execute('''
            DELETE FROM students WHERE id = ?
        ''', (id,))
        self.conn.commit()

    def update_gpa(self, id: int, gpa: float):
        self.cursor.execute('''
            UPDATE students SET gpa = ? WHERE id = ?
        ''', (gpa, id))
        self.conn.commit()

    def get_top_students(self, num: int) -> List[Tuple[int, str, float]]:
        self.cursor.execute('''
            SELECT id, name, gpa FROM students ORDER BY gpa DESC LIMIT ?
        ''', (num,))
        return self.cursor.fetchall()


import sqlite3
from typing import List, Tuple

class StudentDB:
    def __init__(self, db_file: str):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY, name TEXT, gpa REAL)
        ''')

    def add_student(self, id: int, name: str, gpa: float):
        self.cursor.execute('''
            INSERT INTO students (id, name, gpa)
            VALUES (?, ?, ?)
        ''', (id, name, gpa))
        self.conn.commit()

    def delete_student(self, id: int):
        self.cursor.execute('''
            DELETE FROM students WHERE id = ?
        ''', (id,))
        self.conn.commit()

    def update_gpa(self, id: int, gpa: float):
        self.cursor.execute('''
            UPDATE students SET gpa = ? WHERE id = ?
        ''', (gpa, id))
        self.conn.commit()

    def get_top_students(self, num: int) -> List[Tuple[int, str, float]]:
        self.cursor.execute('''
            SELECT id, name, gpa FROM students ORDER BY gpa DESC LIMIT ?
        ''', (num,))
        return self.cursor.fetchall()




class TestStudentDB(unittest.TestCase):
    def setUp(self):
        self.db_file = ':memory:'
        self.db = StudentDB(self.db_file)

    def test_add_student(self):
        self.db.add_student(1, 'Alice', 3.5)
        self.db.add_student(2, 'Bob', 3.2)
        self.assertEqual(self.db.get_top_students(2), [(1, 'Alice', 3.5), (2, 'Bob', 3.2)])

    def test_delete_student(self):
        self.db.add_student(1, 'Alice', 3.5)
        self.db.add_student(2, 'Bob', 3.2)
        self.db


if __name__ == '__main__':
    unittest.main()