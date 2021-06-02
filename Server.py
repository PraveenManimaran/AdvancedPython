import socket
import sys
import xml.etree.ElementTree as ET
from tkinter import *
import tkinter.messagebox
import sqlite3
from tkinter import messagebox
import json
def server_program():
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server_address = ('localhost', 20006)
    print('starting up on {} port {}'.format(*server_address))
    s.bind(server_address)
    
    # Listen for incoming connections
    s.listen(5)
    
    
    while True:
         # Wait for a connection
        print('Waiting for a connection')
        connection, address = s.accept()
        try:
            print("Connection from",address, " has been established!")
            connection.sendall("Hello")
            break
        finally:
            # Clean up the connection
            print("Closing Server Socket")
            
            connection.close()
def readXmlFile(fileName, country):
    countryDict = []
    #countryUnsortedSet = set()
    finalDict = {}
    
    year = ""
    list1 = []
    
    # Parse XML with ElementTree
    tree = ET.ElementTree(file=fileName)
    root = tree.getroot()
    elements = root.getchildren()
    for element in elements:
        elem_children = element.getchildren()
        for elem_child in elem_children:
            elem1 = elem_child.getchildren()
            for elem2 in elem1:
                
                if(elem2.tag == "Country"):
                    countryName = elem2.text
                    year = ""
                    #countryUnsortedSet.add(elem2.text)
                if(elem2.tag == "Year"):
                    year = elem2.text
                         
                if(elem2.tag == "Value"):
                    value = float(elem2.text)
                    value = round(value, 2)
                    tuple1 = (year, value)                   
                    list1.append(tuple1)
                    if(year == "1990"):
                        finalDict[countryName] = list1
                        list1 = []
    connectToDataBase()
    createTable()
    for x in range(28):
        insert(x, finalDict[country][x][0], finalDict[country][x][1])
    
    countryDict = finalDict[country]
    jsonObject = json.dumps(countryDict)
   
    
    '''
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    # parse x:
    y = json.loads(x)
    print(type(y))
    '''
    return jsonObject  

def connectToDataBase():
    try:
        sqliteConnection = sqlite3.connect('Lab4_SQLite.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed\n")

def createTable():
    
    try:
        sqliteConnection = sqlite3.connect('Lab4_SQLite.db')
    
        cursor = sqliteConnection.cursor()
        
        #cursor.execute('CREATE TABLE IF NOT EXISTS Database(Id REAL, year REAL, medianTemperature REAL)')
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS Database(Id REAL, Year REAL, Value REAL )')
        print("Successfully Connected to SQLite")
        
        sqliteConnection.commit()
        print("SQLite table created")
    
        cursor.close()
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed\n")
            
def insert(Id, year, value):
    try:
        sqliteConnection = sqlite3.connect('Lab4_SQLite.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        
        cursor.execute(" INSERT INTO Database(Id, Year, Value) VALUES (?, ?, ?)"
                       ,(Id, year, value,))
        
        sqliteConnection.commit()
        cursor.close()
        
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed\n")

if __name__ == '__main__':
    server_program()
