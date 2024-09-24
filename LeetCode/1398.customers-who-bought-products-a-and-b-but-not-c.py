/* 
Problem Statement:
------------------
You are given a table `Customer` that contains customer purchase records. 
Write an SQL query to find the customers who bought both products 'A' and 'B' 
but did not buy product 'C' during the same purchase session.

Table Structure:

Customer:
---------
| Column Name | Type    |
|-------------|---------|
| customer_id | int     |
| product     | varchar |

- `customer_id` is the customer's unique identifier.
- `product` is the name of the product purchased by the customer.

Write a query to return the list of customers who bought both product 'A' and 'B' but did not purchase product 'C'. The result should be in ascending order of `customer_id`.

Expected Output:
----------------
| customer_id |
|-------------|
| 3           |

Example:
--------
Let's assume the `Customer` table contains the following records:

| customer_id | product |
|-------------|---------|
| 1           | A       |
| 1           | B       |
| 1           | D       |
| 1           | C       |
| 2           | A       |
| 2           | B       |
| 2           | D       |
| 3           | A       |
| 3           | B       |

- Customer 1 bought products 'A', 'B', and 'C', so they are not included in the result.
- Customer 2 bought products 'A', 'B', and 'D', but also bought 'C', so they are not included.
- Customer 3 bought products 'A' and 'B' but did not buy product 'C', so they should be included in the result.

Instructions:
-------------
- Provide DROP, CREATE, and INSERT statements for setting up the environment.
- Do not include the solution in the file unless explicitly asked.

*/

-- Drop the Customer table if it already exists
DROP TABLE IF EXISTS Customer;

-- Create the Customer table
CREATE TABLE Customer (
    customer_id INT,
    product VARCHAR(255)
);

-- Insert sample data into the Customer table
INSERT INTO Customer (customer_id, product) VALUES
(1, 'A'),
(1, 'B'),
(1, 'D'),
(1, 'C'),
(2, 'A'),
(2, 'B'),
(2, 'D'),
(3, 'A'),
(3, 'B');

-- Expected output based on the sample data
-- | customer_id |
-- |-------------|
-- | 3           |



--SOLUTIONS

select customer_id from customer
where product in ('A', 'B')
group by customer_id
having count(distinct product) = 2
and customer_id not in 
(select customer_id from customer where product = 'C');


-- OR USING JOIN

SELECT DISTINCT c1.customer_id
FROM Customer c1
JOIN Customer c2 ON c1.customer_id = c2.customer_id
LEFT JOIN Customer c3 ON c1.customer_id = c3.customer_id AND c3.product = 'C'
WHERE c1.product = 'A' 
  AND c2.product = 'B'
  AND c3.customer_id IS NULL;
