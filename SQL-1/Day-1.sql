CREATE DATABASE StudentDatabase;

USE StudentDatabase;

CREATE TABLE Students (
	StudentID INT PRIMARY KEY AUTO_INCREMENT,
	FirstName VARCHAR NOT NULL,
	LastName VARCHAR NOT NULL,
	DateOfBirth DATE,
	Email VARCHAR UNIQUE,
	Phone VARCHAR,
	Course VARCHAR NOT NULL,
	EnrollmentYear INT NOT NULL
);

INSERT INTO Students
	(FirstName, LastName, DateOfBirth, Email, Phone, Course, EnrollmentYear)
VALUES
	('Aarav', 'Sharma', '2005-03-14', 'aarav.sharma@example.com', '9876543210', 'Computer Science', 2024),
	('Diya', 'Patel', '2004-07-22', 'diya.patel@example.com', '9876543211', 'Information Technology', 2023),
	('Kabir', 'Khan', '2005-11-08', 'kabir.khan@example.com', '9876543212', 'Computer Science', 2024),
	('Anaya', 'Singh', '2006-01-30', 'anaya.singh@example.com', '9876543213', 'Business Administration', 2025),
	('Rohan', 'Verma', '2004-09-17', 'rohan.verma@example.com', '9876543214', 'Mechanical Engineering', 2023);

SELECT * FROM Students;
