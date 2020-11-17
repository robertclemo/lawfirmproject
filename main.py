import mysql.connector
from mysql.connector import connect
import os
from os import system, getenv
import colorama
from colorama import Fore, Style
from dotenv import load_dotenv

load_dotenv()


conn = connect(
    host = "127.0.0.1",
    user = "",
    password = "",
    database =  "",
      
)

def displayEmployees():
    system('cls')
    tableName = "employees"
    try:
        mycursor = conn.cursor()
        mycursor.execute(
            f"SELECT * FROM {tableName} ORDER BY empID"
        )
        #rows = mycursor.fetchall()
        print(Style.RESET_ALL)
        #if(rows):
        print(Fore.CYAN, 'Employee Information: ')
        print(Style.RESET_ALL)
        for row in mycursor:
            print(f'''{Fore.RED}
            Employee ID:.....................{Style.RESET_ALL}{Fore.BLUE}{row[0]}{Fore.WHITE}
            Last Name:.......................{Style.RESET_ALL}{Fore.BLUE}{row[1]}{Fore.WHITE}
            First Name:......................{Style.RESET_ALL}{Fore.BLUE}{row[2]}{Fore.WHITE}
            Title:...........................{Style.RESET_ALL}{Fore.BLUE}{row[3]}{Fore.WHITE}
            Reports To:......................{Style.RESET_ALL}{Fore.BLUE}{row[4]}{Fore.WHITE}
            Email:...........................{Style.RESET_ALL}{Fore.BLUE}{row[5]}{Fore.WHITE}
            Username:........................{Style.RESET_ALL}{Fore.BLUE}{row[6]}{Fore.WHITE}
            Password:........................{Style.RESET_ALL}{Fore.BLUE}{row[7]}{Fore.WHITE}
            ''')
        mycursor.close()
        conn.close()
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)
    
displayEmployees()

def insertEmployeeTable():
    tableName = "employees"
    count = int(input("How many employees do you wish to add? >> "))
    cursor = conn.cursor()
    for i in range(count):
        print(f'Please fill out the following for the {i+1} employees: >> ')
        fname = str(input("Staff First Name >> "))
        lname = str(input("Staff Last Name >> "))
        email = str(input("Staff Email Address >> "))
        specialty = str(input("Staff Specialty >> "))
        department = str(input("Staff Department >> "))
        cursor.execute(
            f"INSERT INTO employees (Last_Name, First_Name, title, ReportsTo, email, username, Password) values ('{Last_Name}', '{First_Name}', '{Title}', '{ReportsTo}', '{Email}', '{username}', '{Password}')")
        conn.commit()
        print(f'Excellent! {fname} has been added to your table!')
        cursor = conn.cursor()
        print('Displaying your table')
        displayEmployees()

insertEmployeeTable()
