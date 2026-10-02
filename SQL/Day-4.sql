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
ALTER Table staff_members RENAME column name to emp_name;

alter table employee MODIFY department VARCHAR(2) to VARCHAR(3);   --prac

-- add column
alter table employee ADD column joining_date DATE DEFAULT(CURRENT_TIME);

-- Rename employee table to staff_members
RENAME TABLE employee to staff_members;

--Delete table salary
alter TABLE employee DROP COLUMN salary;

-- alter table column name and its datatype
alter table staff_members change column name emp_name varchar(100);

SELECT * FROM employee;
show TABLES;
drop table staff_members;

drop Table students;

SELECT * from staff_members;

alter table staff_members modify COLUMN department varchar(2) emp_name;

alter Table staff_members modify emp_name VARCHAR(50) first;
