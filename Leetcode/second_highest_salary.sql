-- Table: Employee

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- id is the primary key column for this table.
-- Each row of this table contains information about the salary of an employee.
 
-- Write an SQL query to report the second highest salary from the Employee table.
-- If there is no second highest salary, the query should report null.

select (
    select distinct salary
    from Employee
    order by salary desc
    limit 1
    offset 1
) as SecondHighestSalary
