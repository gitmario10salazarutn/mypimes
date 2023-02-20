"""# -*- coding: utf-8 -*-

Created on Tue Oct 11 22:55:25 2022

@author: Mario
"""
from flask_cors import CORS
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for
from flask_mongoengine import MongoEngine
from werkzeug.utils import secure_filename
import os
import urllib.request
from config import config
from models import Models as model
from database import connectdb as conn
import gridfs

main = Flask(__name__)
main.secret_key = "mario10salazar"
CORS(main)

@main.route('/get_user_byid/<id_user>', methods=['GET'])
def get_user_byid(id_user):
    try:
        user = model.Model.get_user_byid(id_user)
        if user[0] is None:
            return [None]
        else:
            return user
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

@main.route('/get_users', methods=['GET'])
def get_users():
    try:
        users = model.Model.get_users()
        if users is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return users
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

@main.route('/create_users', methods = ['POST'])
def create_users():
    try:
        data = request.json
        users = model.Model.create_users(data)
        if users is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return jsonify({
                'message': 'User inserted successfully!',
                'point': users
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

@main.route('/delete_user/<id_user>', methods=['DELETE'])
def delete_user(id_user):
    try:
        user = model.Model.delete_user(id_user)
        if user[0] is None:
            return jsonify({'message': 'User deleted failed, User not found!'}), 404
        else:
            return jsonify({'message': 'User deleted successfully!'})
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_user/<id_usuario>', methods=['PUT'])
def update_user(id_usuario):
    try:
        data = request.json
        usuario = model.Model.update_user(id_usuario, data)
        if usuario[0] is None:
            return jsonify({'message': 'User updated failed, User not found!'}), 404
        else:
            return usuario
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

# Person

@main.route('/get_personas', methods=['GET'])
def get_personas():
    try:
        personas = model.Model.get_personas()
        if personas is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return personas
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_persona_byid/<id_persona>', methods=['GET'])
def get_persona_byid(id_persona):
    try:
        persona = model.Model.get_persona_byid(id_persona)
        if persona[0] is None:
            return [None]
        else:
            return persona
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_persona', methods=['POST'])
def create_persona():
    try:
        data = request.json
        persona = model.Model.create_persona(data)
        if persona is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return jsonify({
                'message': 'Person inserted successfully!',
                'persona': persona
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_persona/<id_persona>', methods=['PUT'])
def update_persona(id_persona):
    try:
        data = request.json
        persona = model.Model.update_persona(id_persona, data)
        if persona is None:
            return jsonify({'message': 'Person updated failed, Person not found!'}), 404
        else:
            return jsonify({
                'message': 'Person updated successfully!',
                'persona': persona
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_persona/<id_persona>', methods=['DELETE'])
def delete_persona(id_persona):
    try:
        row_affect = model.Model.delete_persona(id_persona)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


# Rol Usuario
@main.route('/get_rolusuarios', methods=['GET'])
def get_rolusuarios():
    try:
        rolusuarios = model.Model.get_rolusuarios()
        if rolusuarios is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return rolusuarios
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_rolusuario_byid/<id_rolusuario>', methods=['GET'])
def get_rolusuario_byid(id_rolusuario):
    try:
        rolusuario = model.Model.get_rolusuario_byid(id_rolusuario)
        if rolusuario[0] is None:
            return [None]
        else:
            return rolusuario
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_rolusuario', methods=['POST'])
def create_rolusuario():
    try:
        data = request.json
        rolusuario = model.Model.create_rolusuario(data)
        if rolusuario is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return rolusuario[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_rolusuario/<id_rolusuario>', methods=['PUT'])
def update_rolusuario(id_rolusuario):
    try:
        data = request.json
        rolusuario = model.Model.update_rolusuario(id_rolusuario, data)
        if rolusuario is None:
            return jsonify({'message': 'User rol updated failed, Point not found!'}), 404
        else:
            return jsonify({
                'message': 'User rol updated successfully!',
                'rol_usuario': rolusuario[0]
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_rolusuario/<id_rolusuario>', methods=['DELETE'])
def delete_rolusuario(id_rolusuario):
    try:
        row_affect = model.Model.delete_rolusuario(id_rolusuario)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


# Usuarios
@main.route('/get_usuarios', methods=['GET'])
def get_usuarios():
    try:
        usuarios = model.Model.get_usuarios()
        if usuarios is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return usuarios
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_usuario_byid/<id_usuario>', methods=['GET'])
def get_usuario_byid(id_usuario):
    try:
        usuario = model.Model.get_usuario_byid(id_usuario)
        if usuario[0] is None:
            return [None]
        else:
            return usuario
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_usuario', methods=['POST'])
def create_usuario():
    try:
        data = request.json
        usuario = model.Model.create_usuario(data)
        if usuario is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return usuario[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_usuario/<id_usuario>', methods=['PUT'])
def update_usuario(id_usuario):
    try:
        data = request.json
        usuario = model.Model.update_usuario(id_usuario, data)
        if usuario is None:
            return jsonify({'message': 'User updated failed, User not found!'}), 404
        else:
            return usuario[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_usuario/<id_usuario>', methods=['DELETE'])
def delete_usuario(id_usuario):
    try:
        row_affect = model.Model.delete_usuario(id_usuario)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/assign_roluser/<id_user>', methods=['POST'])
def assign_roluser(id_user):
    try:
        data = request.json
        user = model.Model.assign_roluser(id_user, data)
        if user:
            return user[0]
        else:
            return jsonify({'message': 'User rol assign failed! The role has already been assigned before!'}), 404
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

@main.route('/login/<id_user>/<password>', methods=['GET'])
def login(id_user, password):
    try:
        user = model.Model.login(id_user, password)
        if user == 1:
            return jsonify({'message': 'User inactive!'}),404
        elif user == -1:
            return jsonify({'message': 'Login failed! Please enter a valid username or password'}), 404
        elif user is None:
            return jsonify({'message': 'Login failed! Please enter a valid username or password'}), 404
        else:
            return user[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_detalle_reservaciones', methods=['GET'])
def get_detalle_reservaciones():
    try:
        a = model.Model.get_detalle_reservaciones()
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_detalle_reservaciones_byid/<id_areservacion>', methods=['GET'])
def get_detalle_reservaciones_byid(id_areservacion):
    try:
        ac_id = model.Model.get_detalle_reservaciones_byid(id_areservacion)
        if ac_id[0] is None:
            return [None]
        else:
            return ac_id
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_detalle_reservaciones', methods=['POST'])
def create_detalle_reservaciones():
    try:
        data = request.json
        a = model.Model.create_detalle_reservacion(data)
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return jsonify({
                'message': 'Detalle Reservacion inserted successfully!',
                'alicuota': a[0]
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_detalle_reservaciones/<id>', methods=['PUT'])
def update_detalle_reservaciones(id):
    try:
        data = request.json
        a = model.Model.update_detalle_reservacion(id, data)
        if a is None:
            return jsonify({'message': 'Detalle Reservacion updated failed, Detalle Reservacion not found!'}), 404
        else:
            return jsonify({
                'message': 'Detalle Reservacion updated successfully!',
                'detalla_pago': a
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_detalle_reservacion/<id>', methods=['DELETE'])
def delete_detalle_reservacion(id):
    try:
        row_affect = model.Model.delete_detalle_reservacion(id)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500




# **************************************************************************************************

# Alicuotas

@main.route('/get_alicuotas', methods=['GET'])
def get_alicuotas():
    try:
        a  = model.Model.get_alicuotas()
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_alicuota_byid/<id>', methods=['GET'])
def get_alicuota_byid(id):
    try:
        a = model.Model.get_alicuota_byid(id)
        if a[0] is None:
            return [None]
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_alicuota', methods=['POST'])
def create_alicuota():
    try:
        data = request.json
        a = model.Model.create_alicuota(data)
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return jsonify({
                'message': 'Alicuota inserted successfully!',
                'alicuota': a[0]
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_alicuota/<id>', methods=['PUT'])
def update_alicuota(id):
    try:
        data = request.json
        a = model.Model.update_alicuota(id, data)
        if a is None:
            return jsonify({'message': 'Alicuota updated failed, Alicuota not found!'}), 404
        else:
            return jsonify({
                'message': 'Alicuota updated successfully!',
                'alicuota': a
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_alicuota/<id>', methods=['DELETE'])
def delete_alicuota(id):
    try:
        row_affect = model.Model.delete_alicuota(id)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


# **************************************************************************************************

# Pago Alicuotas

@main.route('/get_pago_alicuotas', methods=['GET'])
def get_pago_alicuotas():
    try:
        a  = model.Model.get_pago_alicuotas()
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_pago_alicuota_byid/<id>', methods=['GET'])
def get_pago_alicuota_byid(id):
    try:
        a = model.Model.get_pago_alicuota_byid(id)
        if a[0] is None:
            return [None]
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_pago_alicuota', methods=['POST'])
def create_pago_alicuota():
    try:
        data = request.json
        a = model.Model.create_pago_alicuota(data)
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return jsonify({
                'message': 'Pago Alicuota inserted successfully!',
                'alicuota': a[0]
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_pago_alicuota/<id>', methods=['PUT'])
def update_pago_alicuota(id):
    try:
        data = request.json
        a = model.Model.update_pago_alicuota(id, data)
        if a is None:
            return jsonify({'message': 'Pago Alicuota updated failed, Alicuota not found!'}), 404
        else:
            return jsonify({
                'message': 'Pago Alicuota updated successfully!',
                'alicuota': a
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_pago_alicuota/<id>', methods=['DELETE'])
def delete_pago_alicuota(id):
    try:
        row_affect = model.Model.delete_pago_alicuota(id)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



# **************************************************************************************************

# Detalle Pago

@main.route('/get_detalle_pagos', methods=['GET'])
def get_detalle_pagos():
    try:
        a  = model.Model.get_detalle_pagos()
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_detalle_pago_byid/<id>', methods=['GET'])
def get_detalle_pago_byid(id):
    try:
        a = model.Model.get_detalle_pago_byid(id)
        if a[0] is None:
            return [None]
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_detalle_pago', methods=['POST'])
def create_detalle_pago():
    try:
        data = request.json
        a = model.Model.create_detalle_pago(data)
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return jsonify({
                'message': 'Detalle Pago inserted successfully!',
                'alicuota': a[0]
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_detalle_pago/<id>', methods=['PUT'])
def update_detalle_pago(id):
    try:
        data = request.json
        a = model.Model.update_detalle_pago(id, data)
        if a is None:
            return jsonify({'message': 'Detalle Pago updated failed, Alicuota not found!'}), 404
        else:
            return jsonify({
                'message': 'Detalle Pago updated successfully!',
                'detalla_pago': a
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_detalle_pago/<id>', methods=['DELETE'])
def delete_detalle_pago(id):
    try:
        row_affect = model.Model.delete_detalle_pago(id)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



# **************************************************************************************************

# Egresos

@main.route('/get_egresos', methods=['GET'])
def get_egresos():
    try:
        a  = model.Model.get_egresos()
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_egreso_byid/<id>', methods=['GET'])
def get_egreso_byid(id):
    try:
        a = model.Model.get_egreso_byid(id)
        if a[0] is None:
            return [None]
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_egreso', methods=['POST'])
def create_egreso():
    try:
        data = request.json
        a = model.Model.create_egreso(data)
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return jsonify({
                'message': 'Egreso inserted successfully!',
                'egreso': a[0]
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_egreso/<id>', methods=['PUT'])
def update_egreso(id):
    try:
        data = request.json
        a = model.Model.update_egreso(id, data)
        if a is None:
            return jsonify({'message': 'Egreso updated failed, Egreso not found!'}), 404
        else:
            return jsonify({
                'message': 'Egreso updated successfully!',
                'egreso': a
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_egreso/<id>', methods=['DELETE'])
def delete_egreso(id):
    try:
        row_affect = model.Model.delete_egreso(id)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500




# **************************************************************************************************

# Egresos

@main.route('/get_detalle_egresos', methods=['GET'])
def get_detalle_egresos():
    try:
        a  = model.Model.get_detalle_egresos()
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_detalle_egreso_byid/<id>', methods=['GET'])
def get_detalle_egreso_byid(id):
    try:
        a = model.Model.get_detalle_egreso_byid(id)
        if a[0] is None:
            return [None]
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_detalle_egreso', methods=['POST'])
def create_detalle_egreso():
    try:
        data = request.json
        a = model.Model.create_detalle_egreso(data)
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return jsonify({
                'message': 'Egreso inserted successfully!',
                'egreso': a[0]
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_detalle_egreso/<id>', methods=['PUT'])
def update_detalle_egreso(id):
    try:
        data = request.json
        a = model.Model.update_detalle_egreso(id, data)
        if a is None:
            return jsonify({'message': 'Detalle Egreso updated failed, Egreso not found!'}), 404
        else:
            return jsonify({
                'message': 'Detalle Egreso updated successfully!',
                'egreso': a
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_detalle_egreso/<id>', methods=['DELETE'])
def delete_detalle_egreso(id):
    try:
        row_affect = model.Model.delete_detalle_egreso(id)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


# **************************************************************************************************

# Cabecera Reservaciones

@main.route('/get_cabreservaciones', methods=['GET'])
def get_cabreservaciones():
    try:
        a  = model.Model.get_cabecera_reservaciones()
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_cabreservacion_byid/<id>', methods=['GET'])
def get_cabreservacion_byid(id):
    try:
        a = model.Model.get_cabecera_reservacion_byid(id)
        if a[0] is None:
            return [None]
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

"""
@main.route('/create_cabreservacion', methods=['POST'])
def create_cabreservacion():
    try:
        data = request.json
        a = model.Model.create_cabecera_reservacion(data)
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return jsonify({
                'message': 'Cabecera reservacion inserted successfully!',
                'cabecera_reservacion': a[0]
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500
"""

@main.route('/update_cabreservacion/<id>', methods=['PUT'])
def update_cabreservacion(id):
    try:
        data = request.json
        a = model.Model.update_cabecera_reservacion(id, data)
        if a is None:
            return jsonify({'message': 'Cabecera reservacion updated failed, Cebecera reservacion not found!'}), 404
        else:
            return jsonify({
                'message': 'Cabecera reservacion updated successfully!',
                'cabecera_reservacion': a
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_cabreservacion/<id>', methods=['DELETE'])
def delete_cabreservacion(id):
    try:
        row_affect = model.Model.delete_cabecera_reservacion(id)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

# **************************************************************************************************


list_reservaciones = []
@main.route('/add_detalle_reservaciones', methods = ['GET'])
def add_detalle_reservaciones():
    try:
        data = request.json
        lista = model.Model.add_detail_reserv(data, list_reservaciones)
        if lista:
            return lista
        else:
            return [None]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

list_pagos = []
@main.route('/add_detalle_pagos', methods = ['GET'])
def add_detalle_pagos():
    try:
        data = request.json
        lista = model.Model.add_detail_pago(data, list_pagos)
        if lista:
            return lista
        else:
            return [None]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

list_egresos = []
@main.route('/add_detalle_egresos', methods = ['GET'])
def add_detalle_egresos():
    try:
        data = request.json
        lista = model.Model.add_detail_egreso(data, list_egresos)
        if lista:
            return lista
        else:
            return [None]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

def get_values():
    subtotal = 0
    iva = 0
    total = 0
    if list_reservaciones:
        for d in list_reservaciones:
            subtotal+=d['detres_subtotal']
            iva+=d['detres_iva']
            total+=d['detres_total']
    return subtotal, iva, total

def get_valuesPagos():
    subtotal = 0
    iva = 0
    total = 0
    if list_pagos:
        for d in list_pagos:
            subtotal+=d['detpag_subtotal']
            iva+=d['detpag_iva']
            total+=d['detpag_total']
    return subtotal, iva, total

def get_valuesEgresos():
    subtotal = 0
    iva = 0
    total = 0
    if list_egresos:
        for d in list_egresos:
            subtotal+=d['detegre_subtotal']
            iva+=d['detegre_iva']
            total+=d['detegre_total']
    return subtotal, iva, total

@main.route('/generar_reservacion', methods = ['POST'])
def generar_reservacion():
    try:
        data = request.json
        subtotal, iva, total = get_values()
        cabres = model.Model.create_cabecera_reservacion(subtotal, iva, total, data)[0]
        if list_reservaciones:
            for d in list_reservaciones:
                d['detres_cabreservacion'] = cabres['id_cabreservacion']
                model.Model.create_detalle_reservacion(d)
        list_reservaciones.clear()
        return cabres
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/generar_pago_alicuota', methods = ['POST'])
def generar_pago_alicuota():
    try:
        data = request.json
        subtotal, iva, total = get_valuesPagos()
        d = model.Model.create_pago_alicuota(subtotal, iva, total, data)[0]
        if list_pagos:
            for da in list_pagos:
                da['pagali_id'] = d.get('pagali_id')
                model.Model.create_detalle_pago(da)
        return d
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

@main.route('/generar_egreso', methods = ['POST'])
def generar_egreso():
    try:
        data = request.json
        subtotal, iva, total = get_valuesEgresos()
        d = model.Model.create_egreso(subtotal, iva, total, data)[0]
        if list_egresos:
            for da in list_egresos:
                da['egre_id'] = d['egre_id']
                model.Model.create_detalle_egreso(da)
        return d
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


# **************************************************************************************************

@main.route('/get_multas', methods=['GET'])
def get_multas():
    try:
        multas = model.Model.get_multas()
        if multas is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return multas
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


##-----get id 

@main.route('/get_multas_byid/<id_multa>', methods=['GET'])
def get_multas_byid(id_multa):
    try:
        multa_id = model.Model.get_multas_byid(id_multa)
        if multa_id[0] is None:
            return [None]
        else:
            return multa_id
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

##----create
@main.route('/create_multas', methods=['POST'])
def create_multas():
    try:
        data = request.json
        multas = model.Model.create_multas(data)
        if multas[0] is None:
            return [None]
        else:
            return multas
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

##-----update

@main.route('/update_multas/<id_multas>', methods=['PUT'])
def update_multas(id_multas):
    try:
        data = request.json
        multas = model.Model.update_multas(id_multas, data)
        if multas is None:
            return jsonify({'message': 'Fines updated failed, Fines not found!'}), 404
        else:
            return multas[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


##-------Delete
@main.route('/delete_multas/<id_multas>', methods=['DELETE'])
def delete_multas(id_multas):
    try:
        row_affect = model.Model.delete_multas(id_multas)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



##---------------tipo documentos---------
@main.route('/get_tipoDocumentos', methods=['GET'])
def get_tipoDocumentos():
    try:
        tipodoc = model.Model.get_tipoDocumentos()
        if tipodoc is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return tipodoc
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_tipoDocumentos_byid/<id_documento>', methods=['GET'])
def get_tipoDocumentos_byid(id_documento):
    try:
        tipoDocumentos_id = model.Model.get_tipoDocumentos_byid(id_documento)
        if tipoDocumentos_id[0] is None:
            return [None]
        else:
            return tipoDocumentos_id
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_tipoDocumentos', methods=['POST'])
def create_tipoDocumentos():
    try:
        data = request.json
        tipoDocumentos = model.Model.create_tipoDocumentos(data)
        if tipoDocumentos is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return tipoDocumentos
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



@main.route('/update_tipoDocumentos/<id_tido>', methods=['PUT'])
def update_tipoDocumentos(id_tido):
    try:
        data = request.json
        tido = model.Model.update_tipoDocumentos(id_tido, data)
        if tido is None:
            return jsonify({'message': 'Tipo de documento updated failed, Tipo de documento not found!'}), 404
        else:
            return tido
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



@main.route('/delete_tipoDocumentos/<id_tido>', methods=['DELETE'])
def delete_tipoDocumentos(id_tido):
    try:
        row_affect = model.Model.delete_tipoDocumentos(id_tido)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



##------------tipo de servicio-------------
    ##---get 
@main.route('/get_tipo_servicios', methods=['GET'])
def get_tipo_servicios():
    try:
        tise = model.Model.get_tipo_servicios()
        if tise[0] is None:
            return [None]
        else:
            return tise
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

    
    ##---get id 

@main.route('/get_tipo_servicios_byid/<id_servicio>', methods=['GET'])
def get_tipo_servicios_byid(id_servicio):
    try:
        tipoServicio_id = model.Model.get_tipo_servicios_byid(id_servicio)
        if tipoServicio_id[0] is None:
            return [None]
        else:
            return tipoServicio_id
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

   ##---crear tipo de servicio
@main.route('/create_tipo_servicios', methods=['POST'])
def create_tipo_servicios():
    try:
        data = request.json
        tipoServicio = model.Model.create_tipo_servicios(data)
        if tipoServicio is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return tipoServicio
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

##-----actualizar tipo servicio
@main.route('/update_tipo_servicio/<id_tise>', methods=['PUT'])
def update_tipo_servicio(id_tise):
        try:
            data = request.json
            tise = model.Model.update_tipo_servicio(id_tise, data)
            if tise is None:
                return jsonify({'message': 'Tipo de servicio updated failed, Tipo de servicio not found!'}), 404
            else:
                return tise
        except Exception as ex:
            return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_tipo_servicio/<id_rotise>', methods=['DELETE'])
def delete_tipo_servicio(id_rotise):
    try:
        row_affect = model.Model.delete_tipo_servicio(id_rotise)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


##-------------------SERVICIOS-----------------

#--get

@main.route('/get_servicios', methods=['GET'])
def get_servicios():
    try:
        servicio = model.Model.get_servicios()
        if servicio is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return servicio
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


##-------get id 


@main.route('/get_servicio_byid/<id_servicio>', methods=['GET'])
def get_servicio_byid(id_servicio):
    try:
        Servicios_id = model.Model.get_servicio_byid(id_servicio)
        if Servicios_id[0] is None:
            return [None]
        else:
            return Servicios_id
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

   ##---crear  servicios
@main.route('/create_servicios', methods=['POST'])
def create_servicios():
    try:
        data = request.json
        Servicios = model.Model.create_servicios(data)
        if Servicios is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return Servicios
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


##update servicios

@main.route('/update_servicios/<id_servicios>', methods=['PUT'])
def update_servicios(id_servicios):
    try:
        data = request.json
        servicios = model.Model.update_servicios(id_servicios, data)
        if servicios is None:
            return jsonify({'message': 'Service updated failed, Point not found!'}), 404
        else:
            return jsonify({
                'message': 'Service updated successfully!',
                'point': servicios[0]
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

##-----------delete servicios

@main.route('/delete_servicios/<id_servicios>', methods=['DELETE'])
def delete_servicios(id_servicios):
    try:
        row_affect = model.Model.delete_servicios(id_servicios)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


###-----------------------RESERVACIONES---------------
#---get reseraciones

@main.route('/get_reservaciones', methods=['GET'])
def get_reservaciones():
    try:
        reservaciones = model.Model.get_reservaciones()
        if reservaciones is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return reservaciones
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

#-----get id reservaciones

@main.route('/get_reservaciones_byid/<id_reservaciones>', methods=['GET'])
def get_reservaciones_byid(id_reservaciones):
    try:
        reservaciones_id = model.Model.get_reservaciones_byid(id_reservaciones)
        if reservaciones_id is None:
            return jsonify({'message': 'Reservations not found!'}), 404
        else:
            return reservaciones_id
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


   ##---crear reservaciones
@main.route('/create_reservaciones', methods=['POST'])
def create_reservaciones():
    try:
        data = request.json
        reservaciones = model.Model.create_reservaciones(data)
        if reservaciones is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return reservaciones[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

##update reservaciones

@main.route('/update_reservaciones/<id_reservaciones>', methods=['PUT'])
def update_reservaciones(id_reservaciones):
    try:
        data = request.json
        reservaciones = model.Model.update_reservaciones(id_reservaciones, data)
        if reservaciones is None:
            return jsonify({'message': 'Bookings updated failed, Bookings not found!'}), 404
        else:
            return jsonify({
                'message': 'Bookings updated successfully!',
                'reservacion': reservaciones[0]
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


##delete_reservaciones
@main.route('/delete_reservaciones/<id_reservaciones>', methods=['DELETE'])
def delete_reservaciones(id_reservaciones):
    try:
        row_affect = model.Model.delete_reservaciones(id_reservaciones)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


##---------------------------ALICUOTA ACTUALIZADA----------------------
## get 
@main.route('/get_alicuotaActualizadas', methods=['GET'])
def get_alicuotaActualizadas():
    try:
        a = model.Model.get_alicuotaActualizadas()
        if a is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return a
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

## get id
@main.route('/get_alicuotaActualizada_byid/<id_alicuotaac>', methods=['GET'])
def get_alicuotaActualizada_byid(id_alicuotaac):
    try:
        ac_id = model.Model.get_alicuotaActualizada_byid(id_alicuotaac)
        if ac_id is None:
            return jsonify({'message': 'updated aliquot not found!'}), 404
        else:
            return ac_id
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

## create alicuota_actualizada
@main.route('/create_alicuotaActualizada', methods=['POST'])
def create_alicuotaActualizada():
    try:
        data = request.json
        ac = model.Model.create_alicuotaActualizada(data)
        if ac is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return ac
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


##update alicuota actualizada
@main.route('/update_alicuotaActualizada/<id_alicuotaac>', methods=['PUT'])
def update_alicuotaActualizada(id_alicuotaac):
    try:
        data = request.json
        ac = model.Model.update_alicuotaActualizada(id_alicuotaac, data)
        if ac is None:
            return jsonify({'message': 'Aliquot updated failed, Aliquot not found!'}), 404
        else:
            return jsonify({
                'message': 'Aliquot updated successfully!',
                'point': ac
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



    ##---delete alicuotaac

@main.route('/delete_alicuotaActualizada/<id_ac>', methods=['DELETE'])
def delete_alicuotaActualizada(id_ac):
    try:
        row_affect = model.Model.delete_alicuotaActualizada(id_ac)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

# **************************************************************************************************


@main.route('/get_documentos', methods=['GET'])
def get_documentos():
    try:
        tps = model.Model.get_documentos()
        if tps is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return tps
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_documento_byid/<doc_iddocumento>', methods=['GET'])
def get_documento_byid(doc_iddocumento):
    try:
        d = model.Model.get_documento_byid(doc_iddocumento)
        if d[0] is None:
            return [None]
        else:
            return d
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



@main.route('/create_documentos', methods=['POST'])
def create_documentos():
    try:
        data = request.json
        c_d = model.Model.create_documentos(data)
        if c_d is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return c_d[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_documento/<doc_iddocumento>', methods=['PUT'])
def update_documento(doc_iddocumento):
    try:
        data = request.json
        td = model.Model.update_documento(doc_iddocumento, data)
        if td is None:
            return jsonify({'message': 'Type Document updated failed, Point not found!'}), 404
        else:
            return jsonify({
                'message': 'Type Document updated successfully!',
                'documento': td
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_documento/<doc_iddocumento>', methods=['DELETE'])
def delete_documento(doc_iddocumento):
    try:
        row_affect = model.Model.delete_documento(doc_iddocumento)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



##estado_documento
@main.route('/get_estado_documentoTODO', methods=['GET'])
def get_estado_documentoTODO():
    try:
        tps = model.Model.get_estado_documentoTODO()
        if tps is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return tps
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 
    
    
@main.route('/get_estado_documentoTRUE', methods=['GET'])
def get_estado_documentoTRUE():
    try:
        tps = model.Model.get_estado_documentoTRUE()
        if tps is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return tps
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

@main.route('/get_estado_documentoFALSE', methods=['GET'])
def get_estado_documentoFALSE():
    try:
        tps = model.Model.get_estado_documentoFALSE()
        if tps is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return tps
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



@main.route('/create_estado_documento', methods=['POST'])
def create_estado_documento():
    try:
        data = request.json
        c_td = model.Model.create_estado_documento(data)
        if c_td is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return c_td[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

##reunion
@main.route('/get_reuniones', methods=['GET'])
def get_reuniones():
    try:
        tps = model.Model.get_reunion()
        if tps is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return tps
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 
    
@main.route('/get_reunion_byid/<reun_idreunion>', methods=['GET'])
def get_reunion_byid(reun_idreunion):
    try:
        d = model.Model.get_reunion_byid(reun_idreunion)
        if d is None:
            return jsonify({'message': 'Documento not found!'}), 404
        else:
            return d
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



    
@main.route('/create_reunion', methods=['POST'])
def create_reunion():
    try:
        data = request.json
        c_td = model.Model.create_reunion(data)
        if c_td is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return c_td[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



@main.route('/update_reunion/<id_reunion>', methods=['PUT'])
def update_reunion(id_reunion):
    try:
        data = request.json
        td = model.Model.update_reunion(id_reunion, data)
        if td is None:
            return jsonify({'message': 'Type Document updated failed, Point not found!'}), 404
        else:
            return jsonify({
                'message': 'Type Document updated successfully!',
                'point': td.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_reunion/<id_reunion>', methods=['DELETE'])
def delete_reunion(id_reunion):
    try:
        row_affect = model.Model.delete_reunion(id_reunion)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


# **************************************************************************************************
import pathlib
UPLOAD_FOLDER = 'docs/'
main.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
main.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/upload', methods=['POST'])
def upload():
    mongo = conn.get_connectionMongoDB().db
    file = request.files['inputFile']
    doc_descripcion = request.form['doc_descripcion']
    doc_documento = file.filename
    doc_entidad = request.form['doc_entidad']
    doc_recibido = request.form['doc_recibido']
    estado_delete = request.form['estado_delete']
    sec_idsecretario = request.form['sec_idsecretario']
    tipdoc_id = request.form['tipdoc_id']
    data = 	{
		"doc_descripcion": doc_descripcion,
		"doc_documento": file.filename,
		"doc_entidad": doc_entidad,
		"doc_recibido": doc_recibido,
		"estado_delete": estado_delete,
		"sec_idsecretario": sec_idsecretario,
		"tipdoc_id": tipdoc_id
	}
    doc = model.Model.create_documentos(data)[0]
    id_doc = doc.get('doc_iddocumento')
    filename = secure_filename(file.filename)
    if file and allowed_file(file.filename):
        file.save(os.path.join(main.config['UPLOAD_FOLDER'], filename))
        file_loc = os.path.join(main.config['UPLOAD_FOLDER'], filename)
        docs = mongo['test.files']
        fs = gridfs.GridFS(mongo, collection="test")
        upload_file(file_loc=file_loc, file_name=file.filename, fs=fs, doc_descripcion = doc_descripcion,
                                        doc_documento = file.filename,
                                        doc_entidad = doc_entidad,
                                        doc_recibido = doc_recibido,
                                        estado_delete = estado_delete,
                                        sec_idsecretario = sec_idsecretario,
                                        tipdoc_id = tipdoc_id,
                                        doc_iddocumento = id_doc)
        flash('File successfully uploaded ' + file.filename + ' to the database!')
        return redirect('/')
    else:
        flash('Invalid Uplaod only txt, pdf, png, jpg, jpeg, gif') 
    return redirect('/')

def upload_file(file_loc, file_name, fs, doc_descripcion,
                                        doc_documento,
                                        doc_entidad,
                                        doc_recibido,
                                        estado_delete,
                                        sec_idsecretario,
                                        tipdoc_id, doc_iddocumento):
    """upload file to mongodb"""
    print(file_loc)
    with open(file_loc, 'rb') as file_data:
        data = file_data.read()
    # put file into mongodb
    fs.put(data, filename=file_name, doc_descripcion = doc_descripcion,
                                        doc_documento = doc_documento,
                                        doc_entidad = doc_entidad,
                                        doc_recibido = doc_recibido,
                                        estado_delete = estado_delete,
                                        sec_idsecretario = sec_idsecretario,
                                        tipdoc_id = tipdoc_id,
                                        doc_iddocumento = doc_iddocumento)
    print("Upload Complete")


def download_file(download_loc, db, fs, id_doc):
    """download file from mongodb"""
    data = db.test.files.find_one({"doc_iddocumento": id_doc})
    print(data)
    
    fs_id = data['_id']
    out_data = fs.get(fs_id).read()

    with open(download_loc, 'wb') as output:
        output.write(out_data)
    
    print("Download Completed!")

# **************************************************************************************************

def Page_Not_Found(error):
    return '<h1>Page Not Found</h1>', 404


@main.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    main.register_error_handler(404, Page_Not_Found)
    main.run(debug = True, host = "0.0.0.0")

