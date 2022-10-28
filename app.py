"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restplus import Api, Resource, fields
from datetime import datetime
import os
import sys
import mysql.connector as database
import configparser
import json
import io

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='PIOLINK MariaDB API',
    description='PIOLINK MariaDB API for Web Monitoring List',
)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

config = configparser.ConfigParser()
config.read('config.ini')

class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value


@api.route('/sites')
class sitesRoot(Resource):
    def get(self):
        # Instantiate Connection
        try:
           conn = database.connect(user=config["mysql"]["user"], password=config["mysql"]["password"], host=config["mysql"]["host"], port=int(config["mysql"]["port"]), database=config["mysql"]["db"], auth_plugin = 'mysql_native_password', autocommit=False)
        except database.Error as e:
           print(f"Error connecting to MariaDB Platform: {e}")
           sys.exit(1)

        # Instantiate Cursor
        cur = conn.cursor()

        # sql query 
        sql_squery = "SELECT * FROM sites"

        # exec sql query 
        cur.execute(sql_squery)

        # fetch qeury result
        rows = cur.fetchall()
        #print (rows,'\n')

        # commit 
        conn.commit()

        # Clean up
        cur.close()
        conn.close()
    
        #return jsonify(rows)
        mydict = create_dict()
        for row in rows:
            mydict.add(row[0],({"no":row[0], "username":row[1], "site_name":row[2], "site_url":row[3], "screenshot":row[4], "reg_date":row[5], "last_chk_date":row[6], "similarity":row[7], "defaced":row[8], "send_email":row[9], "threshold":row[10], "reputation_result":row[11], "ai_result":row[12], "ai_score":row[13], "analysis_detail":json.loads(row[14])}))
        
        json_array = [value for key, value in mydict.items()]
        return jsonify(json_array)
        

@api.route('/site_contents')
class sitesRoot(Resource):
    def get(self):
        # Instantiate Connection
        try:
           conn = database.connect(user=config["mysql"]["user"], password=config["mysql"]["password"], host=config["mysql"]["host"], port=int(config["mysql"]["port"]), database=config["mysql"]["db"], auth_plugin = 'mysql_native_password', autocommit=False)
        except database.Error as e:
           print(f"Error connecting to MariaDB Platform: {e}")
           sys.exit(1)

        # Instantiate Cursor
        cur = conn.cursor()

        # sql query 
        sql_squery = "SELECT * FROM sites JOIN site_contents ON sites.no = site_contents.site_no"

        # exec sql query 
        cur.execute(sql_squery)

        # fetch qeury result
        rows = cur.fetchall()
        #print (rows,'\n')

        # commit 
        conn.commit()

        # Clean up
        cur.close()
        conn.close()
    
        #return jsonify(rows)
        mydict = create_dict()
        for row in rows:
            mydict.add(row[15],({"no":row[0], "username":row[1], "site_name":row[2], "site_url":row[3], "screenshot":row[4], "reg_date":row[5], "last_chk_date":row[6], "similarity":row[7], "defaced":row[8], "send_email":row[9], "threshold":row[10], "reputation_result":row[11], "ai_result":row[12], "ai_score":row[13], "analysis_detail":json.loads(row[14]), "site_contents_no":row[15], "username":row[16], "site_no":row[17], "filetype":row[18], "pathname":row[19], "check_date":row[20], "is_malware":row[21], "reputation_result":row[22], "ai_result":row[23], "ai_score":row[24], "site_contents_analysis_detail":json.loads(row[25])}))

        json_array = [value for key, value in mydict.items()]
        return jsonify(json_array)


@api.route('/sites/<id>')
@api.doc(params={'id': 'An Site NO'})
class siteResource(Resource):

    def get(self, id):
        # Instantiate Connection
        try:
           conn = database.connect(user=config["mysql"]["user"], password=config["mysql"]["password"], host=config["mysql"]["host"], port=int(config["mysql"]["port"]), database=config["mysql"]["db"], auth_plugin = 'mysql_native_password', autocommit=False)
        except database.Error as e:
           print(f"Error connecting to MariaDB Platform: {e}")
           sys.exit(1)

        # Instantiate Cursor
        cur = conn.cursor()

        # sql query 
        sql_squery = "SELECT * FROM sites WHERE no="+id

        # exec sql query 
        cur.execute(sql_squery)

        # fetch qeury result
        rows = cur.fetchall()
        #print (rows,'\n')

        # commit 
        conn.commit()

        # Clean up
        cur.close()
        conn.close()
    
        #return jsonify(rows)
        mydict = create_dict()
        for row in rows:
            mydict.add(row[0],({"no":row[0], "username":row[1], "site_name":row[2], "site_url":row[3], "screenshot":row[4], "reg_date":row[5], "last_chk_date":row[6], "similarity":row[7], "defaced":row[8], "send_email":row[9], "threshold":row[10], "reputation_result":row[11], "ai_result":row[12], "ai_score":row[13], "analysis_detail":json.loads(row[14])}))

        json_array = [value for key, value in mydict.items()]
        return jsonify(json_array)


    @api.response(403, 'Not Authorized')
    def post(self, id):
        api.abort(403)

@api.route('/site_contents/<id>')
@api.doc(params={'id': 'An Site NO or Site Contents SITE_NO'})
class siteResource(Resource):

    def get(self, id):
        # Instantiate Connection
        try:
           conn = database.connect(user=config["mysql"]["user"], password=config["mysql"]["password"], host=config["mysql"]["host"], port=int(config["mysql"]["port"]), database=config["mysql"]["db"], auth_plugin = 'mysql_native_password', autocommit=False)
        except database.Error as e:
           print(f"Error connecting to MariaDB Platform: {e}")
           sys.exit(1)

        # Instantiate Cursor
        cur = conn.cursor()

        # sql query 
        sql_squery = "SELECT * FROM sites JOIN site_contents ON sites.no = site_contents.site_no WHERE sites.no="+id

        # exec sql query 
        cur.execute(sql_squery)

        # fetch qeury result
        rows = cur.fetchall()
        #print (rows,'\n')

        # commit 
        conn.commit()

        # Clean up
        cur.close()
        conn.close()
        
        #return jsonify(rows)
        mydict = create_dict()
        for row in rows:
            mydict.add(row[15],({"no":row[0], "username":row[1], "site_name":row[2], "site_url":row[3], "screenshot":row[4], "reg_date":row[5], "last_chk_date":row[6], "similarity":row[7], "defaced":row[8], "send_email":row[9], "threshold":row[10], "reputation_result":row[11], "ai_result":row[12], "ai_score":row[13], "analysis_detail":json.loads(row[14]), "site_contents_no":row[15], "username":row[16], "site_no":row[17], "filetype":row[18], "pathname":row[19], "check_date":row[20], "is_malware":row[21], "reputation_result":row[22], "ai_result":row[23], "ai_score":row[24], "site_contents_analysis_detail":json.loads(row[25])}))

        json_array = [value for key, value in mydict.items()]
        return jsonify(json_array)


    @api.response(403, 'Not Authorized')
    def post(self, id):
        api.abort(403)

if __name__ == '__main__':
    #HOST = os.environ.get('SERVER_HOST', '192.168.1.229')
    HOST = '192.168.1.229'
    PORT = 8086
    app.run(HOST, PORT)
