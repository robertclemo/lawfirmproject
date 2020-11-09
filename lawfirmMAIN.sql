
drop table staff

______

create table staff
(empID serial primary key, fname text not null, lname text not null, email text not null, specialty text not null, department text not null)

select empID AS "Employee ID", fname AS "First Name", lname AS "Last Name", email AS "Email", specialty AS "Specialty", department AS "Department" from staff

insert into staff(fname, lname, email, specialty, department) values
('Arthur', 'Summers', 'asummers@lawfirm.com', 'Attorney', 'Lawyer'),
('Bryan', 'Rolle', 'brolle@lawfirm.com', 'Prosecuting_Attorney', 'Lawyer'),
('Christie', 'Higgins', 'chiggins@lawfirm.com', 'Divorce_Attorney', 'Lawyer'),
('Jeffery', 'Mitchell', 'jmitchell@lawfirm.com', 'Tax_Attorney', 'Lawyer'),
('Robert', 'Clemo', 'rclemo@lawfirm.com', 'Immigration_Attorney', 'Lawyer'),
('Woody', 'Wilson', 'wwilson@lawfirm.com', 'Defense_Attorney', 'Lawyer'),
('Brenda', 'Simmons', 'bsimmons@lawfirm.com', 'Staff', 'HR'),
('Lisa', 'Goldsmith', 'lgoldsmith@lawfirm.com', 'Staff', 'Secretary'),
('Charles', 'Crofton', 'ccrofton@lawfirm.com', 'Staff', 'Custodian')

drop table staff