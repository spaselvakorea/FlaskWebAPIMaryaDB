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
    
        return jsonify(rows)

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
    
        return jsonify(rows)

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
    
        return jsonify(rows)

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
    
        return jsonify(rows)

    @api.response(403, 'Not Authorized')
    def post(self, id):
        api.abort(403)

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    PORT = 8086
    app.run(HOST, PORT)
