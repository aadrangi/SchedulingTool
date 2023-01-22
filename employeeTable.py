# employeeTable.py is called when a new employee is entered into the database.
import sqlite3
import pandas as pd


class employeeDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('Employee_Database.db')
        self.curr = self.conn.cursor()
    def createDatabase(self):
        # CREATE table query (only needs to be run once)
        create_table = (
            "CREATE TABLE employees (first_name, last_name, is_lead, day_night, is_OT)"  # create database
        )
        self.curr.execute(create_table)
        self.conn.commit()
        # employeeDatabase.close()
        # c.execute(create_table)
    def insertData(self, data):
        # INSERT data into table query
        insert_stmt = (
            "INSERT INTO employees (firstName, lastName, is_lead, day_night, is_OT, programs, is_fieldJob) "
            "VALUES (?, ?, ?, ?, ?)"
        )  # statement uses sql syntax to insert info into database
        # data = ('Arash', 'Adrangi', False, 'Night', False)  # insert data into table
        self.curr.execute(insert_stmt, data)  # executes the query
        self.conn.commit()  # commit changes to database
    def clearData(self):
        # CLEAR the database
        delete_stmt = (
            "DELETE FROM employees"
        )
        self.curr.execute(delete_stmt)  # executes the query
        self.conn.commit()  # commit changes to database
    def viewDatabase(self):
        # VIEW all data within the database
        view_stmt = (
            "SELECT * FROM employees"
        )
        self.curr.execute(view_stmt)
        rows = self.curr.fetchall()
        self.conn.commit()
        return rows

data = ('Arash', 'Adrangi', False, 'Night', False)  # insert data into table
x = employeeDatabase()
# x.createDatabase()
print(x.viewDatabase())
x.insertData(data)
print(x.viewDatabase())
x.clearData()
print(x.viewDatabase())
x.conn.close()
