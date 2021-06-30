import urllib , json
import pandas as pd
import sqlite3
from sqlite3 import Error
import logging
import os
import pathlib
import glob


#all the companies for which we have to do a databse entry
company_name=['MSFT','ABB','AAL','AAPL','DELL']

#we have used pathlib as it could easily be used in windows and linux  
db_path=pathlib.Path.cwd().joinpath('sqlite','db','consume.db') 

def createConnection(db_path):
    conn=None
    try:
        conn=sqlite3.connect(db_path)
        return conn
    except Error as e:
        print(e)

#get the list of uRL's from where we have to fetch data 
def getURL(arr):
    urlList=[]
    for company in arr:
        url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED\
        &apikey=NQCFKOVGZASY3EZ9&symbol={company}"
        url = url.replace(" ","") #in case there is any space in URL 
        urlList.append(url)
    return urlList


#imports json from the Restapi 
def ImportJson(url):
    response =urllib.request.urlopen(url)
    data=json.loads(response.read()) #converts to python dict 
    return data


def CreateTable(conn,query):
    try:
        cursor=conn.cursor()
        cursor.execute(query)
    except Error as e:
        print(e)

def CreateEntry(conn,company_name):
    urlList=getURL(company_name)
    cursor=conn.cursor()
    for i,url in enumerate(urlList):
        company=company_name[i]
        data=ImportJson(url)
        entries=[]
        for item in data['Time Series (Daily)'].items():
            cateogary=list(item)
            entries.append(cateogary)
        #initialize variables
        dates=0
        Open = 0
        high = 0
        low = 0
        close =0 
        adjusted_close =0 
        volume=0
        dividend_amount = 0
        split_coefficient=0
        
        #insert data rows into shares
        for date, d in entries:
            dates=date
            Open=d['1. open']
            high=d['2. high']
            low=d['3. low']
            close=d['4. close']
            adjusted_closed=d['5. adjusted close']
            volume=d['6. volume']
            dividend_amount=d['7. dividend amount']
            split_coefficient=d['8. split coefficient']

            cursor.execute("INSERT INTO shares VALUES (?,?,?,?,?,?,?,?,?,?)",(company,dates,Open,high,low,
                                                                              close,adjusted_close,volume,
                                                                              dividend_amount,split_coefficient))

    conn.commit()




if __name__=="__main__":
    #query for creating column names

    sql_query= """ CREATE TABLE IF NOT EXISTS shares (
                                    company_name TEXT NOT NULL,
                                    dates TEXT NOT NULL,
                                    Open REAL , 
                                    high  REAL ,
                                    low  REAL ,
                                    close  REAL ,
                                    adjusted_close  REAL ,
                                    volume REAL ,
                                    dividend_amount  REAL ,
                                    split_coefficient  REAL); """
    conn=createConnection(db_path)
    if conn:
        CreateTable(conn,sql_query)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")
    cursor=conn.cursor()
    count=cursor.execute("SELECT count(*) AS 'total_count' FROM shares").fetchall()
    rows=count[0][0]
    if rows<1:
        CreateEntry(conn,company_name)

    print("DATABASE IS CREATED AND VALUES ARE ENTERED")
    


