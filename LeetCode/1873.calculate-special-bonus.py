-- LeetCode Problem 1873 - "Calculate Special Bonus"

-- Description:
-- Write an SQL query to calculate the bonus of each employee.
-- The bonus of an employee is:
-- - 100% of their salary if their employee_id is odd and their name does not start with the letter 'M'.
-- - Otherwise, the bonus is 0.

-- Input:
-- One table, "Employees", is given.

-- Table: Employees
-- +-------------+---------+--------+
-- | employee_id | name    | salary |
-- +-------------+---------+--------+
-- | 1           | Alice   | 5000   |
-- | 2           | Bob     | 3000   |
-- | 3           | Charlie | 7000   |
-- | 4           | Mandy   | 6000   |
-- | 5           | David   | 4000   |
-- +-------------+---------+--------+

-- Output:
-- The query should return the following result:
-- +-------------+-------+
-- | employee_id | bonus |
-- +-------------+-------+
-- | 1           | 5000  |
-- | 2           | 0     |
-- | 3           | 7000  |
-- | 4           | 0     |
-- | 5           | 4000  |
-- +-------------+-------+

-- Explanation:
-- - Employee 1 (Alice) gets a bonus because their employee_id is odd and their name doesn't start with 'M'.
-- - Employee 3 (Charlie) gets a bonus because their employee_id is odd and their name doesn't start with 'M'.
-- - Employee 5 (David) gets a bonus because their employee_id is odd and their name doesn't start with 'M'.
-- - Employee 2 (Bob) doesn't get a bonus because their employee_id is even.
-- - Employee 4 (Mandy) doesn't get a bonus because their name starts with 'M'.

-- Drop the Employees table if it already exists
DROP TABLE IF EXISTS Employees;

-- Create the Employees table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(255),
    salary INT
);

-- Insert sample data into the Employees table
INSERT INTO Employees (employee_id, name, salary) VALUES
(1, 'Alice', 5000),
(2, 'Bob', 3000),
(3, 'Charlie', 7000),
(4, 'Mandy', 6000),
(5, 'David', 4000);




--- Solution ---

SELECT 
    employee_id,
    name,
    salary,
    CASE 
        WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
        ELSE 0
    END AS bonus
FROM employees;

