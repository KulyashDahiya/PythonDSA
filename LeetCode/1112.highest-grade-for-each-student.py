/*
-- Problem Statement:
LeetCode Problem 1112: Highest Grade for Each Student in Each Subject

You are given three tables: `Students`, `Subjects`, and `ExamResults`. 
Your task is to find the highest grade of each student for each subject. 
The results should include the student's name, subject name, and the highest grade the student received for that subject.


-- Expected Output:
The output should contain the following columns:
- `student_name`: The name of the student.
- `subject_name`: The name of the subject.
- `grade`: The highest grade that the student received for the subject.

-- Example:
Input:
Students:
+------------+--------------+
| student_id | student_name  |
+------------+--------------+
| 1          | Alice         |
| 2          | Bob           |
| 3          | Charlie       |
+------------+--------------+

Subjects:
+------------+--------------+
| subject_id | subject_name  |
+------------+--------------+
| 1          | Math          |
| 2          | Science       |
+------------+--------------+

ExamResults:
+------------+------------+-------+
| student_id | subject_id | grade |
+------------+------------+-------+
| 1          | 1          | 90    |
| 1          | 1          | 85    |
| 1          | 2          | 88    |
| 2          | 1          | 78    |
| 2          | 2          | 80    |
| 3          | 1          | 92    |
| 3          | 2          | 91    |
+------------+------------+-------+


-- Expected Output:
+--------------+--------------+-------+
| student_name | subject_name  | grade |
+--------------+--------------+-------+
| Alice        | Math          | 90    |
| Alice        | Science       | 88    |
| Bob          | Math          | 78    |
| Bob          | Science       | 80    |
| Charlie      | Math          | 92    |
| Charlie      | Science       | 91    |
+--------------+--------------+-------+
*/


-- Solution:

select
	student_name,
    subject_name,
    grade
from (
	select s.student_name, sj.subject_name, e.grade, row_number() over(partition by e.student_id, e.subject_id order by grade desc) as rn
    from students s
	join examresults e
	on s.student_id = e.student_id
	join subjects sj
	on e.subject_id  = sj.subject_id
    ) as rnd
where rn = 1;
