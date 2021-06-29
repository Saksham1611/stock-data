from flask import Flask
import pandas as pd
import urllib , json
import sqlite3
from sqlite3 import Error
import logging
import pathlib

# Create instance of flask
app = Flask(__name__)

#create connection
DATABASE=pathlib.Path.cwd().joinpath('sqlite','db','consume.db')
def createConnection(db_path):
    conn=None
    try:
        conn=sqlite3.connect(db_path)
        return conn
    except Error as e:
        print(e) 

conn=createConnection(DATABASE)
cursor=conn.cursor()

#home function
@app.route('/')
def home():
    return f'Hi welcome to the flask home page'


@app.route("/feature/<string:company>" ,methods=['GET','POST'])
def getfeatures(company):
    return getfeaturesone(company)
    # global conn ,cursor
    # conn=sqlite3.connect(DATABASE)
    # cursor=conn.cursor()
    # query="SELECT Open ,high , low , close FROM shares WHERE company_name = " + company
    # print("DATABE PATH BELOW")
    # print(DATABASE)
    # print("! In am inside the function get feaure")
    # print(cursor.execute(query).fetchall())
    # df =pd.read_sql_query(query,conn)
    # print(df.head(4))
    # labels=['Open','high','low','close']
    # df.to_csv('feature.csv',columns=labels, index=False)
    # result=cursor.execute(query)
    # items=[dict(zip([key[0] for key in cursor.description], row)) for row in result]
    # #dump the dictinary into python 
    # with open('feature.json', "w") as outfile: 
    #     json.dump(items, outfile,indent=4)
    # return "<p>The files have been saved to your current directory :)</p>"

def getfeaturesone(company):
    # global conn ,cursor
    con1=sqlite3.connect(DATABASE)
    cursor1=con1.cursor()
    query="SELECT Open ,high , low , close FROM shares WHERE company_name = " + company
    print("DATABE PATH BELOW")
    print(DATABASE)
    print("! In am inside the function get feaure")
    print(cursor1.execute(query).fetchall())
    df =pd.read_sql_query(query,con1)
    print(df.head(4))
    labels=['Open','high','low','close']
    df.to_csv('feature.csv',columns=labels, index=False)
    result=cursor1.execute(query)
    items=[dict(zip([key[0] for key in cursor1.description], row)) for row in result]
    #dump the dictinary into python 
    with open('feature.json', "w") as outfile: 
        json.dump(items, outfile,indent=4)
    return "<p>The files have been saved to your current directory :)</p>"

# @app.route('/difference/<string:company>',methods=['GET','POST'])
# def getDifference(company):
    
#     query="SELECT dates , close-Open AS 'DIFFERENCE' FROM shares WHERE company_name=" + company
#     df=pd.read_sql_query(query,conn)
#     return df.head(5)

# @app.route('/average/<string:company>',methods=['GET','POST'])
# def getAverage():
#     query="SELECT dates ,avg(close-Open) AS 'AVG' FROM shares GROUP BY dates"
#     df=pd.read_sql_query(query,conn)
#     return df.head(5)

@app.route('/count/<string:company>',methods=['GET','POST'])
def MaximumCount(company):
    DATABASE=pathlib.Path.cwd().joinpath('sqlite','db','consume.db')
    conn=sqlite3.connect(DATABASE)
    cursor=conn.cursor()
    query="SELECT Open , close FROM shares WHERE company_name=" + company
    res=cursor.execute(query)
    temp=[dict(zip([key[0] for key in cursor.description],row) for row in res)]
    Max=0
    currMax=0
    for key in temp:
        for op,cl in key.items():
            if op[1]>cl[1]:
                Max=max(Max,currMax)
                currMax=0
            else:
                currMax+=1
    return "<p>The number of continuous records having a positive diff are {Max}<p>"

# company='"ABB"'    
# query="SELECT Open ,high , low , close FROM shares WHERE company_name = " + company
# print(cursor.execute(query).fetchall())