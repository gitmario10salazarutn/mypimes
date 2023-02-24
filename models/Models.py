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
            person = entities.Entities.personaEntity(result)
            return person
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_persona(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO persona(pers_persona, pers_email, pers_nombres, pers_apellidos, pers_telefono, pers_direccion) values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}') RETURNING pers_persona".format(
                    data['pers_persona'], data['pers_email'], data['pers_nombres'], data['pers_apellidos'], data['pers_telefono'], data['pers_direccion']))
                rows_affects = cursor.rowcount
                id_persona = cursor.fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    persona = self.get_persona_byid(id_persona)
                    return persona
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
                    persona = self.get_persona_byid(id_persona)[0]
                    return persona
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
                cursor.execute("INSERT INTO rol_usuario(rol_nombrerol, prefijo) values('{0}', '{1}')RETURNING rol_idrol".format(
                    data['rol_nombrerol'], data['prefijo']))
                rows_affects = cursor.rowcount
                id_rol = cursor.fetchone()[0]
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
                    return {'message': 'Error, Delete rol user failed, User rol not found!'}
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
                f = datetime.now()
                fecha = "{0}/{1}/{2}".format(f.month, f.day, f.year)
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
                #fecha = datetime.strptime(data['user_fecha'], '%d/%m/%Y')
                password = data['user_password']
                hashed = generate_password_hash(password)
                cursor.execute(
                    "INSERT INTO user_usuario(user_idusuario, rol_idrol, pers_persona, user_password, user_estado, user_fecha) values('{0}', {1}, '{2}','{3}', '{4}', '{5}')".format(iduser, data['rol_idrol'], data['pers_persona'], hashed, 0, fecha))
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
                        "user_estado": 0,
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
                u = rol[0]
                id = u['prefijo']+id_user[4:]
                user_to_assign = self.get_usuario_byid(id)
                user = self.get_usuario_byid(id_user)
                if user and user_to_assign[0] is None:
                    pers = user[0]
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
                    password = pers['user_password']
                    hashed = generate_password_hash(password)
                    da = {
                        "user_idusuario": iduser,
                        "user_password": hashed,
                        "user_estado": pers['user_estado'],
                        "user_email": pers['persona'].get('pers_email')
                    }
                    cursor.execute(
                        "INSERT INTO user_usuario(user_idusuario, rol_idrol, pers_persona, user_password, user_estado, user_fecha) values('{0}', {1}, '{2}', '{3}', {4}, '{5}')".format(iduser, data['rol_idrol'], pers['persona'].get('pers_persona'), hashed, pers['user_estado'], fecha))
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
    def login(self, data):
        try:
            user_found = self.get_usuario_byid(data['username']) #data['user_idusuario']
            if user_found[0]:
                user = user_found[0]
                check_password = check_password_hash(user['user_password'], data['password']) #data['password']
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

    # Detalle Reservaciones

    @classmethod
    def get_detalle_reservaciones(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select*from get_detalle_reservaciones gdr")
            result = cursor.fetchall()
            connection.close()
            a = entities.Entities.listDetalleReservaciones(result)
            return a
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_detalle_reservaciones_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select*from get_detalle_reservaciones a where a.detres_iddetalle= {0};".format(id))
            result = cursor.fetchone()
            connection.close()
            a = [entities.Entities.detalleReservacionesEntity(result)]
            return a
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def create_detalle_reservacion(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into detalle_reservaciones (reservacion, detres_subtotal, detres_iva, detres_total, detres_cantidad, detres_horainicio, detres_horafin, detres_fecha, estado_delete_detres, detres_cabreservacion) values({0}, {1}, {2}, {3}, {4}, '{5}', '{6}', '{7}', '{8}', {9}) returning detres_iddetalle;".format(data['reservacion'], data['detres_subtotal'], data['detres_iva'], data['detres_total'], data['detres_cantidad'], data['detres_horainicio'], data['detres_horafin'], data['detres_fecha'], data['estado_delete_detres'], data['detres_cabreservacion']))
                rows_affects = cursor.rowcount
                id = cursor.fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    a = self.get_detalle_reservaciones_byid(id)
                    return a
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_detalle_reservacion(self, id, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE detalle_reservaciones SET reservacion = {0}, detres_subtotal = {1}, detres_iva = {2}, detres_total = {3}, detres_cantidad = {4}, detres_horainicio = '{5}', detres_horafin = '{6}', detres_fecha = '{7}', estado_delete_detres = '{8}', detres_cabreservacion = {9} WHERE detres_iddetalle = {10}".format(data['reservacion'], data['detres_subtotal'], data['detres_iva'], data['detres_total'], data['detres_cantidad'], data['detres_horainicio'], data['detres_horafin'], data['detres_fecha'], data['estado_delete_detres'], data['detres_cabreservacion'], id))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a   = self.get_detalle_reservaciones_byid(id)[0]
                    return a
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_detalle_reservacion(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM detalle_reservaciones WHERE detres_iddetalle = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Detalle Reservaciones deleted successfully!'}
                else:
                    return {'message': 'Error, Delete detalle Reservaciones failed, Detalle Reservaciones not found!'}
        except Exception as ex:
            raise Exception(ex)



# **************************************************************************************************

    # Alicuotas


    @classmethod
    def get_alicuotas(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_alicuotas")
            result = cursor.fetchall()
            connection.close()
            alicuotas = entities.Entities.listAlicuotas(result)
            return alicuotas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_alicuota_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_alicuotas p where p.id_alicuota = {0};".format(id))
            result = cursor.fetchone()
            connection.close()
            person = [entities.Entities.alicuotaEntity(result)]
            return person
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_alicuota(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into alicuota (mult_idmulta, ali_fecha_actualizacion, ali_valor_anterior, ali_valor_actual, estado_delete_alicuota) values({0}, '{1}', {2}, {3}, '{4}') returning ali_idalicuota;".format(
                    data['mult_idmulta'], data['ali_fecha_actualizacion'], data['ali_valor_anterior'], data['ali_valor_actual'], data['estado_delete_alicuota']))
                rows_affects = cursor.rowcount
                id = cursor.fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    a = self.get_alicuota_byid(id)
                    return a
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_alicuota(self, id, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE alicuota SET mult_idmulta = {0}, ali_fecha_actualizacion = '{1}', ali_valor_anterior = {2}, ali_valor_actual = {3}, estado_delete_alicuota = '{4}' WHERE ali_idalicuota = '{5}'".format(data['mult_idmulta'], data['ali_fecha_actualizacion'], data['ali_valor_anterior'], data['ali_valor_actual'], data['estado_delete_alicuota'], id))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a   = self.get_alicuota_byid(id)[0]
                    return a
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_alicuota(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM alicuota WHERE ali_idalicuota = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Alicuota deleted successfully!'}
                else:
                    return {'message': 'Error, Delete alicuota failed, person not found!'}
        except Exception as ex:
            raise Exception(ex)


# **************************************************************************************************

    # Pago Alicuotas


    @classmethod
    def get_pago_alicuotas(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_pago_alicuotas")
            result = cursor.fetchall()
            connection.close()
            alicuotas = entities.Entities.listPagoAlicuotas(result)
            return alicuotas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_pago_alicuota_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_pago_alicuotas p where p.pagali_id_gpa = {0};".format(id))
            result = cursor.fetchone()
            connection.close()
            person = [entities.Entities.pago_alicuotaEntity(result)]
            return person
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_pago_alicuota(self, subtotal, iva, total, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                f = datetime.now()
                fecha = "{0}/{1}/{2}".format(f.month, f.day, f.year)
                cursor.execute("insert into pago_alicuota (tes_idtesorero, cond_idcondomino, pagali_fecha, pagali_numero, pagali_subtotal, pagali_iva, pagali_total, estado_delete_pagali)  values({0}, {1}, '{2}', '{3}', {4}, {5}, {6}, '{7}') returning pagali_id".format(data['tes_idtesorero'], data['cond_idcondomino'],fecha, data['pagali_numero'], subtotal, iva, total, 'False'))
                rows_affects = cursor.rowcount
                id = cursor.fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    a = self.get_pago_alicuota_byid(id)
                    return a
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_pago_alicuota(self, id, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE pago_alicuota SET tes_idtesorero = {0}, cond_idcondomino = {1}, pagali_fecha = '{2}', pagali_numero = '{3}', pagali_subtotal = {4}, pagali_iva = {5}, pagali_total = {6}, estado_delete_pagali = '{7}' WHERE pagali_id = '{8}'".format(data['tes_idtesorero'], data['cond_idcondomino'], data['pagali_fecha'], data['pagali_numero'], data['pagali_subtotal'], data['pagali_iva'], data['pagali_total'], data['estado_delete_pagali'], id))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a   = self.get_pago_alicuota_byid(id)[0]
                    return a
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_pago_alicuota(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM pago_alicuota WHERE pagali_id = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Pago Alicuota deleted successfully!'}
                else:
                    return {'message': 'Error, Delete pago alicuota failed, Pago alicuota not found!'}
        except Exception as ex:
            raise Exception(ex)


# **************************************************************************************************

    # Detalle Pago

    @classmethod
    def get_detalle_pagos(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_detalle_pagos")
            result = cursor.fetchall()
            connection.close()
            dp = entities.Entities.listDetallePagos(result)
            return dp
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_detalle_pago_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_detalle_pagos p where p.detpag_id = {0};".format(id))
            result = cursor.fetchone()
            connection.close()
            dp = [entities.Entities.detallePagoEntity(result)]
            return dp
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_detalle_pago(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into detalle_pago (pagali_id, aliact_id, detpag_subtotal, detpag_iva, detpag_total, detpag_fecha, detpag_multa, estado_delete_detpag)  values({0}, {1}, {2}, {3}, {4}, '{5}', {6}, '{7}') returning detpag_id".format(data['pagali_id'], data['aliact_id'], data['detpag_subtotal'], data['detpag_iva'], data['detpag_total'], data['detpag_fecha'], data['detpag_multa'], data['estado_delete_detpag']))
                rows_affects = cursor.rowcount
                id = cursor.fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    a = self.get_detalle_pago_byid(id)
                    return a
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_detalle_pago(self, id, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE detalle_pago SET pagali_id = {0}, aliact_id = {1}, detpag_subtotal = {2}, detpag_iva = {3}, detpag_total = {4}, detpag_fecha = '{5}', detpag_multa = {6}, estado_delete_detpag = '{7}' WHERE detpag_id = '{8}'".format(data['pagali_id'], data['aliact_id'], data['detpag_subtotal'], data['detpag_iva'], data['detpag_total'], data['detpag_fecha'], data['detpag_multa'], data['estado_delete_detpag'], id))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a   = self.get_detalle_pago_byid(id)[0]
                    return a
                else:
                    return {'message': 'Error, Update failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_detalle_pago(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM detalle_pago WHERE detpag_id = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Detalle Pago deleted successfully!'}
                else:
                    return {'message': 'Error, Delete detalle pago failed, Pago alicuota not found!'}
        except Exception as ex:
            raise Exception(ex)



# **************************************************************************************************

    # Egresos


    @classmethod
    def get_egresos(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_egresos")
            result = cursor.fetchall()
            connection.close()
            dp = entities.Entities.listEgresos(result)
            return dp
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_egreso_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_egresos p where p.egre_id_ge = {0};".format(id))
            result = cursor.fetchone()
            connection.close()
            dp = [entities.Entities.egresosEntity(result)]
            return dp
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def getCountEgresos(self):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                
                cursor.execute("select max(cr.egre_id) from egresos cr ;")
                num = cursor.fetchone()[0]
                return num
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_egreso(self,subtotal, iva, total, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                numero = self.getCountEgresos() + 1
                f = datetime.now()
                fecha = "{0}/{1}/{2}".format(f.month, f.day, f.year)
                cursor.execute("insert into egresos (tes_idtesorero, egre_descripcion, egre_subtotal, egre_iva, egre_total, egre_fecha,egre_numero, estado_delete_egr)  values({0}, '{1}', {2}, {3}, {4}, '{5}', '{6}', '{7}') returning egre_id".format(data['tes_idtesorero'], data['egre_descripcion'], subtotal, iva, total, fecha, numero, 'False'))
                rows_affects = cursor.rowcount
                id = cursor.fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    a = self.get_egreso_byid(id)
                    return a
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_egreso(self, id, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE egresos SET tes_idtesorero = {0}, egre_descripcion = '{1}', egre_subtotal = {2}, egre_iva = {3}, egre_total = {4}, egre_fecha = '{5}', egre_numero = '{6}', estado_delete_egr = '{7}' WHERE egre_id = '{8}'".format(data['tes_idtesorero'], data['egre_descripcion'], data['egre_subtotal'], data['egre_iva'], data['egre_total'], data['egre_fecha'], data['egre_numero'], data['estado_delete_egr'], id))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a   = self.get_egreso_byid(id)[0]
                    return a
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_egreso(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM egresos WHERE egre_id = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Egreso deleted successfully!'}
                else:
                    return {'message': 'Error, Delete Egreso failed, Egreso not found!'}
        except Exception as ex:
            raise Exception(ex)



# **************************************************************************************************

    # Detalle Egresos


    @classmethod
    def get_detalle_egresos(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_detalle_egresos")
            result = cursor.fetchall()
            connection.close()
            dp = entities.Entities.listDetalleEgresos(result)
            return dp
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_detalle_egreso_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_detalle_egresos p where p.detegre_id = {0};".format(id))
            result = cursor.fetchone()
            connection.close()
            dp = [entities.Entities.detalleEgresoEntity(result)]
            return dp
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_detalle_egreso(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into detalle_egresos (egre_id, detegre_numerofactura, detegre_valorfactura, deteegre_documento, detegre_subtotal, detegre_iva, detegre_total, detegre_fecha, estado_delete_detegre) values({0}, '{1}', {2}, {3}, {4}, {5}, {6}, '{7}', '{8}') returning detegre_id".format(data['egre_id'], data['detegre_numerofactura'], data['detegre_valorfactura'], data['deteegre_documento'], data['detegre_subtotal'], data['detegre_iva'], data['detegre_total'], data['detegre_fecha'], data['estado_delete_detegre']))
                rows_affects = cursor.rowcount
                id = cursor.fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    a = self.get_detalle_egreso_byid(id)
                    return a
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_detalle_egreso(self, id, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE detalle_egresos SET egre_id = {0}, detegre_numerofactura = '{1}', detegre_valorfactura = {2}, deteegre_documento = {3}, detegre_subtotal = {4}, detegre_iva = {5}, detegre_total = {6}, detegre_fecha = '{7}', estado_delete_detegre = '{8}' WHERE detegre_id = '{9}'".format(data['egre_id'], data['detegre_numerofactura'], data['detegre_valorfactura'], data['deteegre_documento'], data['detegre_subtotal'], data['detegre_iva'], data['detegre_total'], data['detegre_fecha'], data['estado_delete_detegre'], id))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a   = self.get_detalle_egreso_byid(id)[0]
                    return a
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_detalle_egreso(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM detalle_egresos WHERE detegre_id = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Detalle Egreso deleted successfully!'}
                else:
                    return {'message': 'Error, Delete Detalle Egreso failed, Egreso not found!'}
        except Exception as ex:
            raise Exception(ex)


# **************************************************************************************************

    # Cabecera Reservaciones

    @classmethod
    def get_cabecera_reservaciones(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select * from get_cabreservaciones gc;")
            result = cursor.fetchall()
            connection.close()
            dp = entities.Entities.listCabeceraReservaciones(result)
            return dp
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_cabecera_reservacion_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_cabreservaciones p where p.id_cabreservacion = {0};".format(id))
            result = cursor.fetchone()
            connection.close()
            dp = [entities.Entities.cabeceraRecervacionesEntity(result)]
            return dp
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def getCountReservaciones(self):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                
                cursor.execute("select max(cr.id_cabreservacion) from cabecera_reservacion cr ;")
                num = cursor.fetchone()[0]
                return num
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_cabecera_reservacion(self,subtotal, iva, total, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                numero = self.getCountReservaciones() + 1
                f = datetime.now()
                fecha = "{0}/{1}/{2}".format(f.month, f.day, f.year)
                cursor.execute("insert into cabecera_reservacion (cabres_secretario, cabres_condomino, cabres_subtotal, cabres_iva, cabres_total, cabres_numero, cabres_fecha) values({0}, {1}, {2}, {3}, {4}, '{5}', '{6}') returning id_cabreservacion;".format(data['cabres_secretario'], data['cabres_condomino'], subtotal, iva, total, numero, fecha))
                rows_affects = cursor.rowcount
                id = cursor.fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    a = self.get_cabecera_reservacion_byid(id)
                    return a
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_cabecera_reservacion(self, id, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE cabecera_reservacion SET cabres_secretario = {0}, cabres_condomino = {1}, cabres_subtotal = {2}, cabres_iva = {3}, cabres_total = {4}, cabres_numero = '{5}', cabres_fecha = '{6}' WHERE id_cabreservacion = {7}".format(data['cabres_secretario'], data['cabres_condomino'], data['cabres_subtotal'], data['cabres_iva'], data['cabres_total'], data['cabres_numero'], data['cabres_fecha'], id))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    a   = self.get_cabecera_reservacion_byid(id)[0]
                    return a
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_cabecera_reservacion(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM cabecera_reservacion WHERE id_cabreservacion = '{0}'".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return {'message': 'Cabecera reservacion deleted successfully!'}
                else:
                    return {'message': 'Error, Delete Cabecera reservacion failed, Cabecera reservacion not found!'}
        except Exception as ex:
            raise Exception(ex)

# **************************************************************************************************

    @classmethod
    def add_detail_reserv(self, data, list_det_reserv: list) -> list:
        try:
            if data:
                dr = []
                reservacion = self.get_reservaciones_byid(data['reservacion'])
                serv_valor = reservacion[0].get('servicios').get('serv_valor')
                serv_iva = reservacion[0].get('servicios').get('serv_iva')
                dr.append(data['reservacion'])
                dr.append(None)
                total = data['cantidad'] * serv_valor
                subtotal = total / ((100 + serv_iva)/100)
                iva = total - subtotal
                f = datetime.now()
                fecha = "{0}/{1}/{2}".format(f.month, f.day, f.year)
                dr.append(subtotal)
                dr.append(iva)
                dr.append(total)
                dr.append(data['cantidad'])
                dr.append(data['hora_inicio'])
                dr.append(data['hora_fin'])
                dr.append(fecha)
                dr.append('False')
                list_det_reserv.append(entities.Entities.Detalle_Reservaciones(dr))
                return list_det_reserv
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_detail_pago(self, data, list_det_pago: list) -> list:
        try:
            if data:
                dr = []
                ali_act = self.get_alicuotaActualizada_byid(data['aliact_id'])
                alic_valor = ali_act[0].get('alicuota').get('ali_valor_actual')
                dr.append(None)
                dr.append(data['aliact_id'])
                total = float(alic_valor)
                subtotal = total / ((100 + 12)/100)
                iva = total - subtotal
                f = datetime.now()
                fecha = "{0}/{1}/{2}".format(f.month, f.day, f.year)
                dr.append(subtotal)
                dr.append(iva)
                dr.append(total)
                dr.append(fecha)
                dr.append(data['detpag_multa'])
                dr.append('False')
                list_det_pago.append(entities.Entities.Detalle_Pago(dr))
                return list_det_pago
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def add_detail_egreso(self, data, list_det_egreso: list) -> list:
        try:
            if data:
                dr = []
                dr.append(None)
                dr.append(data['detegre_numerofactura'])
                f = datetime.now()
                fecha = "{0}/{1}/{2}".format(f.month, f.day, f.year)
                dr.append(data['detegre_valorfactura'])
                dr.append(data['deteegre_documento'])
                dr.append(data['detegre_subtotal'])
                dr.append(data['detegre_iva'])
                dr.append(data['detegre_total'])
                dr.append(fecha)
                dr.append('False')
                list_det_egreso.append(entities.Entities.Detalle_Egreso(dr))
                return list_det_egreso
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


# **************************************************************************************************

    @classmethod
    def get_multas(self):
            try:
                connection = conn.get_connection()
                cursor = connection.cursor()
                cursor.execute(
                    "select m.mult_idmulta, m.mult_nombre, m.mult_valor from multa m")
                result = cursor.fetchall()
                connection.close()
                m = entities.Entities.listMultas(result)
                return m
            except Exception as ex:
                raise Exception(ex)

    #-----------get id

    @classmethod
    def get_multas_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select m.mult_idmulta, m.mult_nombre, m.mult_valor from multa m where m.mult_idmulta= {0};".format(id))
            result = cursor.fetchone()
            m = [entities.Entities.multaEntity(result)]
            connection.close()
            return m
        except Exception as ex:
            raise Exception(ex)

    ##-----create 

    @classmethod
    def create_multas(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO multa(mult_nombre, mult_valor) values('{0}', '{1}') RETURNING mult_idmulta".format(
                    data['mult_nombre'], data['mult_valor']))
                rows_affects = cursor.rowcount
                id_multas = cursor.fetchone()[0]
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
                        "select td.tipdoc_id,td.tipdoc_nombre from tipo_documento td")
                    result = cursor.fetchall()
                    connection.close()
                    td = entities.Entities.listTipoDocumentos(result)
                    return td
                except Exception as ex:
                    raise Exception(ex)


 ##---POR ID GET---
   
    @classmethod
    def get_tipoDocumentos_byid(self, id):
            try:
                connection = conn.get_connection()
                cursor = connection.cursor()
                cursor.execute(
                    "select td.tipdoc_id, td.tipdoc_nombre from tipo_documento td where td.tipdoc_id= '{0}';".format(id))
                result = cursor.fetchone()
                connection.close()
                td = [entities.Entities.tipodocumentoEntity(result)]
                return td
            except Exception as ex:
                raise Exception(ex)


 ##-----crear tipo de docuemento

    @classmethod
    def create_tipoDocumentos(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO tipo_documento(tipdoc_nombre) values('{0}') RETURNING tipdoc_id".format(
                    data['tipdoc_nombre']))
                rows_affects = cursor.rowcount
                id_tido = cursor.fetchone()[0]
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
                    "select ts.tipserv_id, ts.tipserv_nombre from tipo_servicios ts")
                result = cursor.fetchall()
                connection.close()
                ts = entities.Entities.listTipoServicios(result)
                return ts
            except Exception as ex:
                raise Exception(ex)
    
    ###----get id

    @classmethod
    def get_tipo_servicios_byid(self, id):
            try:
                connection = conn.get_connection()
                cursor = connection.cursor()
                cursor.execute(
                    "select ts.tipserv_id, ts.tipserv_nombre from tipo_servicios ts where ts.tipserv_id= {0};".format(id))
                result = cursor.fetchone()
                ts = [entities.Entities.tipoServicioEntity(result)]
                connection.close()
                return ts
            except Exception as ex:
                raise Exception(ex)

    
     ###--- crear  tipo_servicios

    @classmethod
    def create_tipo_servicios(self, data):
            try:
                connection = conn.get_connection()
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO tipo_servicios(tipserv_nombre) values('{0}') RETURNING tipserv_id".format(
                        data['tipserv_nombre']))
                    rows_affects = cursor.rowcount
                    id_ts = cursor.fetchone()[0]
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
    def get_servicios(self):
            try:
                connection = conn.get_connection()
                cursor = connection.cursor()
                cursor.execute(
                "select * from get_servicios")
                result = cursor.fetchall()
                connection.close()
                serv = entities.Entities.listServicios(result)
                return serv
            except Exception as ex:
                raise Exception(ex)

    ##-----get servidicos id

    @classmethod
    def get_servicio_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_servicios s where s.serv_idservicios= {0};".format(id))
            result = cursor.fetchone()
            serv = [entities.Entities.serviciosEntity(result)]
            connection.close()
            return serv
        except Exception as ex:
            raise Exception(ex)

    ##--------- create servicios

    @classmethod
    def create_servicios(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO servicios(tipserv_id, serv_nombreservicio, serv_descripcion, serv_valor, serv_iva, serv_cantidad) values('{0}', '{1}','{2}', '{3}','{4}', '{5}') RETURNING serv_idservicios".format(
                    data['tipserv_id'], data['serv_nombreservicio'], data['serv_descripcion'], data['serv_valor'], data['serv_iva'], data['serv_cantidad']))
                rows_affects = cursor.rowcount
                id_servicio = cursor.fetchone()[0]
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
                "select*from get_reservaciones")
            result = cursor.fetchall()
            connection.close()
            r = entities.Entities.listReservaciones(result)
            return r
        except Exception as ex:
            raise Exception(ex)

    ## get_id reservaciones
    @classmethod
    def get_reservaciones_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select*from get_reservaciones r where r.resv_idreservacion= {0} ".format(id))
            result = cursor.fetchone()
            connection.close()
            r = [entities.Entities.reservacionesEntity(result)]
            return r
        except Exception as ex:
            raise Exception(ex)

    ## create reservaciones
    @classmethod
    def create_reservaciones(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO reservaciones(serv_idservicios, resv_fecha, resv_descripcion) values('{0}', '{1}','{2}') RETURNING resv_idreservacion".format(
                    data['serv_idservicios'], data['resv_fecha'],data['resv_descripcion']))
                rows_affects = cursor.rowcount
                id_reservaciones = cursor.fetchone()[0]
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
                cursor.execute("UPDATE reservaciones SET serv_idservicios = '{0}', resv_fecha = '{1}', resv_descripcion = '{2}' WHERE resv_idreservacion = '{3}'".format(
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
    def get_alicuotaActualizadas(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select*from get_alicuota_actualizada")
            result = cursor.fetchall()
            connection.close()
            a = entities.Entities.listAlicuotasActualizadas(result)
            return a
        except Exception as ex:
            raise Exception(ex)


    ## get id alicuota actualizada       
    @classmethod
    def get_alicuotaActualizada_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select*from get_alicuota_actualizada a where a.alic_id= {0};".format(id))
            result = cursor.fetchone()
            connection.close()
            a = [entities.Entities.alicuota_actualizadaEntity(result)]
            return a
        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def create_alicuotaActualizada(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO alicuota_actualizada(alic_idalicuota, alic_valor, alic_fecha) values({0}, {1}, '{2}') RETURNING alic_id".format(data['alic_idalicuota'], data['alic_valor'], data['alic_fecha']))
                rows_affects = cursor.rowcount
                id_ac = cursor.fetchone()[0]
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
                cursor.execute("UPDATE alicuota_actualizada SET alic_idalicuota = {0}, alic_valor = {1}, alic_fecha = '{2}' WHERE alic_id = '{3}'".format(
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



    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    #SECRETARIO

    # Documento
    @classmethod
    def get_documentos(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_documentos doc")
            result = cursor.fetchall()
            connection.close()
            documentos = entities.Entities.listDocumentos(result)
            return documentos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_documentosv2(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select doc.doc_iddocumento,td.tipdoc_id,td.tipdoc_nombre,s.sec_idsecretario,doc.doc_descripcion,doc.doc_documento,doc.doc_entidad,doc.doc_recibido,doc.estado_delete_docs from documentos doc JOIN tipo_documento td ON doc.tipo_documento=td.tipdoc_id INNER JOIN  secretario s on doc.sec_idsecretario=s.sec_idsecretario")
            result = cursor.fetchall()
            connection.close()
            documentos = entities.Entities.listDocumentos(result)
            return documentos
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_documento_byid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_documentos doc where doc.doc_iddocumento = {0}".format(id))
            result = cursor.fetchone()
            connection.close()
            documentos = entities.Entities.documentoEntity(result)
            return documentos
        except Exception as ex:
            raise Exception(ex)

#Metodos para presidente ----------------------------------------
    @classmethod
    def get_documento_byTipoDoc(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_documentos where tipo_documento = {0}".format(id))
            result = cursor.fetchall()
            connection.close()
            documentos = entities.Entities.listDocumentos(result)
            return documentos
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_documento_byEstado(self, estado):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_documentos where estado_delete_docs = '{0}'".format(estado))
            result = cursor.fetchall()
            connection.close()
            documentos = entities.Entities.listDocumentos(result)
            return documentos
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_documento_byTipoDocAndEstado(self, id,estado):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from get_documentos where tipo_documento = {0} and estado_delete_docs ='{1}'".format(id,estado))
            result = cursor.fetchall()
            connection.close()
            documentos = entities.Entities.listDocumentos(result)
            return documentos
        except Exception as ex:
            raise Exception(ex)



      
#Metodos para presidente ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    @classmethod
    def create_documentos(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO documentos(tipo_documento,sec_idsecretario,doc_descripcion,doc_documento,doc_entidad,doc_recibido) values('{0}', '{1}','{2}', '{3}','{4}','{5}') RETURNING doc_iddocumento".format(
                    data['tipdoc_id'], data['sec_idsecretario'],data['doc_descripcion'],data['doc_documento'],data['doc_entidad'],data['doc_recibido']))
                rows_affects = cursor.rowcount
                id_d = cursor.fetchone()[0]
                connection.commit()
                if rows_affects > 0:
                    d = self.get_documento_byid(id_d)
                    return d
                else:
                    return {'message': 'Error, Insert failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_documento(self, doc_iddocumento, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE documentos SET tipo_documento = '{0}',sec_idsecretario='{1}',doc_descripcion='{2}',doc_documento='{3}',doc_entidad='{4}',doc_recibido='{5}' WHERE doc_iddocumento = '{6}'".format(data['tipdoc_id'], data['sec_idsecretario'], data['doc_descripcion'], data['doc_documento'], data['doc_entidad'], data['doc_recibido'], doc_iddocumento))
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    d = self.get_documento_byid(doc_iddocumento)
                    return d
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
                cursor.execute("INSERT INTO estado_documentos(doc_iddocumento,aprobado_presidente,aprobado_entidad,fecha_aprovadopresidente,fecha_aprobadoentidad) values('{0}','{1}','{2}','{3}','{4}') returning estdoc_id".format(
                    data['doc_iddocumento'],data['aprobado_presidente'],data['aprobado_entidad'],data['fecha_aprovadopresidente'],data['fecha_aprobadoentidad']))
                rows_affects = cursor.rowcount
                id_ed = cursor.fetchone()[0]
                connection.commit()
                if rows_affects > 0:
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
                "select * from get_reuniones r")
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
                "select * from get_reuniones r where r.reun_idreunion={0};".format(id))
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
                cursor.execute("INSERT INTO reunion(pres_idpresidente,mult_idmulta,reun_fecha,reun_hora,reun_descripcion,reun_quorum,reun_estado,secretario) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}') RETURNING reun_idreunion".format(
                   data['reun_idreunion'], data['pres_idpresidente'],data[' mult_idmulta'],data['reun_fecha'],data['reun_hora'],data['reun_descripcion'],data['reun_quorum'],data['reun_estado'],data['secretario'] ))
                rows_affects = cursor.rowcount
                id_td = cursor.fetchone()[0]
                connection.commit()
                if rows_affects > 0:
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
                    r = self.get_reunion_byid(id_reunion)
                    return r
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
