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

CREATE TABLE hospital(
  id int PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  age INT
);
INSERT into hospital
VALUES
(1,'Ali',30),
(2,'AHmed',35),
(3,'arfa',40);

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


