/*
Problem Statement:

LeetCode Problem 1112: Highest Grade For Each Student

We have a table `Students` that contains the following columns:
- `student_id` (int) : Unique identifier for each student.
- `name` (varchar) : Name of the student.

We also have a table `Subjects` that contains the following columns:
- `subject_name` (varchar) : Name of the subject.

Finally, there is a table `Grades` that tracks the grades for each student in various subjects. It contains the following columns:
- `student_id` (int) : Refers to the student from the Students table.
- `subject_name` (varchar) : Refers to the subject from the Subjects table.
- `grade` (decimal) : The grade the student received in the subject.

Your task is to create an SQL query that retrieves each student's highest grade in any subject. If a student has not received any grades, that student should not appear in the result.

Table Definitions:
1. Students: Stores student information.
   Columns:
   - student_id (int): Unique identifier for each student.
   - name (varchar): Name of the student.

2. Subjects: Stores subject information.
   Columns:
   - subject_name (varchar): Name of the subject.

3. Grades: Tracks grades received by students.
   Columns:
   - student_id (int): Refers to the student from the Students table.
   - subject_name (varchar): Refers to the subject from the Subjects table.
   - grade (decimal): The grade received by the student.

Input:
- The `Students` table with student details.
- The `Grades` table with each student's grades.
- The `Subjects` table with the subject names.

Expected Output:
- A result set showing each student's highest grade in any subject.

*/

-- Drop tables if they already exist
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Subjects;
DROP TABLE IF EXISTS Grades;

-- Create Students table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- Create Subjects table
CREATE TABLE Subjects (
    subject_name VARCHAR(50) PRIMARY KEY
);

-- Create Grades table
CREATE TABLE Grades (
    student_id INT,
    subject_name VARCHAR(50),
    grade DECIMAL(4, 2),
    PRIMARY KEY (student_id, subject_name),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_name) REFERENCES Subjects(subject_name)
);

-- Insert sample data into Students table
INSERT INTO Students (student_id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

--
