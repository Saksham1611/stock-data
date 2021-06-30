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

db_path=pathlib.Path.cwd().joinpath('sqlite','db','consume.db') 

conn=sqlite3.connect(db_path)
cursor=conn.cursor()

class Feature(Resource):
    def get(self, company):
        labels=['Open','high','low','close']
        query="SELECT Open ,high , low , close FROM shares WHERE company_name = " + company
        df=cursor.execute(query).fetchall()
        print(df)
        #df =pd.read_sql_query(query,conn)
        #print(json.)
        # df.to_csv("feature.csv",columns=labels, index=False)
        # result=cursor.execute(query)
        # items=[dict(zip([key[0] for key in cursor.description], row)) for row in result]
        # #dump the dictinary into python 
        # with open("feature.json", "w") as outfile: 
        #     json.dump(items, outfile,indent=4)
        # #print("The files have been saved to your current directory")
        # return {"company":items}

api.add_resource(Feature, "/feature/<string:company>")



if __name__=="__main__":
    app.run(debug=True)