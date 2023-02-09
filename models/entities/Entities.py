# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:28:34 2022

@author: Mario
"""


from datetime import datetime
import math
from fractions import Fraction
import json

class Entities:
    @classmethod
    def rol_usuarioEntity(self, rol_usuario) -> dict:
        if rol_usuario:
            return {
                "rol_idrol": rol_usuario[0],
                "rol_nombrerol": rol_usuario[1],
                "prefijo": rol_usuario[2]
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
			"user_fecha": usuario[10],
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

    @classmethod
    def multaEntity(self, multa) -> dict:
        if multa:
            return {
                "mult_idmulta": multa[0],
                "mult_nombre": multa[1],
                "mult_valor": multa[2]
            }
        else:
            return None

    @classmethod
    def listMultas(self, multas) -> list:
        return [self.multaEntity(multa) for multa in multas]

    @classmethod
    def alicuotaEntity(self, alicuota) -> dict:
        if alicuota:
            return {
                "ali_idalicuota": alicuota[0],
                "multa": {
                    "mult_idmulta": alicuota[1],
                    "mult_nombre": alicuota[2],
                    "mult_valor": alicuota[3]
                },
                "ali_fecha_actualizacion": alicuota[4],
                "ali_valor_anterior": alicuota[5],
                "ali_valor_actual": alicuota[6]
            }
        else:
            return None

    @classmethod
    def listAlicotas(self, alicuotas) -> list:
        return [self.alicuotaEntity(alicuota) for alicuota in alicuotas]

    @classmethod
    def alicuota_actualizadaEntity(self, alicuota_actualizada) -> dict:
        if alicuota_actualizada:
            return {
                "alic_id": alicuota_actualizada[0],
                "alicuota": {
                    "ali_idalicuota": alicuota_actualizada[1],
                    "multa": {
                        "mult_idmulta": alicuota_actualizada[2],
                        "mult_nombre": alicuota_actualizada[3],
                        "mult_valor": alicuota_actualizada[4]
                },
                    "ali_fecha_actualizacion": alicuota_actualizada[5],
                    "ali_valor_anterior": alicuota_actualizada[6],
                    "ali_valor_actual": alicuota_actualizada[7]
                },
                "alic_valor": alicuota_actualizada[8],
                "alic_fecha": alicuota_actualizada[9]
            }
        else:
            return None

    @classmethod
    def tesoreroEntity(self, tesorero) -> dict:
        if tesorero:
            return {
                "tes_idtesorero": tesorero[0],
                "usuario": {
			"user_idusuario": tesorero[8],
			"user_password": tesorero[11],
			"user_estado": tesorero[9],
			"user_fecha": tesorero[10],
            "rol_usuario": {
                "rol_idrol": tesorero[0],
			    "rol_nombrerol": tesorero[1]
            },
            "persona": {
                "pers_persona": tesorero[2],
                "pers_email": tesorero[3],
                "pers_nombres": tesorero[4],
                "pers_apellidos": tesorero[5],
                "pers_telefono": tesorero[6], 
                "pers_direccion": tesorero[7]
            }
        }
            }

    @classmethod
    def listAlicuotasActualizadas(self, alicuota_actualizadas) -> list:
        return [self.alicuota_actualizadaEntity(alicuota_actualizada) for alicuota_actualizada in alicuota_actualizadas]

    ##############################Tesorero
    @classmethod
    def tipodocumentoEntity(self, tipodocumento) -> dict:
        if tipodocumento:
            return {
            "tipdoc_id": tipodocumento[0],
            "tipdoc_nombre": tipodocumento[1]
        }
        else:
            return None

    @classmethod
    def listTipoDocumentos(self, tipodocumentos) -> list:
        return [self.tipodocumentoEntity(tp) for tp in tipodocumentos]

    @classmethod
    def documentoEntity(self, documentos) -> dict:
        if documentos:
            return {
            "doc_iddocumento": documentos[0],
    
            "tipo_documento":{
                "tipdoc_id":documentos[1]
                
                },
            "secretario":{
                "sec_idsecretario":documentos[2],
            },

            "doc_descripcion":documentos[3],
            "doc_documento":documentos[4],
            "doc_entidad":documentos[5],
            "doc_recibido":documentos[6],
     
                
         }
          
        else:
            return None

    @classmethod
    def listDocumentos(self, documentos) -> list:
        return [self.documentoEntity(doc) for doc in documentos]


    @classmethod
    def estado_documentosEntity(self, estado_documentos) -> dict:
        if estado_documentos:
            return  {
			"estdoc_id": estado_documentos[0],
			"documentos":{
                "doc_iddocumento":estado_documentos[1]
            },
			"aprobado_presidente": estado_documentos[2],
			"aprobado_entidad": estado_documentos[3],
            "fecha_aprovadopresidente":estado_documentos[4],
            "fecha_aprovadoentidad":estado_documentos[5]  
        }
        else:
            return None

    @classmethod
    def listEstadoDocumentos(self, estado_documentoss) -> list:
        return [self.estado_documentosEntity(ed) for ed in estado_documentoss]


    @classmethod
    def reunionEntity(self, reunion) -> dict:
        if reunion:
            return  {
			"reun_idreunion": reunion[0],
			"presidente":{
                "pres_idpresidente":reunion[1]
            },
            "multa":{
            "mult_idmulta":reunion[2]  
            },
            "reun_fecha":reunion[3],
            "reun_hora":reunion[4],
            "reun_descripcion":reunion[5],
            "reun_quorum":reunion[6],
            "reun_estado":reunion[7],
            "secretario":{
                "sec_idsecretario":reunion[8]
            }
			
        }
        else:
            return None

    @classmethod
    def listReunion(self, reuniones) -> list:
        return [self.reunionEntity(r) for r in reuniones]

@classmethod
def detallePagoEntity(self, detallepago) -> dict:
    if detallepago:
        return {
                "detpag_id": detallepago[0],
                "alicuota": {
                "ali_idalicuota": detallepago[0],
                "multa": {
                    "mult_idmulta": detallepago[1],
                    "mult_nombre": detallepago[2],
                    "mult_valor": detallepago[3]
                },
                "ali_fecha_actualizacion": detallepago[4].strftime('%d/%m/%Y'),
                "ali_valor_anterior": detallepago[5],
                "ali_valor_actual": detallepago[6]
            },
                "alicuota_actualizada": {
                "alic_id": detallepago[0],
                "alicuota": {
                    "ali_idalicuota": detallepago[1],
                    "multa": {
                        "mult_idmulta": detallepago[2],
                        "mult_nombre": detallepago[3],
                        "mult_valor": detallepago[4]
                },
                    "ali_fecha_actualizacion": detallepago[5],
                    "ali_valor_anterior": detallepago[6],
                    "ali_valor_actual": detallepago[7]
                },
                "alic_valor": detallepago[8],
                "alic_fecha": detallepago[9].strftime('%d/%m/%Y')
            },
                "detpag_subtotal": detallepago[3],
                "detpag_iva": detallepago[4],
                "detpag_total": detallepago[5],
                "detpag_fecha": detallepago[6],
                "detpag_multa": detallepago[7]
            }
    else:
        return None

    #07
    @classmethod
    def tesoreroEntity(self, tesorero) -> dict:
        if tesorero:
            return {
                "tes_idtesorero": tesorero[12],
                "usuario": {
                    "user_idusuario": tesorero[8],
                    "user_password": tesorero[11],
                    "user_estado": tesorero[9],
                    "user_fecha": tesorero[10].strftime('%d/%m/%Y'),
                    "rol_usuario": {
                        "rol_idrol": tesorero[0],
                        "rol_nombrerol": tesorero[1]
                        },
                    "persona": {
                        "pers_persona": tesorero[2],
                        "pers_email": tesorero[3],
                        "pers_nombres": tesorero[4],
                        "pers_apellidos": tesorero[5],
                        "pers_telefono": tesorero[6], 
                        "pers_direccion": tesorero[7]
                    }
                }
            }
        else:
            return None

    @classmethod
    def listTesoreros(self, tesoreros) -> list:
        return [self.tesoreroEntity(tesorero) for tesorero in tesoreros]

    #08
    @classmethod
    def secretarioEntity(self, secretario) -> dict:
        if secretario:
            return {
                "tes_idsecretario": secretario[12],
                "usuario": {
                    "user_idusuario": secretario[8],
                    "user_password": secretario[11],
                    "user_estado": secretario[9],
                    "user_fecha": secretario[10].strftime('%d/%m/%Y'),
                    "rol_usuario": {
                        "rol_idrol": secretario[0],
                        "rol_nombrerol": secretario[1]
                        },
                    "persona": {
                        "pers_persona": secretario[2],
                        "pers_email": secretario[3],
                        "pers_nombres": secretario[4],
                        "pers_apellidos": secretario[5],
                        "pers_telefono": secretario[6], 
                        "pers_direccion": secretario[7]
                    }
                }
            }
        else:
            return None

    @classmethod
    def listSecretarios(self, secretarios) -> list:
        return [self.secretarioEntity(secretario) for secretario in secretarios]

    #09
    @classmethod
    def presidenteEntity(self, presidente) -> dict:
        if presidente:
            return {
                "tes_idpresidente": presidente[12],
                "usuario": {
                    "user_idusuario": presidente[8],
                    "user_password": presidente[11],
                    "user_estado": presidente[9],
                    "user_fecha": presidente[10].strftime('%d/%m/%Y'),
                    "rol_usuario": {
                        "rol_idrol": presidente[0],
                        "rol_nombrerol": presidente[1]
                        },
                    "persona": {
                        "pers_persona": presidente[2],
                        "pers_email": presidente[3],
                        "pers_nombres": presidente[4],
                        "pers_apellidos": presidente[5],
                        "pers_telefono": presidente[6], 
                        "pers_direccion": presidente[7]
                    }
                }
            }
        else:
            return None

    @classmethod
    def listPresidentes(self, presidentes) -> list:
        return [self.presidenteEntity(presidente) for presidente in presidentes]

    #10
    @classmethod
    def condominoEntity(self, condomino) -> dict:
        if condomino:
            return {
                "tes_idcondomino": condomino[12],
                "usuario": {
                    "user_idusuario": condomino[8],
                    "user_password": condomino[11],
                    "user_estado": condomino[9],
                    "user_fecha": condomino[10].strftime('%d/%m/%Y'),
                    "rol_usuario": {
                        "rol_idrol": condomino[0],
                        "rol_nombrerol": condomino[1]
                        },
                    "persona": {
                        "pers_persona": condomino[2],
                        "pers_email": condomino[3],
                        "pers_nombres": condomino[4],
                        "pers_apellidos": condomino[5],
                        "pers_telefono": condomino[6], 
                        "pers_direccion": condomino[7]
                    }
                }
            }
        else:
            return None

    @classmethod
    def listCondominos(self, condominos) -> list:
        return [self.condominoEntity(condomino) for condomino in condominos]

    #11
    @classmethod
    def tipoServicioEntity(self, tiposervicio) -> dict:
        if tiposervicio:
            return {
                "tipserv_id": tiposervicio[0],
                "tipserv_nombre": tiposervicio[1]
            }
        else:
            return None

    @classmethod
    def listTipoServicios(self, tiposervicios) -> list:
        return [self.tipoServicioEntity(ts) for ts in tiposervicios]

    #12
    @classmethod
    def sericiosEntity(self, servicio) -> dict:
        if servicio:
            return {
                "serv_idservicios": servicio[0],
                "tipo_servicio": {
                    "tipserv_id": servicio[1],
                    "serv_nombreservicio": servicio[2],
                    "serv_descripcion": servicio[3],
                    "serv_valor": servicio[4],
                    "serv_iva": servicio[5],
                    "serv_cantidad": servicio[6]
                }
            }
        else:
            return None

    @classmethod
    def listServicios(self, servicios) -> list:
        return [self.sericiosEntity(serv) for serv in servicios]

    @classmethod
    def egresosEntity(self, egreso) -> dict:
        if egreso:
            return {
                "egre_id": egreso[0],
                "tesorero": {
                "tes_idtesorero": egreso[12],
                "usuario": {
                    "user_idusuario": egreso[8],
                    "user_password": egreso[11],
                    "user_estado": egreso[9],
                    "user_fecha": egreso[10].strftime('%d/%m/%Y'),
                    "rol_usuario": {
                        "rol_idrol": egreso[0],
                        "rol_nombrerol": egreso[1]
                        },
                    "persona": {
                        "pers_persona": egreso[2],
                        "pers_email": egreso[3],
                        "pers_nombres": egreso[4],
                        "pers_apellidos": egreso[5],
                        "pers_telefono": egreso[6], 
                        "pers_direccion": egreso[7]
                    }
                }
            },
                "egre_descripcion": egreso[2],
                "egre_subtotal": egreso[3],
                "egre_iva": egreso[4],
                "egre_total": egreso[5],
                "egre_fecha": egreso[6],
                "egre_numero": egreso[7]
            }
        else:
            return None

    @classmethod
    def listEgresos(self, egresos, tesorero) -> list:
        return [self.egresosEntity(egreso, tesorero) for egreso in egresos]

    @classmethod
    def detalleEgresoEntity(self, detalleegreso) -> dict:
        if detalleegreso:
            return {
                "detegre_id": detalleegreso[0],
                "egreso": {
                "egre_id": detalleegreso[0],
                "tesorero": {
                "tes_idtesorero": detalleegreso[12],
                "usuario": {
                    "user_idusuario": detalleegreso[8],
                    "user_password": detalleegreso[11],
                    "user_estado": detalleegreso[9],
                    "user_fecha": detalleegreso[10].strftime('%d/%m/%Y'),
                    "rol_usuario": {
                        "rol_idrol": detalleegreso[0],
                        "rol_nombrerol": detalleegreso[1]
                        },
                    "persona": {
                        "pers_persona": detalleegreso[2],
                        "pers_email": detalleegreso[3],
                        "pers_nombres": detalleegreso[4],
                        "pers_apellidos": detalleegreso[5],
                        "pers_telefono": detalleegreso[6], 
                        "pers_direccion": detalleegreso[7]
                    }
                }
            },
                "egre_descripcion": detalleegreso[2],
                "egre_subtotal": detalleegreso[3],
                "egre_iva": detalleegreso[4],
                "egre_total": detalleegreso[5],
                "egre_fecha": detalleegreso[6],
                "egre_numero": detalleegreso[7]
            },
                "detegre_numerofactura": detalleegreso[2], 
                "detegre_valorfactura": detalleegreso[3], 
                "detegre_documento": {
                    
                },
                "detegre_subtotal": detalleegreso[0],
                "detegre_iva": detalleegreso[0],
                "detegre_total": detalleegreso[0],
                "detegre_fecha": detalleegreso[0]
            }

    @classmethod
    def listDetalleEgresos(self, detaleegresos) -> list:
        return [self.detalleEgresoEntity(detaleegreso) for detaleegreso in detaleegresos]

    @classmethod
    def documentoEntity(self, data) -> dict:
        if data:
            return {
                "_id": str(data['_id']),
                "doc_iddocumento": data['doc_iddocumento'],
                "tipdoc_id": data['tipdoc_id'],
                "sec_idsecretario": data['sec_idsecretario'],
                "doc_descripcion": data['doc_descripcion'],
                "doc_documento": data['doc_documento'],
                "doc_entidad": data['doc_entidad'],
                "doc_recibido": data['doc_recibido']
            }
        else:
            return None

    @classmethod
    def listDocumentos(self, documentos) -> list:
        return [self.documentoEntity(doc) for doc in documentos]









class Rol_Usuario:

    def __init__(self, rol_idrol, rol_nombrerol):
        self.rol_idrol = rol_idrol
        self.rol_nombrerol = rol_nombrerol

    def convert_object_json_data(self, data):
        try:
            p = Rol_Usuario(data['rol_idrol'], data['rol_nombrerol'])
            return p
        except Exception as ex:
            raise Exception(ex)

    # Convert a json list to person Object
    def convert_object_list(self, list):
        try:
            data = json.loads(list)[0]
            p = Persona(data['pers_persona'], data['pers_email'], data['pers_nombres'],
                        data['pers_apellidos'], data['pers_telefono'], data['pers_direccion'])
            return p
        except Exception as ex:
            raise Exception(ex)

    def convert_to_json(self):
        return {
            "rol_idrol": self.rol_idrol,
            "rol_nombrerol": self.rol_nombrerol
        }


class Persona:
    def __init__(self, pers_persona, pers_email, pers_nombres, pers_apellidos, pers_telefono, pers_direccion):
        self.pers_persona = pers_persona
        self.pers_email = pers_email
        self.pers_nombres = pers_nombres
        self.pers_apellidos = pers_apellidos
        self.pers_telefono = pers_telefono
        self.pers_direccion = pers_direccion

    # Convert a json list to person Object
    def convert_object_list(self, list):
        try:
            data = list[0]
            p = Persona(data['pers_persona'], data['pers_email'], data['pers_nombres'],
                        data['pers_apellidos'], data['pers_telefono'], data['pers_direccion'])
            return p
        except Exception as ex:
            raise Exception(ex)

    # convert a json to Persona (Object)
    def convert_object_json_data(self, data):
        try:
            p = Persona(data['pers_persona'], data['pers_email'], data['pers_nombres'],
                        data['pers_apellidos'], data['pers_telefono'], data['pers_direccion'])
            return p
        except Exception as ex:
            raise Exception(ex)

    def convert_to_json(self):
        return {
            "pers_persona": self.pers_persona,
            "pers_email": self.pers_email,
            "pers_nombres": self.pers_nombres,
            "pers_apellidos": self.pers_apellidos,
            "pers_telefono": self.pers_telefono,
            "pers_direccion": self.pers_direccion
        }


class User_Usuario:

    def __init__(self, user_iduser, rol_usuario, persona, user_password, user_estado, user_fecha):
        self.user_idusuario = user_iduser
        self.rol_usuario = rol_usuario
        self.persona = persona
        self.user_password = user_password
        self.user_estado = user_estado
        self.user_fecha = user_fecha

    # Convert a json list to person Object
    def convert_object_list(self, list):
        try:
            data = json.loads(list)[0]
            p = Rol_Usuario(data['user_idusuario'], data['pers_email'], data['pers_nombres'],
                            data['pers_apellidos'], data['pers_telefono'], data['pers_direccion'])
            return p
        except Exception as ex:
            raise Exception(ex)

    # convert a json to Persona (Object)
    def convert_object_json_data(self, data):
        try:
            p = Persona(data['pers_persona'], data['pers_email'], data['pers_nombres'],
                        data['pers_apellidos'], data['pers_telefono'], data['pers_direccion'])
            return p
        except Exception as ex:
            raise Exception(ex)

    def convert_to_json(self):
        return {
            "user_idusuario": self.user_idusuario,
            "rol_usuario": self.rol_usuario.convert_to_json(),
            "persona": self.persona.convert_to_json(),
            "user_password": self.user_password,
            "user_estado": self.user_estado,
            "user_fecha": self.user_fecha
        }
        
        
    #########################333
    
class TipoDocumento:
    def __init__(self, tipdoc_id, tipdoc_nombre):
        self.tipdoc_id = tipdoc_id
        self.tipdoc_nombre = tipdoc_nombre
    # Convert a json list to person Object
    def convert_object_list(self, list):
        try:
            data = list[0]
            td = TipoDocumento(data['tipdoc_id'], data['tipdoc_nombre'])
            return td
        except Exception as ex:
            raise Exception(ex)

    # convert a json to Persona (Object)
    def convert_object_json_data(self, data):
        try:
            td = TipoDocumento(data['tipdoc_id'], data['tipdoc_nombre'])
            return td
        except Exception as ex:
            raise Exception(ex)

    def convert_to_json(self):
        return {
            "tipdoc_id": self.tipdoc_id,
            "tipdoc_nombre": self.tipdoc_nombre
        }

    
class Documento:
    def __init__(self, doc_iddocumento, tipdoc_id,sec_idsecretario,doc_descripcion,doc_documento,doc_entidad,doc_recibido):
        self.doc_iddocumento=doc_iddocumento
        self.tipdoc_id = tipdoc_id
        self.sec_idsecretario =sec_idsecretario
        self.doc_descripcion=doc_descripcion
        self.doc_documento=doc_documento
        self.doc_entidad=doc_entidad
        self.doc_recibido=doc_recibido 
        
        
    # Convert a json list to person Object
    def convert_object_list(self, list):
        try:
            data = list[0]
            d = Documento(data['doc_iddocumento'], data['tipdoc_id'], data['sec_idsecretario'], data['doc_descripcion'], data['doc_documento'], data['doc_entidad'], data['doc_recibido'])
            return d
        except Exception as ex:
            raise Exception(ex)

    # convert a json to Persona (Object)
    def convert_object_json_data(self, data):
        try:
            d = Documento(data['doc_iddocumento'], data['tipdoc_id'], data['sec_idsecretario'], data['doc_descripcion'], data['doc_documento'], data['doc_entidad'], data['doc_recibido'])
            return d
        except Exception as ex:
            raise Exception(ex)

    def convert_to_json(self):
        return {
            "doc_iddocumento":self.doc_iddocumento,
            "tipdoc_id": self.tipdoc_id,
            "sec_idsecretario": self.sec_idsecretario,
            "doc_descripcion": self.doc_descripcion,
            "doc_documento":self.doc_documento,
            "doc_entidad":self.doc_entidad,
            "doc_recibido":self.doc_recibido
            
            
        }
        
        
class Estado_Documento:
    def __init__(self, estdoc_id, doc_iddocumento,aprobado_presidente,aprobado_entidad,fecha_aprovadopresidente,fecha_aprobadoentidad):
        self.estdoc_id = estdoc_id
        self.doc_iddocumento = doc_iddocumento
        self.aprobado_presidente = aprobado_presidente
        self.aprobado_entidad=aprobado_entidad        
        self.fecha_aprovadopresidente = fecha_aprovadopresidente
        self.fecha_aprobadoentidad=fecha_aprobadoentidad
    # Convert a json list to person Object
    def convert_object_list(self, list):
        try:
            data = list[0]
            ed = Estado_Documento(data['estdoc_id'], data['doc_iddocumento'],data['aprobado_presidente'],data['aprobado_entidad'],data['fecha_aprovadopresidente'],data['fecha_aprobadoentidad'])
            return ed
        except Exception as ex:
            raise Exception(ex)

    # convert a json to Persona (Object)
    def convert_object_json_data(self, data):
        try:
             ed = Estado_Documento(data['estdoc_id'], data['doc_iddocumento'],data['aprobado_presidente'],data['aprobado_entidad'],data['fecha_aprovadopresidente'],data['fecha_aprobadoentidad'])
             return ed
        except Exception as ex:
            raise Exception(ex)

    def convert_to_json(self):
        return {
            "estdoc_id": self.estdoc_id,
            "doc_iddocumento": self.doc_idocumento,
            "aprobado_presidente":self.aprobado_presidente,
            "aprobado_entidad": self.aprobado_entidad,
            "fecha_aprovadopresidente":self.fecha_aprovadopresidente,
            "fecha_aprobadoentidad":self.fecha_aprobadoentidad
        }

              
class Reunion:
    def __init__(self,reun_idreunion, pres_idpresidente,mult_idmulta,reun_fecha,reun_hora,reun_descripcion,reun_quorum,reun_estado,secretario):
        self.reun_idreunion = reun_idreunion
        self.pres_idpresidente = pres_idpresidente
        self.mult_idmulta = mult_idmulta
        self.reun_fecha=reun_fecha        
        self.reun_hora = reun_hora
        self.reun_descripcion=reun_descripcion
        self.reun_quorum=reun_quorum
        self.reun_estado=reun_estado
        self.secretario=secretario
    # Convert a json list to person Object
    def convert_object_list(self, list):
        try:
            data = list[0]
            ed = Reunion(data['reun_idreunion'], data['pres_idpresidente'],data[' mult_idmulta'],data['reun_fecha'],data['reun_hora'],data['reun_descripcion'],data['reun_quorum'],data['reun_estado'],data['secretario'] )
            return ed
        except Exception as ex:
            raise Exception(ex)

    # convert a json to Persona (Object)
    def convert_object_json_data(self, data):
        try:
             ed = Reunion(data['reun_idreunion'], data['pres_idpresidente'],data[' mult_idmulta'],data['reun_fecha'],data['reun_hora'],data['reun_descripcion'],data['reun_quorum'],data['reun_estado'],data['secretario'] )
             return ed
        except Exception as ex:
            raise Exception(ex)

    def convert_to_json(self):
        return {
            "reun_idreunion": self.reun_idreunion,
            "pres_idpresidente": self.pres_idpresidente,
            "mult_idmulta":self.mult_idmulta,
            "reun_fecha": self.reun_fecha,
            "reun_hora":self.reun_hora,
            "reun_descripcion":self.reun_descripcion,
            "reun_quorum":self.reun_quorum,
            "reun_estado":self.reun_estado,
            "secretario":self.secretario
        }
        