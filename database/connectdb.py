# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:15:31 2022

@author: Mario
"""

import psycopg2 as conn
from psycopg2 import DatabaseError
from decouple import config
from flask_pymongo import PyMongo
from flask import Flask

def connect_postgresql(hostname, dbname, username, password):
    try:
        conn_query = "host = '" + hostname + "' dbname = '" + dbname + "' user= '" + username + "' password= '" + password + "' port = '5432' sslmode = 'require'"
        conn_post = conn.connect(conn_query)
        print("Database connect successfully to PostgreSQL")
        return conn_post
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a PostgreSQL: ", e)
        raise Exception(e)


"""
def connect_postgresql(hostname, dbname, username, password):
    try:
        conn_query = "host = '" + hostname + "' dbname = '" + dbname + "' user= '" + username + "' password= '" + password + "' port = '5432' sslmode = 'require'"
        conn_post = conn.connect(conn_query)
        print("Database connect successfully to PostgreSQL")
        return conn_post
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a PostgreSQL: ", e)
        raise Exception(e)
"""

# Method to connect MongoDB Local
def connect_MongoDB_local():
    try:
        app = Flask(__name__)
        app.config["MONGO_URI"] = "mongodb://localhost:27017/mypimesutn"
        mongo = PyMongo(app)
        return mongo.db
    except Exception as e:
        print("Error to connect MongoDB: ", e)

# Method to connect MongoDB Remote
def connect_MongoDB(username, password, database):
    try:
        hostnae = "n1-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017,n2-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017"
        app = Flask(__name__)
        app.config["MONGO_URI"] = "mongodb://{0}:{1}@{2}/{3}".format(username, password, hostnae, database) # "mongodb+srv://{0}:{1}@{2}/{3}".format(username, password, hostname, database)
        mongo = PyMongo(app)
        if mongo.db.with_options is not None:
            return mongo
        else:
            print("Error no se pudo conectar!")
    except Exception as e:
        print("Error to connect MongoDB: ", e)

def get_connectionMongoDB():
    try:
        mongo =  connect_MongoDB(
            config('USERNAME_MONGODB'),
            config('PASSWORD_MONGODB'),
            config('DATABASE_MONGODB')
        )
        return mongo
    except Exception as ex:
        raise ex
# connect_postgresql(hostname, dbname, username, password):
def get_connection():
    try:
        connection = connect_postgresql(
            config('HOST_NAME_HEROKU'),
            config('DATABASE_HEROKU'),
            config('USER_NAME_HEROKU'),
            config('PASSWORD_HEROKU'),
            #config('HOST_NAME_LOCAL'),
            #config('DATABASE_LOCAL'),
            #config('USER_NAME_LOCAL'),
            #config('PASSWORD_LOCAL')
        )
        return connection
    except Exception as ex:
        raise ex
"""

a = get_connection()
a = a.cursor()
a.execute("select * from detalle_reservaciones dr")
row = a.fetchall()
for p in row:
    print(p)

"""