"""# -*- coding: utf-8 -*-

Created on Tue Oct 11 22:55:25 2022

@author: Mario
"""

from flask import jsonify, request
from flask import Flask, jsonify, request
from config import config
from models import Models as model

main = Flask(__name__)

@main.route('/get_user_byid/<id_user>', methods=['GET'])
def get_user_byid(id_user):
    try:
        user = model.Model.get_user_byid(id_user)
        if user[0] is None:
            return jsonify({'message': 'User not found!'}), 404
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


@main.route('/get_personas_byid/<id_persona>', methods=['GET'])
def get_persona_byid(id_persona):
    try:
        persona = model.Model.get_persona_byid(id_persona)
        print(persona)
        if persona is None:
            return jsonify({'message': 'Person not found!'}), 404
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
                'point': persona
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_persona/<id_persona>', methods=['PUT'])
def update_persona(id_persona):
    try:
        data = request.json
        persona = model.Model.update_persona(id_persona, data)
        if persona is None:
            return jsonify({'message': 'Person updated failed, Point not found!'}), 404
        else:
            return jsonify({
                'message': 'Person updated successfully!',
                'point': persona.convert_to_json()
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
        print(rolusuario)
        if rolusuario is None:
            return jsonify({'message': 'Usr rol not found!'}), 404
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
                'point': rolusuario[0]
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
        if usuario is None:
            return jsonify({'message': 'User not found!'}), 404
        else:
            return usuario
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_usuario', methods=['POST'])
def create_usuario():
    try:
        data = request.json
        usuario = model.Model.create_usuario(data)
        print(usuario)
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
        print(user,'Hello')
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
######################## Tesorero
@main.route('/get_tipo_documento', methods=['GET'])
def get_tipo_documento():
    try:
        tps = model.Model.get_tipo_documento()
        if tps is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return tps
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_tipodocumento_byid/<tipdoc_id>', methods=['GET'])
def get_tipodocumento_byid(tipdoc_id):
    try:
        td = model.Model.get_tipodocumento_byid(tipdoc_id)
        print(td)
        if td is None:
            return jsonify({'message': 'Person not found!'}), 404
        else:
            return td
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



@main.route('/create_tipodocumento', methods=['POST'])
def create_tipodocumento():
    try:
        data = request.json
        c_td = model.Model.create_tipodocumento(data)
        print(c_td)
        if c_td is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return c_td[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_tipodocumento/<id_tipdoc>', methods=['PUT'])
def update_tipodocumento(id_tipdoc):
    try:
        data = request.json
        td = model.Model.update_tipodocumento(id_tipdoc, data)
        if td is None:
            return jsonify({'message': 'Type Document updated failed, Point not found!'}), 404
        else:
            return jsonify({
                'message': 'Type Document updated successfully!',
                'point': td.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_tipodocumento/<id_tipdoc>', methods=['DELETE'])
def delete_tipodocumento(id_tipdoc):
    try:
        row_affect = model.Model.delete_tipodocumento(id_tipdoc)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500




@main.route('/get_documento', methods=['GET'])
def get_documento():
    try:
        tps = model.Model.get_documento()
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
        print(d)
        if d is None:
            return jsonify({'message': 'Documento not found!'}), 404
        else:
            return d
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500



@main.route('/create_documentos', methods=['POST'])
def create_documentos():
    try:
        data = request.json
        c_d = model.Model.create_documentos(data)
        print(c_d)
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
                'point': td.convert_to_json()
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
        print(c_td)
        if c_td is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return c_td[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

##reunion
@main.route('/get_reunion', methods=['GET'])
def get_reunion():
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
        print(d)
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
        print(c_td)
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

##-------------Multas-------------

##---get
@main.route('/get_multas', methods=['GET'])
def get_multas():
    try:
        multas = model.Model.get_multas()
        if multas is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return multas[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


##-----get id 

@main.route('/get_multas_byid/<id_multa>', methods=['GET'])
def get_multas_byid(id_multa):
    try:
        multa_id = model.Model.get_multas_byid(id_multa)
        if multa_id is None:
            return jsonify({'message': 'Person not found!'}), 404
        else:
            return multa_id[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

##----create
@main.route('/create_multas', methods=['POST'])
def create_multas():
    try:
        data = request.json
        multas = model.Model.create_multas(data)
        if multas is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return multas[0]
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
            return tipodoc[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_tipoDocumentos_byid/<id_documento>', methods=['GET'])
def get_tipoDocumentos_byid(id_documento):
    try:
        tipoDocumentos_id = model.Model.get_tipoDocumentos_byid(id_documento)
        if tipoDocumentos_id is None:
            return jsonify({'message': 'Person not found!'}), 404
        else:
            return tipoDocumentos_id[0]
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
            return tipoDocumentos[0]
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
            return tido[0]
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
        if tise is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return tise[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500

    
    ##---get id 

@main.route('/get_tipo_servicios_byid/<id_servicio>', methods=['GET'])
def get_tipo_servicios_byid(id_servicio):
    try:
        tipoServicio_id = model.Model.get_tipo_servicios_byid(id_servicio)
        if tipoServicio_id is None:
            return jsonify({'message': 'Person not found!'}), 404
        else:
            return tipoServicio_id[0]
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
            return tipoServicio[0]
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
                return tise[0]
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

@main.route('/get_servicio', methods=['GET'])
def get_servicio():
    try:
        servicio = model.Model.get_servicio()
        if servicio is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return servicio[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


##-------get id 


@main.route('/get_servicio_byid/<id_servicio>', methods=['GET'])
def get_servicio_byid(id_servicio):
    try:
        Servicios_id = model.Model.get_servicio_byid(id_servicio)
        if Servicios_id is None:
            return jsonify({'message': 'Service not found!'}), 404
        else:
            return Servicios_id[0]
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
            return Servicios[0]
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
        reseraciones = model.Model.get_reservaciones()
        if reseraciones is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return reseraciones[0]
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
            return reservaciones_id[0]
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
                'point': reservaciones[0]
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
@main.route('/get_alicuotaActualizada', methods=['GET'])
def get_alicuotaActualizada():
    try:
        reseraciones = model.Model.get_alicuotaActualizada()
        if reseraciones is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return reseraciones[0]
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
            return ac_id[0]
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
            return ac[0]
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
                'point': ac[0]
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


def Page_Not_Found(error):
    return '<h1>Page Not Found</h1>', 404


@main.route('/')
def index():
    return '<h1>Hi, I am Mario and Who are you?</h1>'


if __name__ == '__main__':
    main.config.from_object(config['development'])
    main.register_error_handler(404, Page_Not_Found)
    main.run()
