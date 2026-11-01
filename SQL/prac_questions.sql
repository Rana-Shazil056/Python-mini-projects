-- Active: 1792704254332@@127.0.0.1@3306@student_db

CREATE DATABASE IF NOT EXISTS ai_platform;
USE ai_platform;

-- Drop existing tables
DROP TABLE IF EXISTS ai_logs;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS plans;

-- 1. Create Plans Table
CREATE TABLE plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(50) NOT NULL,
    monthly_price DECIMAL(10,2) NOT NULL
);

-- 2. Create Users Table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    plan_id INT,
    country VARCHAR(50) NOT NULL,
    created_at DATE NOT NULL,
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id) ON DELETE SET NULL
);

-- 3. Create AI Logs Table
CREATE TABLE ai_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    prompt TEXT NOT NULL,
    tokens_used INT NOT NULL,
    response_metadata JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Insert Subscription Plans
INSERT INTO plans (plan_name, monthly_price) VALUES
('Free', 0.00),
('Pro', 20.00),
('Enterprise', 100.00);

-- Insert Users
INSERT INTO users (name, email, plan_id, country, created_at) VALUES
('Aarav Sharma', 'aarav@example.com', 2, 'India', '2025-01-15'),
('Zeynep Yilmaz', 'zeynep@example.com', 1, 'Turkey', '2025-02-01'),
('Rana Shazil', 'rana@example.com', 3, 'Pakistan', '2025-02-10'),
('Elena Rostova', 'elena@example.com', 2, 'Germany', '2025-02-20'),
('Carlos Mendez', 'carlos@example.com', NULL, 'Spain', '2025-03-01'),
('Sarah Jenkins', 'sarah@example.com', 1, 'USA', '2025-03-05');

-- Insert AI Interaction Logs
INSERT INTO ai_logs (user_id, prompt, tokens_used, response_metadata) VALUES
(1, 'Summarize this PDF report', 350, '{"model": "gpt-4o", "latency_ms": 1200, "status": "success"}'),
(1, 'Translate to French', 120, '{"model": "gpt-3.5-turbo", "latency_ms": 450, "status": "success"}'),
(3, 'Build a SQL query for vector search', 850, '{"model": "gpt-4o", "latency_ms": 2100, "status": "success"}'),
(3, 'Debug my Python code', 600, '{"model": "gpt-4o", "latency_ms": 1800, "status": "success"}'),
(2, 'Write an email to my manager', 200, '{"model": "gpt-3.5-turbo", "latency_ms": 600, "status": "success"}'),
(4, 'Generate a JSON schema', 450, '{"model": "gpt-4o", "latency_ms": 1100, "status": "success"}'),
(1, 'Explain neural networks', 500, '{"model": "gpt-4o", "latency_ms": 1400, "status": "success"}');


--1 task 1
SELECT name , email ,plan_name FROM users
LEFT JOIN
plans
on user_id=plan_id;

SELECT * from users;
SELECT * from ai_logs;
SELECT users.name, users.email, users.country, ai_logs.prompt 
FROM users left JOIN ai_logs
on users.user_id=ai_logs.user_id;



-- doing again
use ai_platform;
drop table if exists department;
drop table if exists user;
CREATE table department (
dept_id int primary key AUTO_INCREMENT,
dept_name varchar(100)
);
CREATE table user(
    id int PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    dept_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (dept_id) REFERENCES department(dept_id) ON DELETE SET NULL
);

-- Insert Departments
INSERT INTO department (dept_id, dept_name) VALUES
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'Human Resources'),
(4, 'Finance'); -- (Notice: No employees will belong to Finance)

-- Insert Employees
INSERT INTO user (name, salary, dept_id) VALUES
('Aarav Sharma', 75000.00, 1),   -- Engineering
('Zeynep Yilmaz', 62000.00, 2),  -- Marketing
('Rana Shazil', 95000.00, 1),   -- Engineering
('Elena Rostova', 58000.00, 3),  -- Human Resources
('Carlos Mendez', 50000.00, NULL); -- (Notice: Carlos has NO department)

select  * from user;
SELECT user.name,user.salary,department.dept_id,department.dept_name from user
INNER join department
on department.dept_id=user.id;


-- prac q
use ai_platform;
drop table if exists developers;
DROP table if exists ai_models;

CREATE Table developers
(
    dev_id int AUTO_INCREMENT PRIMARY KEY ,
    dev_name VARCHAR(100),
    role varchar(100)
);

INSERT INTO developers (dev_id,dev_name,role) VALUES
    (1,'Rana Shazil', 'AI Engineer'),
    (2,'Aarav Sharma', 'Data Scientist'),
    (3,'Zeynep Yilmaz', 'MLOps Engineer'),
    (4,'Elena Rostova', 'Software Engineer');
CREATE Table ai_models(
    mo_id int AUTO_INCREMENT PRIMARY KEY,    --child table
    mo_name VARCHAR(100),
    framework VARCHAR(100),
    dev_id INT,
    constraint fk_user FOREIGN KEY (dev_id) REFERENCES developers(dev_id) on delete CASCADE
);
INSERT into ai_models(mo_id,mo_name,framework,dev_id) VALUES
(1,'GPT-Custom-v1', 'PyTorch',1 ),

(2,'Vision-Net-3D', 'TensorFlow', 2 ),

(3,'LLM-FineTune-7B', 'PyTorch', 1 ),

(4,'BERT-Classifier', 'PyTorch', 3),

(5,'Auto-Chatbot', 'LangChain', NULL);
select * from developers;

SELECT * from ai_models;

--now inner join using my rule
--child.foriegn key = parent. primary KEY

SELECT developers.dev_id,developers.dev_name,developers.role,ai_models.mo_name,ai_models.framework
from developers 
inner JOIN
ai_models
ON ai_models.dev_id=developers.dev_id;

--left join
SELECT developers.dev_id,developers.dev_name,developers.role,ai_models.mo_name,ai_models.framework
from developers 
left JOIN
ai_models
on ai_models.dev_id=developers.dev_id;

--    or
SELECT d.dev_id,d.dev_name,d.role,m.mo_name,m.framework,COUNT(d.dev_id) as TOTAL 
from developers d
LEFT JOIN
ai_models m
on m.dev_id=d.dev_id GROUP BY d.dev_id , d.dev_name;

--task
use ai_platform;
drop table if exists stud;
drop table if exists sports;

create table stud(
    stud_id int AUTO_INCREMENT PRIMARY KEY,
    stud_name VARCHAR(100)
);
CREATE table sports (
    sp_id int PRIMARY KEY,
    sp_name VARCHAR(100),
    stud_id int,
    FOREIGN key (stud_id) REFERENCES stud(stud_id)
);
insert into stud VALUES
(1, 'Ali'),
(2, 'Sara'),
(3, 'Rana'); -- (Notice: Rana plays NO sports)

-- Insert 2 Sports
INSERT INTO sports VALUES
(101, 'Cricket', 1),   -- Ali plays Cricket
(102, 'Football', 2);

--inner join
select * from stud 
inner JOIN
sports
ON sports.stud_id=stud.stud_id;

--left join 
select * from stud
left join 
sports
on sports.stud_id=stud.stud_id;

--Right join
select * from stud
Right join 
sports
on sports.stud_id=stud.stud_id;