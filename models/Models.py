# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:28:03 2022

@author: Mario
"""

from database import connectdb as conn
from .entities import Entities as entities
import json
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Model:

    @classmethod
    def userEntity(self, entity) -> dict:
        if entity:
            return {
            "_id": str(entity['_id']),
            "user_idusuario": entity['user_idusuario'],
            "user_password": entity['user_password'],
            "user_estado": entity['user_estado'],
            "user_email": entity['user_email']
        }
        else:
            return None
    
    @classmethod
    def usersEntity(self, entitys) -> list:
        return [self.userEntity(entity) for entity in entitys]
    
    #Example MongoDB
    @classmethod
    def create_users(self, data):
        try:
            username = data['user_idusuario']
            password = data['user_password']
            estado = data['user_estado']
            email = data['user_email']
            if username and password and email:
                hashed_password = generate_password_hash(password)
                mongo = conn.get_connectionMongoDB().db
                users = mongo['users']
                id = users.insert_one(
                    {
                    'user_idusuario': username,
                    'user_password': hashed_password,
                    'user_estado': estado,
                    'user_email': email
                    }
                )
                response = {
                    'id': str(id),
                    'user_idusuario': username,
                    'user_password': hashed_password,
                    'user_estado': estado,
                    'user_email': email
                    }
                return response
            else:
                return None
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_users(self):
        try:
            mongo = conn.get_connectionMongoDB().db
            collection = mongo['users']
            users = self.usersEntity(collection.find())
            if len(users) > 0:
                return users
            else:
                return None
        except Exception as  e:
            raise Exception(e)

    @classmethod
    def get_user_byid(self, id):
        try:
            mongo = conn.get_connectionMongoDB().db
            collection = mongo['users']
            return [self.userEntity(collection.find_one({'user_idusuario': id}))]
        except Exception as  e:
            raise Exception(e)

    @classmethod
    def delete_user(self, id):
        try:
            mongo = conn.get_connectionMongoDB().db
            collection = mongo['users']
            return [self.userEntity(collection.find_one_and_delete({'user_idusuario': id}))]
        except Exception as  e:
            raise Exception(e)

    @classmethod
    def update_user(self, id_user, data):
        try:
            hashed_password = generate_password_hash(data['user_password'])
            estado = data['user_estado']
            email = data['user_email']
            mongo = conn.get_connectionMongoDB().db
            collection = mongo['users']
            return [self.userEntity(collection.find_one_and_update({'user_idusuario': id_user},
                        { '$set': {
                    'user_password': hashed_password,
                    'user_estado': estado,
                    'user_email': email
                    }}))]
        except Exception as ex:
            raise Exception(ex)

    # Personas
    @classmethod
    def get_personas(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select p.pers_persona, p.pers_email, p.pers_nombres, p.pers_apellidos, p.pers_telefono, p.pers_direccion from persona p")
            result = cursor.fetchall()
            connection.close()
            persons = entities.Entities.listPersonas(result)
            return persons
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_persona_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select p.pers_persona, p.pers_email, p.pers_nombres, p.pers_apellidos, p.pers_telefono, p.pers_direccion from persona p where p.pers_persona= '{0}';".format(id))
            result = cursor.fetchone()
            connection.close()
            person = [entities.Entities.personaEntity(result)]
            return person
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_persona(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO persona(pers_persona, pers_email, pers_nombres, pers_apellidos, pers_telefono, pers_direccion) values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
                    data['pers_persona'], data['pers_email'], data['pers_nombres'], data['pers_apellidos'], data['pers_telefono'], data['pers_direccion']))
                rows_affects = cursor.rowcount
                id_persona = cursor.execute(
                    "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                print(rows_affects)
                connection.commit()
                if rows_affects > 0:
                    persona = entities.Persona(id_persona, data['pers_email'], data['pers_nombres'],
                                               data['pers_apellidos'], data['pers_telefono'], data['pers_direccion'])
                    return persona.convert_to_json()
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_persona(self, id_persona, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE persona SET pers_email = '{0}', pers_nombres = '{1}', pers_apellidos = '{2}', pers_telefono = '{3}', pers_direccion = '{4}' WHERE pers_persona = '{5}'".format(
                    data['pers_email'], data['pers_nombres'], data['pers_apellidos'], data['pers_telefono'], data['pers_direccion'], id_persona))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    point = entities.Persona(id_persona, data['pers_email'], data['pers_nombres'],
                                             data['pers_apellidos'], data['pers_telefono'], data['pers_direccion'])
                    return point
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_persona(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM persona WHERE pers_persona = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Person deleted successfully!'}
                else:
                    return {'message': 'Error, Delete person failed, person not found!'}
        except Exception as ex:
            raise Exception(ex)

    # Rol Usuario

    @classmethod
    def get_rolusuarios(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select p.rol_idrol, p.rol_nombrerol, p.prefijo from rol_usuario p;")
            result = cursor.fetchall()
            connection.close()
            rol_usuarios = entities.Entities.list_rolUsuarios(result)
            return rol_usuarios
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_rolusuario_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select p.rol_idrol, p.rol_nombrerol, p.prefijo from rol_usuario p where p.rol_idrol= {0};".format(id))
            result = cursor.fetchone()
            connection.close()
            rol_usuario = [entities.Entities.rol_usuarioEntity(result)]
            return rol_usuario
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_rolusuario(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO rol_usuario(rol_nombrerol, prefijo) values('{0}', '{1}')".format(
                    data['rol_nombrerol'], data['prefijo']))
                rows_affects = cursor.rowcount
                id_rol = cursor.execute(
                    "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    rol = self.get_rolusuario_byid(id_rol)
                    return rol
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_rolusuario(self, id_rol, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE rol_usuario SET rol_nombrerol = '{0}', prefijo = '{1}' WHERE rol_idrol = '{2}'".format(
                    data['rol_nombrerol'], data['prefijo'], id_rol))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    rol = self.get_rolusuario_byid(id_rol)
                    return rol
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_rolusuario(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM rol_usuario WHERE rol_idrol = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'User rol deleted successfully!'}
                else:
                    return {'message': 'Error, Delete person failed, User rol not found!'}
        except Exception as ex:
            raise Exception(ex)

    # Usuarios

    @classmethod
    def get_usuarios(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select*from get_usuarios;")
            result = cursor.fetchall()
            connection.close()
            users = entities.Entities.listUsuarios(result)
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_usuario_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select*from get_usuarios where user_idusuario = '{0}'".format(id))
            result = cursor.fetchone()
            connection.close()
            user = [entities.Entities.usuarioEntity(result)]
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_usuario(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO persona(pers_persona, pers_email, pers_nombres, pers_apellidos, pers_telefono, pers_direccion) values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
                    data['pers_persona'], data['pers_email'], data['pers_nombres'], data['pers_apellidos'], data['pers_telefono'], data['pers_direccion']))
                iduser = ''
                if int(data['rol_idrol']) == 1:
                    iduser = 'PRE-' + data['pers_persona']
                if int(data['rol_idrol']) == 2:
                    iduser = 'SEC-' + data['pers_persona']
                if int(data['rol_idrol']) == 3:
                    iduser = 'TES-' + data['pers_persona']
                if int(data['rol_idrol']) == 4:
                    iduser = 'CON-' + data['pers_persona']
                fecha = datetime.strptime(data['user_fecha'], '%d/%m/%Y')
                password = data['user_password']
                hashed = generate_password_hash(password)
                cursor.execute(
                    "INSERT INTO user_usuario(user_idusuario, rol_idrol, pers_persona, user_password, user_estado, user_fecha) values('{0}', {1}, '{2}','{3}', '{4}', '{5}')".format(iduser, data['rol_idrol'], data['pers_persona'], hashed, data['user_estado'], fecha))
                if int(data['rol_idrol']) == 1:
                    cursor.execute(
                        "INSERT INTO presidente(user_idusuario) values('{0}')".format(iduser))
                if int(data['rol_idrol']) == 2:
                    cursor.execute(
                        "INSERT INTO secretario(user_idusuario) values('{0}')".format(iduser))
                if int(data['rol_idrol']) == 3:
                    cursor.execute(
                        "INSERT INTO tesorero(user_idusuario) values('{0}')".format(iduser))
                if int(data['rol_idrol']) == 4:
                    cursor.execute(
                        "INSERT INTO condomino(user_idusuario) values('{0}')".format(iduser))
                rows_affects = cursor.rowcount
                connection.commit()
                da = {
                        "user_idusuario": iduser,
                        "user_password": hashed,
                        "user_estado": data['user_estado'],
                        "user_email": data['pers_email']
                    }
                if rows_affects > 0:
                    print(self.create_users(da))
                    user = self.get_usuario_byid(iduser)
                    return user
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_usuario(self, id_user, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                password = generate_password_hash(data['user_password'])
                cursor.execute("UPDATE persona SET pers_email = '{0}', pers_nombres = '{1}', pers_apellidos = '{2}', pers_telefono = '{3}', pers_direccion = '{4}' WHERE pers_persona = '{5}'".format(
                    data['pers_email'], data['pers_nombres'], data['pers_apellidos'], data['pers_telefono'], data['pers_direccion'], id_user[4:]))
                cursor.execute("UPDATE user_usuario SET user_password = '{0}', user_estado = {1} WHERE user_idusuario = '{2}'".format(password, data['user_estado'], id_user))
                rows_affects = cursor.rowcount
                connection.commit()
                da = {
                        "user_idusuario": id_user,
                        "user_password": password,
                        "user_estado": data['user_estado'],
                        "user_email": data['pers_email']
                    }
                if rows_affects > 0:
                    print(self.update_user(id_user, da))
                    user = self.get_usuario_byid(id_user)
                    return user
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_usuario(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM user_usuario WHERE user_idusuario = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    print(self.delete_user(id))
                    return {'message': 'User deleted successfully!'}
                else:
                    return {'message': 'Error, Delete user failed, user not found!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def assign_roluser(self, id_user, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                rol = self.get_rolusuario_byid(data['rol_idrol'])
                u = json.loads(rol[0])[0]
                id = u['prefijo']+id_user[4:]
                user_to_assign = self.get_usuario_byid(id)
                user = self.get_usuario_byid(id_user)
                if user and user_to_assign is None:
                    pers = json.loads(user[0])[0]
                    iduser = ''
                    if int(data['rol_idrol']) == 1:
                        iduser = 'PRE-' + pers['persona'].get('pers_persona')
                    if int(data['rol_idrol']) == 2:
                        iduser = 'SEC-' + pers['persona'].get('pers_persona')
                    if int(data['rol_idrol']) == 3:
                        iduser = 'TES-' + pers['persona'].get('pers_persona')
                    if int(data['rol_idrol']) == 4:
                        iduser = 'CON-' + pers['persona'].get('pers_persona')
                    fecha = datetime.now()
                    password = pers['user_usuario'].get('user_password')
                    hashed = generate_password_hash(password)
                    da = {
                        "user_idusuario": iduser,
                        "user_password": hashed,
                        "user_estado": pers['user_usuario'].get('user_estado'),
                        "user_email": pers['persona'].get('pers_email')
                    }
                    cursor.execute(
                        "INSERT INTO user_usuario(user_idusuario, rol_idrol, pers_persona, user_password, user_estado, user_fecha) values('{0}', {1}, '{2}', '{3}', {4}, '{5}')".format(iduser, data['rol_idrol'], pers['persona'].get('pers_persona'), hashed, pers['user_usuario'].get('user_estado'), fecha))
                    if int(data['rol_idrol']) == 1:
                        cursor.execute(
                            "INSERT INTO presidente(user_idusuario) values('{0}')".format(iduser))
                    if int(data['rol_idrol']) == 2:
                        cursor.execute(
                            "INSERT INTO secretario(user_idusuario) values('{0}')".format(iduser))
                    if int(data['rol_idrol']) == 3:
                        cursor.execute(
                            "INSERT INTO tesorero(user_idusuario) values('{0}')".format(iduser))
                    if int(data['rol_idrol']) == 4:
                        cursor.execute(
                            "INSERT INTO condomino(user_idusuario) values('{0}')".format(iduser))
                    rows_affects = cursor.rowcount
                    connection.commit()
                    if rows_affects > 0:
                        print(self.create_users(da))
                        user = self.get_usuario_byid(iduser)
                        return user
                else:
                    return None
        except Exception as ex:
            return Exception(ex)

    @classmethod
    def login(self, username, password):
        try:
            user_found = self.get_usuario_byid(username)
            if user_found:
                user = user_found[0]
                check_password = check_password_hash(user['user_password'], password)
                if check_password and user_found and user['user_estado'] == 0:
                    return user_found
                elif user['user_estado'] == 1:
                    return 1    # On case that user is disable
                else:
                    return -1   # Username or password are invalidates
            else:
                return None     # Username or password are invalidates
        except Exception as ex:
            return Exception(ex)
        
    #############################################################################################
        
        #SECRETARIO
        
     #Tipo de documento
    @classmethod
    def get_tipo_documento(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select td.tipdoc_id, td.tipdoc_nombre from tipo_documento td")
            result = cursor.fetchall()
            connection.close()
            tipodocumentos = entities.Entities.listTipoDocumentos(result)
            return tipodocumentos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_tipodocumento_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select td.tipdoc_id, td.tipdoc_nombre from tipo_documento td where td.tipdoc_id= {0};".format(id))
            result = cursor.fetchone()
            connection.close()
            td = [entities.Entities.tipodocumentoEntity(result)]
            return td
        except Exception as ex:
            raise Exception(ex)

    
    @classmethod
    def create_tipodocumento(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO tipo_documento(tipdoc_nombre) values('{0}')".format(
                    data['tipdoc_nombre']))
                rows_affects = cursor.rowcount
                id_td = cursor.execute(
                    "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                print(rows_affects)
                connection.commit()
                if rows_affects > 0:
                   ##td = entities.TipoDocumento(id_td, data['tipdoc_nombre'])
                    idd = self.get_tipodocumento_byid(id_td)
                    return idd
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_tipodocumento(self, id_tipdoc, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE tipo_documento SET tipdoc_nombre = '{0}' WHERE tipdoc_id = '{1}'".format(
                    data['tipdoc_nombre'],id_tipdoc))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    point = entities.TipoDocumento(id_tipdoc, data['tipdoc_nombre'])
                    return point
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_tipodocumento(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM tipo_documento WHERE tipdoc_id = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Type Document deleted successfully!'}
                else:
                    return {'message': 'Error, Delete type Document failed, Type Document not found!'}
        except Exception as ex:
            raise Exception(ex)
        

        
     #Documento
    @classmethod
    def get_documento(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select doc.doc_iddocumento, doc.tipdoc_id,doc.sec_idsecretario,doc.doc_descripcion,doc.doc_documento,doc.doc_entidad,doc.doc_recibido from documentos doc")
            result = cursor.fetchall()
            connection.close()
            documentoss = entities.Entities.listDocumentos(result)
            return documentoss
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_documento_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select doc.doc_iddocumento, doc.tipdoc_id,doc.sec_idsecretario,doc.doc_descripcion,doc.doc_documento,doc.doc_entidad,doc.doc_recibido from documentos doc where doc.doc_iddocumento= {0};".format(id))
            result = cursor.fetchone()
            connection.close()
            td = [entities.Entities.documentoEntity(result)]
            return td
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def create_documentos(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO documentos(tipdoc_id,sec_idsecretario,doc_descripcion,doc_documento,doc_entidad,doc_recibido) values('{0}', '{1}','{2}', '{3}','{4}','{5}')".format(
                    data['tipdoc_id'], data['sec_idsecretario'],data['doc_descripcion'],data['doc_documento'],data['doc_entidad'],data['doc_recibido']))
                rows_affects = cursor.rowcount
                id_d = cursor.execute(
                    "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                print(rows_affects)
                connection.commit()
                if rows_affects > 0:
                    d = entities.Documento(id_d,data['tipdoc_id'], data['sec_idsecretario'],data['doc_descripcion'],data['doc_documento'],data['doc_entidad'],data['doc_recibido'])
                    return d.convert_to_json()
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_documento(self, doc_iddocumento, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE documentos SET tipdoc_id = '{0}',sec_idsecretario='{1}',doc_descripcion='{2}',doc_documento='{3}',doc_entidad='{4}',doc_recibido='{5}' WHERE doc_iddocumento = '{6}'".format(
                    doc_iddocumento))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    point = entities.Documento(doc_iddocumento,data['tipdoc_id'], data['sec_idsecretario'],data['doc_descripcion'],data['doc_documento'],data['doc_entidad'],data['doc_recibido'])
                    return point
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def delete_documento(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM documentos WHERE doc_iddocumento = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Document deleted successfully!'}
                else:
                    return {'message': 'Error, Delete type Document failed, Type Document not found!'}
        except Exception as ex:
            raise Exception(ex)

     ##estado_documentos   
    @classmethod
    def get_estado_documentoTODO(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select ed.estdoc_id, ed.doc_iddocumento,ed.aprobado_presidente,ed.aprobado_entidad,ed.fecha_aprovadopresidente, ed.fecha_aprobadoentidad from estado_documentos ed")
            result = cursor.fetchall()
            connection.close()
            eds = entities.Entities.listEstadoDocumentos(result)
            return eds
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_estado_documentoTRUE(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select ed.estdoc_id, ed.doc_iddocumento,ed.aprobado_presidente,ed.aprobado_entidad,ed.fecha_aprovadopresidente, ed.fecha_aprobadoentidad from estado_documentos ed where ed.aprobado_presidente=1")
            result = cursor.fetchall()
            connection.close()
            eds = entities.Entities.listEstadoDocumentos(result)
            return eds
        except Exception as ex:
            raise Exception(ex)
    @classmethod    
    def get_estado_documentoFALSE(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                          "select ed.estdoc_id, ed.doc_iddocumento,ed.aprobado_presidente,ed.aprobado_entidad,ed.fecha_aprovadopresidente, ed.fecha_aprobadoentidad from estado_documentos ed where ed.aprobado_presidente=0")
            result = cursor.fetchall()
            connection.close()
            eds = entities.Entities.listEstadoDocumentos(result)
            return eds
        except Exception as ex:
            raise Exception(ex)
    
    

    
    @classmethod
    def get_estado_documento_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                         "select ed.estdoc_id, ed.doc_iddocumento,ed.aprobado_presidente,ed.aprobado_entidad,ed.fecha_aprovadopresidente, ed.fecha_aprobadoentidad from estado_documentos ed where ed.estdoc_id={0};".format(id))
            result = cursor.fetchone()
            connection.close()
            td = [entities.Entities.estado_documentosEntity(result)]
            return td
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_estado_documento(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO estado_documentos(doc_iddocumento,aprobado_presidente,aprobado_entidad,fecha_aprovadopresidente,fecha_aprobadoentidad) values('{0}','{1}','{2}','{3}','{4}')".format(
                    data['doc_iddocumento'],data['aprobado_presidente'],data['aprobado_entidad'],data['fecha_aprovadopresidente'],data['fecha_aprobadoentidad']))
                rows_affects = cursor.rowcount
                id_ed = cursor.execute(
                    "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                print(rows_affects)
                connection.commit()
                if rows_affects > 0:
                   ##td = entities.TipoDocumento(id_td, data['tipdoc_nombre'])
                    idd = self.get_estado_documento_byid(id_ed)
                    return idd
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)


##reunion  
    @classmethod
    def get_reunion(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select r.reun_idreunion, r.pres_idpresidente,r.mult_idmulta,r.reun_fecha,r.reun_hora,r.reun_descripcion,r.reun_quorum,r.reun_estado,r.secretario from reunion r")
            result = cursor.fetchall()
            connection.close()
            reuniones = entities.Entities.listReunion(result)
            return reuniones
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_reunion_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select r.reun_idreunion, r.pres_idpresidente,r.mult_idmulta,r.reun_fecha,r.reun_hora,r.reun_descripcion,r.reun_quorum,r.reun_estado,r.secretario from reunion r where r.reun_idreunion={0};".format(id))
            result = cursor.fetchone()
            connection.close()
            td = [entities.Entities.reunionEntity(result)]
            return td
        except Exception as ex:
            raise Exception(ex)

  
    @classmethod
    def create_reunion(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO reunion(pres_idpresidente,mult_idmulta,reun_fecha,reun_hora,reun_descripcion,reun_quorum,reun_estado,secretario) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(
                   data['reun_idreunion'], data['pres_idpresidente'],data[' mult_idmulta'],data['reun_fecha'],data['reun_hora'],data['reun_descripcion'],data['reun_quorum'],data['reun_estado'],data['secretario'] ))
                rows_affects = cursor.rowcount
                id_td = cursor.execute(
                    "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                print(rows_affects)
                connection.commit()
                if rows_affects > 0:
                   ##td = entities.TipoDocumento(id_td, data['tipdoc_nombre'])
                    idd = self.get_reunion_byid(id_td)
                    return idd
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_reunion(self, id_reunion, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE reunion SET pres_idpresidente = '{0}',mult_idmulta = '{1}',reun_fecha = '{2}',reun_hora = '{3}',reun_descripcion = '{4}',reun_quorum = '{5}',reun_estado = '{6}',secretario = '{7}', WHERE reun_idreunion = '{8}'".format(
                    data['pres_idpresidente'],data[' mult_idmulta'],data['reun_fecha'],data['reun_hora'],data['reun_descripcion'],data['reun_quorum'],data['reun_estado'],data['secretario'],id_reunion))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    point = entities.Reunion(id_reunion,   data['pres_idpresidente'],data[' mult_idmulta'],data['reun_fecha'],data['reun_hora'],data['reun_descripcion'],data['reun_quorum'],data['reun_estado'],data['secretario'])
                    return point
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_reunion(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM reunion WHERE reun_idreunion = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Type Document deleted successfully!'}
                else:
                    return {'message': 'Error, Delete type Document failed, Type Document not found!'}
        except Exception as ex:
            raise Exception(ex)
        
  ##---------------------Yo------------------------------------
  ##--------------Multas----------
  ##-----get
    @classmethod
    def get_multas(self):
            try:
                connection = conn.get_connection()
                cursor = connection.cursor()
                cursor.execute(
                    "declare @multas nvarchar(max) set @multas = (select m.mult_idmulta, m.mult_nombre, m.mult_valor from multa m for json path ) select @multas as multas return")
                result = cursor.fetchone()
                connection.close()
                return result
            except Exception as ex:
                raise Exception(ex)

    #-----------get id

    @classmethod
    def get_multas_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select m.mult_idmulta, m.mult_nombre, m.mult_valor from multa m where m.mult_idmulta= {0} for json path;".format(id))
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)

    ##-----create 

    @classmethod
    def create_multas(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO multa(mult_nombre, mult_valor) values('{0}', '{1}')".format(
                    data['mult_nombre'], data['mult_valor']))
                rows_affects = cursor.rowcount
                id_multas = cursor.execute(
                    "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    multas = self.get_multas_byid(id_multas)
                    return multas
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    ##update
    @classmethod
    def update_multas(self, id, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE multa SET mult_nombre = '{0}', mult_valor = '{1}' WHERE mult_idmulta = '{2}'".format(
                  data['mult_nombre'], data['mult_valor'], id))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    rol = self.get_multas_byid(id)
                    return rol
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)


    #delete
    @classmethod
    def delete_multas(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM multa WHERE mult_idmulta = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Fines deleted successfully!'}
                else:
                    return {'message': 'Error, Delete fines failed, finess not found!'}
        except Exception as ex:
            raise Exception(ex)



    ##----------------------Documentos-----------------------
    ##--------get_tipoDocumentos        
    
    @classmethod
    def get_tipoDocumentos(self):
                try:
                    connection = conn.get_connection()
                    cursor = connection.cursor()
                    cursor.execute(
                        "declare @tipodoc nvarchar(max) set @tipodoc = (select td.tipdoc_id,td.tipdoc_nombre from tipo_documento td for json path ) select @tipodoc as tipodoc return")
                    result = cursor.fetchone()
                    connection.close()
                    return result
                except Exception as ex:
                    raise Exception(ex)


 ##---POR ID GET---
   
    @classmethod
    def get_tipoDocumentos_byid(self, id):
            try:
                connection = conn.get_connection()
                cursor = connection.cursor()
                cursor.execute(
                    "select td.tipdoc_id, td.tipdoc_nombre from tipo_documento td where td.tipdoc_id= '{0}' for json path;".format(id))
                result = cursor.fetchone()
                connection.close()
                return result
            except Exception as ex:
                raise Exception(ex)


 ##-----crear tipo de docuemento

    @classmethod
    def create_tipoDocumentos(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO tipo_documento(tipdoc_nombre) values('{0}')".format(
                    data['tipdoc_nombre']))
                rows_affects = cursor.rowcount
                id_tido = cursor.execute(
                    "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    rol = self.get_tipoDocumentos_byid(id_tido)
                    return rol
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_tipoDocumentos(self, id_tido, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE tipo_documento SET tipdoc_nombre = '{0}' WHERE tipdoc_id = '{1}'".format(
                    data['tipdoc_nombre'], id_tido))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    rol = self.get_tipoDocumentos_byid(id_tido)
                    return rol
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def delete_tipoDocumentos(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM tipo_documento WHERE tipdoc_id = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Tipo de documento deleted successfully!'}
                else:
                    return {'message': 'Error, Delete tipo de documento failed, tipo de documento not found!'}
        except Exception as ex:
            raise Exception(ex)

  ##-----------------tipo de servicio-----------------------------
   ###----get 
    @classmethod
    def get_tipo_servicios(self):
            try:
                connection = conn.get_connection()
                cursor = connection.cursor()
                cursor.execute(
                    "declare @tise nvarchar(max) set @tise = ( select ts.tipserv_id, ts.tipserv_nombre from tipo_servicios ts for json path ) select @tise as tise return")
                result = cursor.fetchone()
                connection.close()
                return result
            except Exception as ex:
                raise Exception(ex)
    
    ###----get id

    @classmethod
    def get_tipo_servicios_byid(self, id):
            try:
                connection = conn.get_connection()
                cursor = connection.cursor()
                cursor.execute(
                    "select ts.tipserv_id, ts.tipserv_nombre from tipo_servicios ts where ts.tipserv_id= {0} for json path;".format(id))
                result = cursor.fetchone()
                connection.close()
                return result
            except Exception as ex:
                raise Exception(ex)

    
     ###--- crear  tipo_servicios

    @classmethod
    def create_tipo_servicios(self, data):
            try:
                connection = conn.get_connection()
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO tipo_servicios(tipserv_nombre) values('{0}')".format(
                        data['tipserv_nombre']))
                    rows_affects = cursor.rowcount
                    id_ts = cursor.execute(
                        "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                    connection.commit()
                    if rows_affects > 0:
                        ts = self.get_tipo_servicios_byid(id_ts)
                        return ts
                    else:
                        return {'message': 'Error, Insert failed!'}
            except Exception as ex:
                raise Exception(ex)


  ###--- actualizar  tipo_servicios
 
    @classmethod
    def update_tipo_servicio(self, id, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE tipo_servicios SET tipserv_nombre = '{0}' WHERE tipserv_id = '{1}'".format(
                    data['tipserv_nombre'], id))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    ts = self.get_tipo_servicios_byid(id)
                    return ts
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)

  ###--- eliminar  tipo_servicios
    @classmethod
    def delete_tipo_servicio(self, id):
            try:
                connection = conn.get_connection()
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM tipo_servicios WHERE tipserv_id = '{0}'".format(id))
                    row_affects = cursor.rowcount
                    connection.commit()
                    if row_affects > 0:
                        return {'message': 'Type service deleted successfully!'}
                    else:
                        return {'message': 'Error, Delete servicio failed, type service not found!'}
            except Exception as ex:
                raise Exception(ex)

    ##-------------------------------------SERVICIOS----------------------

     ##-----get Servicios
    @classmethod
    def get_servicio(self):
            try:
                connection = conn.get_connection()
                cursor = connection.cursor()
                cursor.execute(
               ## "declare @servicio nvarchar(max) set @servicio = (select s.serv_idservicios as 'servicios.serv_idservicios', s.s as 'serv_idservicios.s', p.eje_focal as 'parabola.eje_focal', v.id_punto as 'vertice.id_punto', v.coord_x as 'vertice.coord_x', v.coord_y as 'vertice.coord_y' from parabola p inner join punto v on p.vertice = v.id_punto for json path) select @parabolas as parabolas return")
                "declare @servicio nvarchar(max) set @servicio = ( select s.serv_idservicios, s.tipserv_id, s.serv_nombreservicio, s.serv_descripcion, s.serv_valor, s.serv_iva, s.serv_cantidad from servicios s for json path ) select @servicio as servicio return")
                result = cursor.fetchone()
                connection.close()
                return result
            except Exception as ex:
                raise Exception(ex)

    ##-----get servidicos id

    @classmethod
    def get_servicio_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select s.serv_idservicios, s.tipserv_id, s.serv_nombreservicio, s.serv_descripcion, s.serv_valor, s.serv_iva, s.serv_cantidad from servicios s where s.serv_idservicios= {0} for json path;".format(id))
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)

    ##--------- create servicios

    @classmethod
    def create_servicios(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO servicios(tipserv_id, serv_nombreservicio, serv_descripcion, serv_valor, serv_iva, serv_cantidad) values('{0}', '{1}','{2}', '{3}','{4}', '{5}')".format(
                    data['tipserv_id'], data['serv_nombreservicio'], data['serv_descripcion'], data['serv_valor'], data['serv_iva'], data['serv_cantidad']))
                rows_affects = cursor.rowcount
                id_servicio = cursor.execute(
                    "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    servicio = self.get_servicio_byid(id_servicio)
                    return servicio
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

  ##--------- create servicios
    @classmethod
    def update_servicios(self, id_servicios, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE servicios SET tipserv_id = '{0}', serv_nombreservicio = '{1}' , serv_descripcion = '{2}', serv_valor = '{3}', serv_iva = '{4}', serv_cantidad = '{5}'WHERE serv_idservicios = '{6}'".format(
                    data['tipserv_id'], data['serv_nombreservicio'],  data['serv_descripcion'], data['serv_valor'],  data['serv_iva'], data['serv_cantidad'], id_servicios))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    servicios = self.get_servicio_byid(id_servicios)
                    return servicios
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)


    ##-----------delete servicios

    @classmethod
    def delete_servicios(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM servicios WHERE serv_idservicios = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Service deleted successfully!'}
                else:
                    return {'message': 'Error, Delete service failed, service not found!'}
        except Exception as ex:
            raise Exception(ex)
  
    ##------------------------RESERVACIONES--------------------
     ## get reservaciones
    @classmethod
    def get_reservaciones(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "declare @reservacion nvarchar(max) set @reservacion = ( select r.resv_idreservacion, r.serv_idservicios, r.resv_fecha, r.resv_descripcion from reservaciones r for json path ) select @reservacion as reservacion return")
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)

    ## get_id reservaciones
    @classmethod
    def get_reservaciones_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select r.resv_idreservacion, r.serv_idservicios, r.resv_fecha, r.resv_descripcion from reservaciones r where r.resv_idreservacion= {0} for json path;".format(id))
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)

    ## create reservaciones
    @classmethod
    def create_reservaciones(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO reservaciones(serv_idservicios, resv_fecha, resv_descripcion) values('{0}', '{1}','{2}')".format(
                    data['serv_idservicios'], data['resv_fecha'],data['resv_descripcion']))
                rows_affects = cursor.rowcount
                id_reservaciones = cursor.execute(
                    "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    rol = self.get_reservaciones_byid(id_reservaciones)
                    return rol
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    #---update reservaciones       

    @classmethod
    def update_reservaciones(self, id_rol, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE reservaciones SET serv_idservicios = '{0}', resv_fecha = '{1}', resv_descripcion = '{2}' WHERE rol_idrol = '{3}'".format(
                    data['serv_idservicios'], data['resv_fecha'], data['resv_descripcion'], id_rol))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    reservaciones = self.get_reservaciones_byid(id_rol)
                    return reservaciones
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)

    ## delete reservaciones

    @classmethod
    def delete_reservaciones(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM reservaciones WHERE resv_idreservacion = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Booking deleted successfully!'}
                else:
                    return {'message': 'Error, Delete booking failed, booking not found!'}
        except Exception as ex:
            raise Exception(ex)
    

    ##------------------------ALICUOTA ACTUALIZADA--------------------
     ## get alicuota actualizada
    @classmethod
    def get_alicuotaActualizada(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "declare @alicuotaac nvarchar(max) set @alicuotaac = ( select a.alic_id, a.alic_idalicuota, a.alic_valor, a.alic_fecha from alicuota_actualizada a for json path ) select @alicuotaac as alicuotaac return")
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)


    ## get id alicuota actualizada       
    @classmethod
    def get_alicuotaActualizada_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select a.alic_id, a.alic_idalicuota, a.alic_valor, a.alic_fecha  from alicuota_actualizada a where a.alic_id= {0} for json path;".format(id))
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)
    
    ##create alicuota actualizada////errorrrrrrr

    @classmethod
    def create_alicuotaActualizada(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO alicuota_actualizada( alic_valor, alic_fecha ) values('{0}', '{1}')".format(
                data['alic_valor'], data['alic_fecha']))
                rows_affects = cursor.rowcount
                id_ac = cursor.execute(
                    "SELECT @@IDENTITY AS 'Identity'").fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    ac = self.get_alicuotaActualizada_byid(id_ac)
                    return ac
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    #---update ralicuotaac

    @classmethod
    def update_alicuotaActualizada(self, id_rol, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE alicuota_actualizada SET alic_idalicuota = '{0}', alic_valor = '{1}', alic_fecha = '{3}' WHERE alic_id = '{3}'".format(
                    data['alic_idalicuota'], data['alic_valor'], data['alic_fecha'], id_rol))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    ac = self.get_alicuotaActualizada_byid(id_rol)
                    return ac
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)
        
    ##---delete alicuotaac
    
    @classmethod
    def delete_alicuotaActualizada(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM alicuota_actualizada WHERE alic_id = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Aliquot deleted successfully!'}
                else:
                    return {'message': 'Error, Delete Aliquot failed, User rol not found!'}
        except Exception as ex:
            raise Exception(ex)