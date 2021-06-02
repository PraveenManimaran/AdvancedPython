#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:05:14 2020

@author: praveenmanimaran
"""



from bs4 import BeautifulSoup
import json


def PrintIt(t):
        print(type(t))
        print(json.dumps(t))
        print(type(json.dumps(t)))
        print('----------')
dict1 = {}
with open('/Users/praveenmanimaran/Desktop/Presidents.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    
    rows_list = soup.find_all('tr')
   
    firstList = []
    presidentNames = []
    termNumber = []
    count = 0
    for a in rows_list:
        if(count>=1):
            firstList.append(a)
            if(count<10):
                termNumber.append(a.b.text[0])
            elif(count>=10 and count<=23):
                termNumber.append(a.b.text[0]+a.b.text[1])
            else:
                termNumber.append(a.b.text[1]+a.b.text[2])
            
        count = count +1
    
    
    for x in range(0, len(firstList)):
        nextList = firstList[x].find_all('a')
        presidentNames.append(nextList[0].text)
    
    
    for b in range(0, len(termNumber)):
        dict1[termNumber[b]] = presidentNames[b]
   
    print(dict1)
    
    j = json.dumps(dict1)
    print(json.dumps(j["1"]))
    #PrintIt(j)
   

    
    '''
    def insert(Id,termNumber, presidentName):
    try:
        sqliteConnection = sqlite3.connect('Lab3_SQLite.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        
        cursor.execute(" INSERT INTO Database(Id, TermNumber, President) VALUES (?, ?, ?)"
                       ,(Id, termNumber, presidentName))
        
        sqliteConnection.commit()
        cursor.close()
        
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed\n")
    '''
    
   # for x in firstList:
       # print(x.text)
       # count+=1
    # print(nextList[0].find_all('title'))


'''
html = urlopen('https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions')
    soup = BeautifulSoup(html, 'html.parser') 
    
  
    rows_list = soup.find_all('tr')
    
    
    countryList = []
    count = 0
    for a in rows_list:
        if(count>=6):
            countryList.append(a)
        count = count +1
    
    for x in range(0, len(countryList)):
        nextList = countryList[x].find_all('td')
        
        if(len(nextList) == 8):
            countryNames.append(nextList[0].a.text)
            Emissions1990.append(nextList[1].text)
            Emissions2005.append(nextList[2].text)
            Emissions2017.append(nextList[3].text)
            Percentage_2017.append(nextList[4].text)
            ChangeFrom1990To2017.append(nextList[5].text)
            PerLandArea.append(nextList[6].text)
            PerCapita .append(nextList[7].text)
    

'''