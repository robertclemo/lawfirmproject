# create table customer
# (
# customer_id serial primary key,
# customer_firstname text not null,
# customer_lastname text not null,
# customer_phone text not null,
# customer_address text not null,
# customer_email text not null
# )
# insert into customer(customer_firstname, customer_lastname, customer_phone, customer_address, customer_email) values
# ('John', 'Mitchell', '1233456789', '55 Wells St', 'December@gmail.com'),
# ('Darlene', 'Phifer', '1235678901', '204 Valley Lane', 'March18@gmail.com'),
# ( 'Claudette', 'Legans', '1236789012', '190 Remember Ave', 'Janury@gmail.com'),
# ('Valerie', 'Smith', '1237890123', '400 Vermont Cir', 'February@gmail.com'),
# ('Kim', 'Lumpkins', '1238901234', '567 Piedmont Rd', 'September@gmail.com')
# select * from customer
import mysql.connector
import os
from os import system
from mysql.connector import connect
conn = connect(
    user = "",
    password="",
    host= "",
    database = ""
)
#except mysql.connector.Error as err:
   # print(‘Error connecting to DB’)
def displaycustomer():
    system('cls')
    tableName = "customer"
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customer')
        for row in cursor:
            print(f'''
            customer id......{row[0]}
            first name.......{row[1]}
            last name........{row[2]}
            phone............{row[3]}
            address..........{row[4]}
            email............{row[5]}
            ''')
        cursor.close()
        conn.close()
    except(Exception, mysql.connector.Error) as error:
            print('Error while fetching data from MySQL', error)
displaycustomer()
