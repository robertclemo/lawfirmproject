create table staff_credentials(
staff_credential_id serial primary key,
staff_username text not null,
staff_password text not null,
role text not null,
permission text not null
)

select staff_credential_id AS "Credential ID", staff_username AS "Staff Username", staff_password AS "Staff Password", role AS "Role", permission AS "Permission" from staff_credentials

insert into staff_credentials(staff_username, staff_password, role, permission) values 
('Arther_Summers', 'BigAR22', 'Attorney', 'Limited for only Lawyers'),
('Bryan_Rolle', 'Topdog_th3elite', 'Prosecuting_Attorney', 'Limited for only Lawyers'),
('Christie_Higgins', 'C-higgy_44', 'Divorce_Attorney', 'Limited for only Lawyers'),
('Jeffery_Mitchell', 'JM_thestar', 'Tax_Attorney', 'Limited for only Lawyers' ),
('Robert_Clemo', 'Clemo_the_Limo', 'Immigration_Attorney', 'Limited for only Lawyers'),
('Woody_Wilson', 'ToyStory9000', 'Defense_Attorney', 'Limited for only Lawyers'),
('Brenda_Simmons', 'Brenda-the-Blenda', 'HR', 'Nearly all permissions, is not owner'),
('Lisa_Goldsmith', 'Lisa_Alisa', 'Secretary', 'Limited for only Secretaries'),
('Charles_Crofton', 'CC_nocopyright', 'Custodian', 'Basically none, only has access to the building')


select * from staff_credentials 

drop table staff_credentials 