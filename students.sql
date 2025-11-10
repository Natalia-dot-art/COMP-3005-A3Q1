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

-- table created and values added