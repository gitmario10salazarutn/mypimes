# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:50:55 2022

@author: Mario
"""


from flask import Blueprint, jsonify, request
from models import Models as model

main = Blueprint('conicas_blueprint', __name__)


@main.route('/get')
def get():
    return "Hola"

# GET ALL


@main.route('/get_personas', methods=['GET'])
def get_personas():
    try:
        personas = model.Model.get_personas()
        if personas is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return personas[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_points', methods=['GET'])
def get_points():
    try:
        points = model.Model.get_points()
        if points is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return points[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_lines', methods=['GET'])
def get_lines():
    try:
        lines = model.Model.get_lines()
        if lines is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return lines[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_circunferences', methods=['GET'])
def get_circunferences():
    try:
        circunferences = model.Model.get_circunferences()
        if circunferences is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return circunferences[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elipses', methods=['GET'])
def get_elipses():
    try:
        elipses = model.Model.get_elipses()
        if elipses is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return elipses[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_hiperbolas', methods=['GET'])
def get_hiperbolas():
    try:
        hiperbolas = model.Model.get_hiperbolas()
        if hiperbolas is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return hiperbolas[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_parabolas', methods=['GET'])
def get_parabolas():
    try:
        parabolas = model.Model.get_parabolas()
        if parabolas is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return parabolas[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


# GET BY ID

@main.route('/get_point_byid/<id_punto>', methods=['GET'])
def get_point_byid(id_punto):
    try:
        point = model.Model.get_point_byid(id_punto)
        if point is None:
            return jsonify({'message': 'Point not found!'}), 404
        else:
            return point[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_line_byid/<id_recta>', methods=['GET'])
def get_line_byid(id_recta):
    try:
        line = model.Model.get_line_byid(id_recta)
        if line is None:
            return jsonify({'message': 'Line not found!'}), 404
        else:
            return line[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_circunference_byid/<id_circunference>', methods=['GET'])
def get_circunference_byid(id_circunference):
    try:
        circunference = model.Model.get_circunference_byid(id_circunference)
        if circunference is None:
            return jsonify({'message': 'Circunference not found!'}), 404
        else:
            return circunference[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elipse_byid/<id_elipse>', methods=['GET'])
def get_elipse_byid(id_elipse):
    try:
        elipse = model.Model.get_elipse_byid(id_elipse)
        if elipse is None:
            return jsonify({'message': 'Elipse not found!'}), 404
        else:
            return elipse[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_hiperbola_byid/<id_hiperbola>', methods=['GET'])
def get_hiperbola_byid(id_hiperbola):
    try:
        hiperbola = model.Model.get_hiperbola_byid(id_hiperbola)
        if hiperbola is None:
            return jsonify({'message': 'Hiperbola not found!'}), 404
        else:
            return hiperbola[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_parabola_byid/<id_parabola>', methods=['GET'])
def get_parabola_byid(id_parabola):
    try:
        parabola = model.Model.get_parabola_byid(id_parabola)
        if parabola is None:
            return jsonify({'message': 'Line not found!'}), 404
        else:
            return parabola[0]
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_point', methods=['POST'])
def create_point():
    try:
        data = request.json
        point = model.Model.create_point(data)
        if point is None:
            return jsonify({'message': 'Data not found!'}), 404
        else:
            return jsonify({
                'message': 'Point inserted successfully!',
                'point': point
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_line', methods=['POST'])
def create_line():
    try:
        data = request.json
        line = model.Model.create_line(data)
        if line is None:
            return jsonify({'message': 'Insert line failed!'}), 404
        else:
            return jsonify({
                'message': 'Line inserted successfully!',
                'line': line
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_circunference', methods=['POST'])
def create_circunference():
    try:
        data = request.json
        circunference = model.Model.create_circunference(data)
        if circunference is None:
            return jsonify({'message': 'Insert circunference failed!'}), 404
        else:
            return jsonify({
                'message': 'Circunference inserted successfully!',
                'circunference': circunference
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_parabola', methods=['POST'])
def create_parabola():
    try:
        data = request.json
        parabola = model.Model.create_parabola(data)
        if parabola is None:
            return jsonify({'message': 'Insert parabola failed!'}), 404
        else:
            return jsonify({
                'message': 'Parabola inserted successfully!',
                'parabola': parabola
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_elipse', methods=['POST'])
def create_elipse():
    try:
        data = request.json
        elipse = model.Model.create_elipse(data)
        if elipse is None:
            return jsonify({'message': 'Insert elipse failed!'}), 404
        else:
            return jsonify({
                'message': 'Elipse inserted successfully!',
                'elipse': elipse
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/create_hiperbola', methods=['POST'])
def create_hiperbola():
    try:
        data = request.json
        hiperbola = model.Model.create_hiperbola(data)
        if hiperbola is None:
            return jsonify({'message': 'Insert hiperbola failed!'}), 404
        else:
            return jsonify({
                'message': 'Hiperbola inserted successfully!',
                'hiperbola': hiperbola
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_point/<id_punto>', methods=['PUT'])
def update_point(id_punto):
    try:
        data = request.json
        point = model.Model.update_point(id_punto, data)
        if point is None:
            return jsonify({'message': 'Point updated failed, Point not found!'}), 404
        else:
            return jsonify({
                'message': 'Point updated successfully!',
                'point': point.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_line/<id_line>', methods=['PUT'])
def update_line(id_line):
    try:
        data = request.json
        line = model.Model.update_line(id_line, data)
        if line is None:
            return jsonify({'message': 'Update line failed, Line not found!'}), 404
        else:
            return jsonify({
                'message': 'Line updated successfully!',
                'line': line.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_circunference/<id_circunference>', methods=['PUT'])
def update_circunference(id_circunference):
    try:
        data = request.json
        circunference = model.Model.update_circunference(
            id_circunference, data)
        if circunference is None:
            return jsonify({'message': 'Update circunference failed, circunference not found!'}), 404
        else:
            return jsonify({
                'message': 'Circunference updated successfully!',
                'circunference': circunference.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_parabola/<id_parabola>', methods=['PUT'])
def update_parabola(id_parabola):
    try:
        data = request.json
        parabola = model.Model.update_parabola(id_parabola, data)
        if parabola is None:
            return jsonify({'message': 'Update parabola failed, parabola not found!'}), 404
        else:
            return jsonify({
                'message': 'Parabola updated successfully!',
                'parabola': parabola.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_elipse/<id_elipse>', methods=['PUT'])
def update_elipse(id_elipse):
    try:
        data = request.json
        elipse = model.Model.update_elipse(id_elipse, data)
        if elipse is None:
            return jsonify({'message': 'Update elipse failed, elipse not found!'}), 404
        else:
            return jsonify({
                'message': 'Elipse updated successfully!',
                'elipse': elipse.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/update_hiperbola/<id_hiperbola>', methods=['PUT'])
def update_hiperbola(id_hiperbola):
    try:
        data = request.json
        hiperbola = model.Model.update_hiperbola(id_hiperbola, data)
        if hiperbola is None:
            return jsonify({'message': 'Update hiperbola failed, hiperbola not found!'}), 404
        else:
            return jsonify({
                'message': 'Hiperbola updated successfully!',
                'hiperbola': hiperbola.convert_to_json()
            })
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_point/<id_punto>', methods=['DELETE'])
def delete_point(id_punto):
    try:
        row_affect = model.Model.delete_point(id_punto)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_line/<id_line>', methods=['DELETE'])
def delete_line(id_line):
    try:
        row_affect = model.Model.delete_line(id_line)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_circunference/<id_circunference>', methods=['DELETE'])
def delete_circunference(id_circunference):
    try:
        row_affect = model.Model.delete_circunference(id_circunference)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_parabola/<id_parabola>', methods=['DELETE'])
def delete_parabola(id_parabola):
    try:
        row_affect = model.Model.delete_parabola(id_parabola)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_elipse/<id_elipse>', methods=['DELETE'])
def delete_elipse(id_elipse):
    try:
        row_affect = model.Model.delete_elipse(id_elipse)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/delete_hiperbola/<id_hiperbola>', methods=['DELETE'])
def delete_hiperbola(id_hiperbola):
    try:
        row_affect = model.Model.delete_hiperbola(id_hiperbola)
        return jsonify(row_affect)
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elements_linebyid/<id_line>', methods=['GET'])
def get_elements_linebyid(id_line):
    try:
        line = model.Model.get_elements_line_byid(id_line)
        if line is None:
            return jsonify({'message': 'Line not found!'})
        else:
            return line.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elements_circunferencebyid/<id_circunference>', methods=['GET'])
def get_elements_circunferencebyid(id_circunference):
    try:
        circunference = model.Model.get_elements_circunference_byid(
            id_circunference)
        if circunference is None:
            return jsonify({'message': 'Circunference not found!'})
        else:
            return circunference.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elements_parabolabyid/<id_parabola>', methods=['GET'])
def get_elements_parabolabyid(id_parabola):
    try:
        parabola = model.Model.get_elements_parabola_byid(id_parabola)
        if parabola is None:
            return jsonify({'message': 'Parabola not found!'})
        else:
            return parabola.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elements_elipsebyid/<id_elipse>', methods=['GET'])
def get_elements_elipsebyid(id_elipse):
    try:
        elipse = model.Model.get_elements_elipse_byid(id_elipse)
        if elipse is None:
            return jsonify({'message': 'Elipse not found!'})
        else:
            return elipse.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elements_hiperbolabyid/<id_hiperbola>', methods=['GET'])
def get_elements_hiperbolabyid(id_hiperbola):
    try:
        hiperbola = model.Model.get_elements_hiperbola_byid(id_hiperbola)
        if hiperbola is None:
            return jsonify({'message': 'Hiperbola not found!'})
        else:
            return hiperbola.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elements_line', methods=['GET'])
def get_elements_line():
    try:
        data = request.json
        line = model.Model.get_elements_line(data)
        if line is None:
            return jsonify({'message': 'Data Line not found!'})
        else:
            return line.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elements_circunference', methods=['GET'])
def get_elements_circunference():
    try:
        data = request.json
        circunference = model.Model.get_elements_circunference(data)
        if circunference is None:
            return jsonify({'message': 'Data Circunference not found!'})
        else:
            return circunference.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elements_parabola', methods=['GET'])
def get_elements_parabola():
    try:
        data = request.json
        parabola = model.Model.get_elements_parabola(data)
        if parabola is None:
            return jsonify({'message': 'Data Parabola not found!'})
        else:
            return parabola.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elements_elipse', methods=['GET'])
def get_elements_elipse():
    try:
        data = request.json
        elipse = model.Model.get_elements_elipse(data)
        if elipse is None:
            return jsonify({'message': 'Data Elipse not found!'})
        else:
            return elipse.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500


@main.route('/get_elements_hiperbola', methods=['GET'])
def get_elements_hiperbola():
    try:
        data = request.json
        hiperbola = model.Model.get_elements_hiperbola(data)
        if hiperbola is None:
            return jsonify({'message': 'Data Hiperbola not found!'})
        else:
            return hiperbola.get_elements()
    except Exception as ex:
        return jsonify({'message': 'Error {0}'.format(ex)}), 500
