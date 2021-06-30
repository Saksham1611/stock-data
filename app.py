from flask import Flask
from flask_restful import Api ,Resource
import sqlite3
import pandas as pd
import urllib , json
from sqlite3 import Error
import logging
import pathlib

app=Flask(__name__)
api=Api(app)

class Feature(Resource):
    def get(self, company):
        db_path=pathlib.Path.cwd().joinpath('sqlite','db','consume.db')
        conn=sqlite3.connect(db_path)
        cursor=conn.cursor()
        labels=['Open','high','low','close']
        query="SELECT Open ,high , low , close FROM shares WHERE company_name = " + company
        df =pd.read_sql_query(query,conn)
        df.to_csv("feature.csv",columns=labels, index=False)
        result=cursor.execute(query)
        items=[dict(zip([key[0] for key in cursor.description], row)) for row in result]
        #dump the dictinary into python 
        with open("feature.json", "w") as outfile: 
            json.dump(items, outfile,indent=4)
        print("The feature.json and feature.csv files have been saved to your current directory")
        conn.close()
        return {"Example_Feature_row":items[0]}

class Difference(Resource):
    def get(self,company):
        db_path=pathlib.Path.cwd().joinpath('sqlite','db','consume.db')
        conn=sqlite3.connect(db_path)
        cursor=conn.cursor()
        query="SELECT dates , close-Open AS 'DIFFERENCE' FROM shares WHERE company_name=" + company
        result=cursor.execute(query)
        items=[dict(zip([key[0] for key in cursor.description], row)) for row in result]
        conn.close()
        return {"Difference":items}

class Average(Resource):
    def get(self,company):
        db_path=pathlib.Path.cwd().joinpath('sqlite','db','consume.db')
        conn=sqlite3.connect(db_path)
        cursor=conn.cursor()
        query="SELECT dates ,avg(close-Open) AS 'AVG' FROM shares GROUP BY dates"
        result=cursor.execute(query)
        items=[dict(zip([key[0] for key in cursor.description], row)) for row in result]
        conn.close()
        return {"Average":items}

class MaximumCount(Resource):
    def get(self,company):
        db_path=pathlib.Path.cwd().joinpath('sqlite','db','consume.db')
        conn=sqlite3.connect(db_path)
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
        conn.close()
        return {"Maximum_Continous_Records":Max}

api.add_resource(MaximumCount, "/maximum/<string:company>")
api.add_resource(Average, "/average/<string:company>")
api.add_resource(Difference, "/difference/<string:company>")
api.add_resource(Feature, "/feature/<string:company>")



if __name__=="__main__":
    app.run(debug=True)