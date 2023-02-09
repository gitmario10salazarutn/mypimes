# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:15:31 2022

@author: Mario
"""

import pyodbc as conn
from decouple import config
from flask_pymongo import PyMongo
from flask import Flask

# Method to connect SQL Server
def connect_sqlserver(hostname, dbname, username, password):
    try:
        conexion = conn.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                hostname + ';DATABASE=' + dbname + ';UID=' + username + ';PWD=' + password)
        #print("Database connect successfully to SQL Server")
        #print(config('HOSTNAME'), config('USER_NAME'), config('SERVER'), config('PASSWORD'), config('USERNAME'))
        return conexion
    except Exception as e:
        # Atrapar error
        print("Error to connect to SQL Server: ", e)


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
def connect_MongoDB(hostname, username, password, database):
    try:
        app = Flask(__name__)
        app.config["MONGO_URI"] = "mongodb+srv://{0}:{1}@{2}/{3}".format(username, password, hostname, database)
        print(app.config["MONGO_URI"])
        mongo = PyMongo(app)
        if mongo.db.with_options is not None:
            return mongo
        else:
            print("Error no se pudo conectar!")
    except Exception as e:
        print("Error to connect MongoDB: ", e)


def get_connection():
    try:
        return connect_sqlserver(
            config('HOST_NAME'),
            config('DATABASE'),
            config('USER_NAME'),
            config('PASSWORD')
        )
    except Exception as ex:
        raise ex

def get_connectionMongoDB():
    try:
        mongo =  connect_MongoDB(
            config('HOSTNAME_MONGODB'),
            config('USERNAME_MONGODB'),
            config('PASSWORD_MONGODB'),
            config('DATABASE_MONGODB')
        )
        return mongo
    except Exception as ex:
        raise ex

class Entities:
    @classmethod
    def rol_usuarioEntity(self, rol_usuario) -> dict:
        if rol_usuario:
            return {
                "rol_idrol": rol_usuario[0],
                "rol_nombrerol": rol_usuario[1]
            }
        else:
            return None
    
    @classmethod
    def list_rolUsuarios(self,rol_usuarios) -> list:
        return [self.rol_usuarioEntity(rol_usuario) for rol_usuario in rol_usuarios]

    @classmethod
    def personaEntity(self, persona) -> dict:
        if persona:
            return {
            "pers_persona": persona[0],
            "pers_email": persona[1],
            "pers_nombres": persona[2],
            "pers_apellidos": persona[3],
            "pers_telefono": persona[4],
            "pers_direccion": persona[5]
        }
        else:
            return None

    @classmethod
    def listPersonas(self, personas) -> list:
        return [self.personaEntity(persona) for persona in personas]

    @classmethod
    def usuarioEntity(self, usuario) -> dict:
        if usuario:
            return  {
			"user_idusuario": usuario[8],
			"user_password": usuario[11],
			"user_estado": usuario[9],
			"user_fecha": usuario[10].strftime('%d/%m/%Y'),
            "rol_usuario": {
                "rol_idrol": usuario[0],
			    "rol_nombrerol": usuario[1]
            },
            "persona": {
                "pers_persona": usuario[2],
                "pers_email": usuario[3],
                "pers_nombres": usuario[4],
                "pers_apellidos": usuario[5],
                "pers_telefono": usuario[6], 
                "pers_direccion": usuario[7]
            }
        }
        else:
            return None

    @classmethod
    def listUsuarios(self, usuarios) -> list:
        return [self.usuarioEntity(user) for user in usuarios]

con  = get_connection().cursor()
row  = con.execute("select p.pers_persona, p.pers_email, p.pers_nombres, p.pers_apellidos, p.pers_telefono, p.pers_direccion from persona p")

for p in row:
    print(p)