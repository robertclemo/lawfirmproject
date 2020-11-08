import mysql.connector
import os
from os import system
import colorama
from colorama import Fore, Style


firmdb = mysql.connector.connect(
    host="myproject-database.cipvfz3qjhug.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Phipsy1!",
    database="myproject_DB"
)

def displayStaff():
    system('cls')
    tableName = "staff"
    try:
        mycursor = firmdb.cursor()
        mycursor.execute(
            f"SELECT * FROM {tableName} ORDER BY empID"
        )
        rows = mycursor.fetchall()
        print(Style.RESET_ALL)
        if(rows):
            print(Fore.CYAN, 'Staff Information: ')
            print(Style.RESET_ALL)
            for row in rows:
                print(f'''{Fore.RED}
                Employee ID:.....................{Style.RESET_ALL}{Fore.BLUE}{row[0]}{Fore.WHITE}
                First Name:......................{Style.RESET_ALL}{Fore.BLUE}{row[1]}{Fore.WHITE}
                Last Name:.......................{Style.RESET_ALL}{Fore.BLUE}{row[2]}{Fore.WHITE}
                Email:...........................{Style.RESET_ALL}{Fore.BLUE}{row[3]}{Fore.WHITE}
                Specialty:.......................{Style.RESET_ALL}{Fore.BLUE}{row[4]}{Fore.WHITE}
                Department:......................{Style.RESET_ALL}{Fore.BLUE}{row[5]}{Fore.WHITE}
                ''')
            mycursor.close()
        else:
            print('Your database is empty. Try adding some rows.')

    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)
    
displayStaff()

def insertStaffTable():
    tableName = "staff"
    count = int(input("How many staff members do you wish to add? >> "))
    cursor = firmdb.cursor()
    for i in range(count):
        print(f'Please fill out the following for the {i+1} staff member: >> ')
        fname = str(input("Staff First Name >> "))
        lname = str(input("Staff Last Name >> "))
        email = str(input("Staff Email Address >> "))
        specialty = str(input("Staff Specialty >> "))
        department = str(input("Staff Department >> "))
        cursor.execute(
            f"INSERT INTO staff (fname, lname, email, specialty, department) values ('{fname}', '{lname}', '{email}', '{specialty}', '{department}')")
        firmdb.commit()
        print(f'Excellent! {fname} has been added to your table!')
        cursor = firmdb.cursor()
        print('Displaying your table')
        displayStaff()

insertStaffTable()