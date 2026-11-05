use startersql;
show tables;
SELECT * FROM `user`;
CREATE TABLE if NOT exists user(
    id int AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    gender ENUM('Male','Female','Other'),
    date_of_birth DATE,
    salary DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
DELIMITER $$
CREATE PROCEDURE Add_user(
IN p_name VARCHAR(100),
IN p_email VARCHAR(100),
In p_gender ENUM('Male','Female','Other')
)
Begin
INSERT into user(name,email,gender)VALUES
(p_name,p_email,p_gender);
SELECT * from user;
END $$
DELIMITER ;
drop PROCEDURE `Add_user`;
Call Add_user('Rana','Rana@Shazil.com','Male');
