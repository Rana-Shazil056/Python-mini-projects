CREATE DATABASE myfirstdb;
USE myfirstdb;
CREATE table student(
id int primary key,
name VARCHAR(50),
age INT
);
INSERT INTO student
VALUES
(1,'SHAZIL',21),
(2,'Ahmed',22),
(3,'Arfa',23);

SELECT * from student;