--Doing some functions
DROP table if exists Students;
CREATE table Students(
    id int PRIMARY key,
    name VARCHAR(50),
    age int ,
    marks FLOAT
);
INSERT INTO Students values
(1,'shazil',21,88),
(2,'Ahmed',22,66),
(3,'aba',22,77),
(4,'ali',13,88),
(5,'Arfa',23,01);
 
SELECT * FROM students

select COUNT(*) from students;

SELECT SUM(marks) from students;
select AVG(marks) FROM students  group by marks;
SELECT MAX(marks);

SELECT age, COUNT(*) FROM students GROUP BY age;

select AVG(marks) from students WHERE age > 21;

select age ,marks from students ORDER BY marks DESC