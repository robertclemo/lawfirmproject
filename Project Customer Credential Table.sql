create table customer_credential(
customer_credential_id serial primary key,
customer_username text not null,
customer_password text not null,
role text not null,
permission text not null
)

select customer_credential_id as "Customer ID", customer_username as "Customer Username", customer_password as "Customer Password", role as "Role", permission as "Permission" from customer_credential

insert into customer_credential(customer_username, customer_password, role, permission) values
('John_Mitchell', 'JJ_Mitch-theman', 'Customer', 'Can view profile and delete profile'),
('Darlene_Phifer', 'Dar-Phif3r', 'Customer', 'Can view profile and delete profile'),
('Claudette_Legans', 'C-Legans23', 'Customer', 'Can view profile and delete profile'),
('Valerie_Smith', 'Val_Smitty', 'Customer', 'Can view profile and delete profile'),
('Kim_Lumpkins', 'Kim_Possible56', 'Customer', 'Can view profile and delete profile')

select * from customer_credential 

drop table customer_credential

