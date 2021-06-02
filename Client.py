import socket
import sys
import Server
import requests 
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
from collections import namedtuple
from collections import defaultdict
from tkinter import *
from tkinter.ttk import *
import tkinter
import sqlite3
from tkinter import *
import tkinter.messagebox
import sqlite3
from tkinter import messagebox
import json 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.patches as patches
import matplotlib.path as path
from scipy.interpolate import *
from pylab import * 

def main():  
   # Server.readXmlFile(fileName)
    createSocket()
    selectCountry()
    
def selectCountry():
    
    root = Tk()
    root.geometry("400x200")
    
    root.title("Select The Graph You Want To Display")
    options = ["Australia", "Austria", "Belarus", "Belgium", "Bulgaria", "Canada"
               ,"Croatia", "Cyprus", "Czechia","Denmark", "Estonia", "European Union"
               , "Finland", "France","Germany", "Greece", "Hungary","Iceland"
               ,"Ireland", "Italy","Japan","Latvia", "Liechtenstein", "Lithuania"
               , "Luxembourg", "Malta", "Monaco", "Netherlands","New Zealand", "Norway",
               "Poland", "Portugal", "Romania", "Russian Federation", "Slovakia"
               , "Slovenia", "Spain", "Swededn", "Switzerland", "Turkey", "Ukraine"
               , "United Kingdom", "United States of America"]
    var = StringVar()
    menu = OptionMenu(root,var,*options,command=selected)
    menu.place(x=1,y=1)

    root.mainloop()
   

def createSocket():
     # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 20006)
    print('connecting to {} port {}'.format(*server_address))
    s.connect(server_address)
    
    
    try:
        msg = s.recv(1024)
        print(msg.decode())
    finally:
        print("Closing Socket")
        s.close()

    
def selected(value):
    #CHANGE PATH NAME!
    fileName = "/Users/praveenmanimaran/Desktop/UNData.xml"
    jSonObject = Server.readXmlFile(fileName, value)
    
    newDict = json.loads(jSonObject)
    plotData(newDict)
    #print(countryDict)
def plotData(countryDict):
    #print(countryDict[0])
    years = []
    values = []
    for key2 in countryDict:
        year = (int)(key2[0])
        value = key2[1]
        years.append(year)
        values.append(value)
    
    plt.plot(years, values)
    plt.xlabel("Years")
    plt.ylabel("Values")
    plt.title("XY Plot")
    plt.show()
      
  
if __name__ == '__main__':
    main()