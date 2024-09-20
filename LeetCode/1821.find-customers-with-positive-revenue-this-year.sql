-- LeetCode Problem 1821 - "Find Customers With Positive Revenue this Year"

-- Description:
-- Write an SQL query to find the customer_id of customers who have a positive revenue for the year 2021.

-- Input:
-- One table, "Customer", is given.

-- Table: Customer
-- +--------------+------+
-- | customer_id  | year | revenue |
-- +--------------+------+
-- | 1            | 2020 | 1000    |
-- | 1            | 2021 | 7000    |
-- | 2            | 2021 | -200    |
-- | 3            | 2020 | 500     |
-- | 3            | 2021 | 300     |
-- +--------------+------+

-- Output:
-- The query should return the following result:
-- +--------------+
-- | customer_id  |
-- +--------------+
-- | 1            |
-- | 3            |
-- +--------------+

-- Explanation:
-- Customers with customer_id 1 and 3 have a positive revenue in the year 2021.

-- Drop the Customer table if it already exists
DROP TABLE IF EXISTS Customer;

-- Create the Customer table
CREATE TABLE Customer (
    customer_id INT,
    year INT,
    revenue INT
);

-- Insert sample data into the Customer table
INSERT INTO Customer (customer_id, year, revenue) VALUES
(1, 2020, 1000),
(1, 2021, 7000),
(2, 2021, -200),
(3, 2020, 500),
(3, 2021, 300);

-- Query to find customers with positive revenue in the year 2021
-- The query should return the customer_id from the Customer table where the year is 2021 and the revenue is positive.

-- SELECT customer_id
-- FROM Customer
-- WHERE year = 2021 AND revenue > 0;
