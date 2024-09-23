-- LeetCode Problem 183 - "Customers Who Never Order"

-- Description:
-- Write an SQL query to find all customers who never placed an order.

-- Input:
-- Two tables, "Customers" and "Orders", are given.

-- Table: Customers
-- +----+---------+
-- | id | name    |
-- +----+---------+
-- | 1  | Alice   |
-- | 2  | Bob     |
-- | 3  | Charlie |
-- | 4  | David   |
-- +----+---------+

-- Table: Orders
-- +----+------------+
-- | id | customerId |
-- +----+------------+
-- | 1  | 1          |
-- | 2  | 3          |
-- +----+------------+

-- Output:
-- The query should return the following result:
-- +-------+
-- | name  |
-- +-------+
-- | Bob   |
-- | David |
-- +-------+

-- Explanation:
-- Bob and David are customers who did not place any orders in the "Orders" table.

-- Drop the Orders and Customers tables if they already exist
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;

-- Create the Customers table
CREATE TABLE Customers (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Create the Orders table
CREATE TABLE Orders (
    id INT PRIMARY KEY,
    customerId INT,
    FOREIGN KEY (customerId) REFERENCES Customers(id)
);

-- Insert sample data into the Customers table
INSERT INTO Customers (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David');

-- Insert sample data into the Orders table
INSERT INTO Orders (id, customerId) VALUES
(1, 1),
(2, 3);



-- SOLUTION -

SELECT name 
FROM Customers c
WHERE c.id NOT IN 
(SELECT customerId FROM Orders);
