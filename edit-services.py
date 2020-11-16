import mysql.connector
import os
from os import system
from mysql.connector import connect


conn = connect( 
    user = "root",
    password = "buttbutt",
    host = "127.0.0.1",
    database =  "nci_db"   
)

def displayServices():
    system('cls')
    tableName = "services"
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM services"
        )
        rows = cursor.fetchall()
        print
        if(rows):
            print('Service Information')
            print
            for row in rows:
                print(f'''
                Service:........................ {row[0]}
                Description:.................... {row[1]}
                Price per hour:................. ${row[2]}
                ''')
            cursor.close()
        else:
            print('Your database is empty. Try adding some rows.')

    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)
    
displayServices()

def insertServiceTable():
    tableName = "services"
    count = int(input("How many services do you wish to add? >> "))
    cursor = conn.cursor()
    for i in range(count):
       print(f'Please fill out the following for service {i+1}: >> ')
       servname = str(input("What is the service name? >> "))
       servdesc = str(input("Describe the service >> "))
       servprice = int(input("Please enter a price per hour >> "))
       cursor.execute(
           f"INSERT INTO services (serv_name, serv_desc, serv_price) values ('{servname}', '{servdesc}', '{servprice}')")
       conn.commit()
       cursor = conn.cursor()
       displayServices()
insertServiceTable()

def removeServiceTable():
    tableName = "services"
    count = int(input("how many services do you want to remove? >> "))
    cursor = conn.cursor()
    for i in range(count):
        remoserv = str(input("what service would you like to remove? >> "))
        cursor.execute(
        f"DELETE FROM services WHERE serv_name = '{remoserv}'")
        conn.commit()
        cursor = conn.cursor()

    displayServices()
removeServiceTable()