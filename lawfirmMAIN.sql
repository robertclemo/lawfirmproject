create table employees
(empID serial primary key, Last_Name text not null, First_Name text not null, Title text not null, ReportsTo int, Email text not NULL, username text NOT NULL, pass text NOT null)

insert into employees(Last_Name, First_Name, Title, ReportsTo, Email, username, pass) values
('Summers', 'Arthur', 'Partner', null, 'asummers@gmail.com', 'asummers', 'asummers20'),
('Simmons', 'Brenda', 'HR', 1, 'bsimmons@gmail.com', 'bsimmons', 'bsimmons20'),
('Rolle', 'Bryan', 'Prosecuting_Attorney', 2, 'brolle@gmail.com', 'brolle', 'brolle20'),
('Higgins', 'Christie', 'Divorce_Attorney', 2, 'chiggins@gmail.com', 'chiggins', 'chiggins20'),
('Mitchell', 'Jeffery', 'Tax_Attorney', 2, 'jmitchell@gmail.com', 'jmitchell', 'jmitchell20'),
('Clemo', 'Robert', 'Immigration_Attorney', 2, 'rclemo@gmail.com', 'rclemo', 'rclemo20'),
('Wilson', 'Woody', 'Defense_Attorney', 2, 'wwilson@gmail.com', 'wwilson', 'wwilson20'),
('Goldsmith', 'Lisa', 'Secretary', 2, 'lgoldsmith@gmail.com', 'lgoldsmith', 'lgoldsmith20'),
('Crofton', 'Charles', 'Custodian', 2, 'ccrofton@gmail.com', 'ccrofton', 'ccrofton20')

select * from employees;

drop table employees;
