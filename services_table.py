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

def displayServices():
    system('cls')
    tableName = "services"

    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM services')
        for row in cursor:
            print(f'''
            Service..... {row[1]}
            Description ..... {row[2]}
            Price per hour..... {row[3]}
            ''')
        cursor.close()
        conn.close()
    except(Exception, mysql.connector.Error) as error:
            print('Error while fetching data from MySQL', error)

displayServices()


# SQL COMMANDS


# create table services(
#     serv_name text not null,
#     serv_desc text not null,
#     serv_price int not null
# )

# INSERT INTO services (serv_name, serv_desc, serv_price) values 
# ('Tax Attorney', 'Back taxes, Unified returns, Halt wage garnishments, Leins and Levies, IRS Compromises', 200 ),
# ('Defence Attorney', 'Defense of individuals and companies charged with criminal activity.', 150),
# ('Deivorce Attorney', 'Division of assets, debt among spouses, child custody, and legal separations', 450 ),
# ('Prosecuting Attorney', 'Represent local, state, or federal governments in criminal court cases. In addition to trying cases,', 2000),
# ('Bankruptcy',  'Assist clients through court proceedings to reduce or eliminate debt or to proceed forward with bankruptcy.', 500)
