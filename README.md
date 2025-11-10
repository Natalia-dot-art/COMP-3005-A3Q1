# COMP-3005-A3Q1 

Natalia Gomez 
Assignment 3
COMP 3005
101256528

How to compile A3Q1.py? Type in terminal where the script is located: python A3Q1.py

The program will prompt you to select 1 out of 5 options:

1) get all students 
2) add a student 
3) update student email 
4) delete student 
5) exit

PostgreSQL Code used to create and populate the Students table:

CREATE TABLE  students (

	student_id 		serial       Primary Key,
	first_name 		varchar(255) Not Null,
	last_name  		varchar(255) Not Null,
	email           varchar(255) Not Null Unique,
	enrollment_date Date
	);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');