-- Active: 1790453436125@@127.0.0.1@3306@student_db
CREATE DATABASE IF NOT EXISTS student_db;

USE student_db;

DROP TABLE IF EXISTS employee;

CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    department VARCHAR(2)
);

INSERT INTO employee
(id, name, salary, department)
VALUES
(1,'Shazil',20000,'IT'),
(2,'Moiz',30000,'HR');

--now change the name to emp_name
ALTER Table employee RENAME column name to emp_name;

alter table employee MODIFY department VARCHAR(2) to VARCHAR(3);

-- add column
alter table employee ADD column joining_date DATE DEFAULT(CURRENT_TIME);
SELECT * FROM employee;


