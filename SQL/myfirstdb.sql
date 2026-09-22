CREATE DATABASE IF NOT EXISTS myfirstdb;
USE myfirstdb;
DROP TABLE if EXISTS student;
CREATE TABLE student(
id int primary key,
name VARCHAR(50),
age INT
);
INSERT INTO student
VALUES
(1,'SHAZIL',21),
(2,'Ahmed',22),
(3,'aba',225),
(4,'ali',24),
(5,'Arfa',23);

SELECT * FROM student ORDER BY id;

DROP TABLE if EXISTS hospital;
CREATE TABLE hospital(
  id int PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  age INT
);
INSERT into hospital
VALUES
(1,'Ali',30),
(2,'AHmed',35),
(4,'Arshuman',50);
-- DELETE FROM hospital;
SELECT * FROM hospital where age >35;
SELECT * FROM hospital ORDER BY id;


Create Table Sales
(
  Salesid INT Primary key,
  cstname VARCHAR(10),
  ItemBUY VARCHAR(10),
  Amount Decimal(10,2)
);
Insert into Sales Values
(1,'Shazil','Eggs',10),
(2,'ali','chick',20),
(3,'hira','beef',30);
Select 
Sum (Amount) as TotalRevenue,
Count(1) as TotalTransactions
from Sales;


