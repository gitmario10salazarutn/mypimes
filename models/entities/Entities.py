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
    def list_rolUsuarios(self, rol_usuarios) -> list:
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
            return {
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
                "ali_idalicuota": alicuota[4],
                "multa": {
                    "mult_idmulta": alicuota[0],
                    "mult_nombre": alicuota[1],
                    "mult_valor": alicuota[2]
                },
                "ali_fecha_actualizacion": alicuota[5].strftime('%d/%m/%Y'),
                "ali_valor_anterior": alicuota[6],
                "ali_valor_actual": alicuota[7],
                "estado_delete_alicuota": alicuota[8]
            }
        else:
            return None

    @classmethod
    def listAlicuotas(self, alicuotas) -> list:
        return [self.alicuotaEntity(alicuota) for alicuota in alicuotas]

    @classmethod
    def alicuota_actualizadaEntity(self, alicuota_actualizada) -> dict:
        if alicuota_actualizada:
            return {
                "alic_id": alicuota_actualizada[9],
                "alicuota": {
                    "ali_idalicuota": alicuota_actualizada[4],
                    "multa": {
                        "mult_idmulta": alicuota_actualizada[0],
                        "mult_nombre": alicuota_actualizada[1],
                        "mult_valor": alicuota_actualizada[2]
                    },
                    "ali_fecha_actualizacion": alicuota_actualizada[5].strftime('%d/%m/%Y'),
                    "ali_valor_anterior": alicuota_actualizada[6],
                    "ali_valor_actual": alicuota_actualizada[7]
                },
                "alic_valor": alicuota_actualizada[10],
                "alic_fecha": alicuota_actualizada[11].strftime('%d/%m/%Y')
            }
        else:
            return None

    @classmethod
    def listAlicuotasActualizadas(self, alicuota_actualizadas) -> list:
        return [self.alicuota_actualizadaEntity(a) for a in alicuota_actualizadas]

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
                "doc_iddocumento": documentos[14],

                "tipo_documento": {
                    "tipdoc_id": documentos[15],
                    "tipdoc_nombre": documentos[23]
                },
                "secretario": {
                    "sec_idsecretario": documentos[12],
                    "usuario": {
                        "user_idusuario": documentos[8],
                        "user_password": documentos[11],
                        "user_estado": documentos[9],
                        "user_fecha": documentos[10].strftime('%d/%m/%Y'),
                        "rol_usuario": {
                            "rol_idrol": documentos[0],
                            "rol_nombrerol": documentos[1]
                        },
                        "persona": {
                            "pers_persona": documentos[2],
                            "pers_email": documentos[3],
                            "pers_nombres": documentos[4],
                            "pers_apellidos": documentos[5],
                            "pers_telefono": documentos[6],
                            "pers_direccion": documentos[7]
                        }
                    },
                    "estado_delete": documentos[13]
                },
                "doc_descripcion": documentos[17],
                "doc_documento": documentos[18],
                "doc_entidad": documentos[19],
                "doc_recibido": documentos[20],
                "estado_delete": documentos[21]
            }
        else:
            return None

    @classmethod
    def listDocumentos(self, documentos) -> list:
        return [self.documentoEntity(doc) for doc in documentos]

    @classmethod
    def documentov2Entity(self, documentos) -> dict:
        if documentos:
            return {
                "doc_iddocumento": documentos[0],
                "tipo_documento": {
                    "tipdoc_id": documentos[1],
                    "tipdoc_nombre": documentos[2]
                },
                "secretario": {
                    "sec_idsecretario": documentos[3]

                },
                "doc_descripcion": documentos[4],
                "doc_documento": documentos[5],
                "doc_entidad": documentos[6],
                "doc_recibido": documentos[7],
                "estado_delete": documentos[8]
            }
        else:
            return None

    @classmethod
    def listDocumentosv2(self, documentos) -> list:
        return [self.documentoEntity(doc) for doc in documentos]

    @classmethod
    def estado_documentosEntity(self, estado_documentos) -> dict:
        if estado_documentos:
            return {
                "estdoc_id": estado_documentos[0],
                "documentos": {
                    "doc_iddocumento": estado_documentos[1]
                },
                "aprobado_presidente": estado_documentos[2],
                "aprobado_entidad": estado_documentos[3],
                "fecha_aprovadopresidente": estado_documentos[4],
                "fecha_aprovadoentidad": estado_documentos[5]
            }
        else:
            return None

    @classmethod
    def listEstadoDocumentos(self, estado_documentoss) -> list:
        return [self.estado_documentosEntity(ed) for ed in estado_documentoss]

    @classmethod
    def reunionEntity(self, reunion) -> dict:
        if reunion:
            return {
                "reun_idreunion": reunion[0],
                "presidente": {
                    "pres_idpresidente": reunion[1],
                    "usuario": {
                        "user_idusuario": reunion[17],
                        "user_password": reunion[20],
                        "user_estado": reunion[18],
                        "user_fecha": reunion[19].strftime('%d/%m/%Y'),
                        "rol_usuario": {
                            "rol_idrol": reunion[9],
                            "rol_nombrerol": reunion[10]
                        },
                        "persona": {
                            "pers_persona": reunion[11],
                            "pers_email": reunion[12],
                            "pers_nombres": reunion[13],
                            "pers_apellidos": reunion[14],
                            "pers_telefono": reunion[15],
                            "pers_direccion": reunion[16]
                        }
                    }
                },
                "multa": {
                    "mult_idmulta": reunion[2],
                    "mult_nombre": reunion[37],
                    "mult_valor": reunion[38]
                },
                "reun_fecha": reunion[3].strftime('%d/%m/%Y'),
                "reun_hora": reunion[4].strftime("%H:%M:%S"),
                "reun_descripcion": reunion[5],
                "reun_quorum": reunion[6],
                "reun_estado": reunion[7],
                "secretario": {
                    "sec_idsecretario": reunion[8],
                    "usuario": {
                        "user_idusuario": reunion[31],
                        "user_password": reunion[34],
                        "user_estado": reunion[32],
                        "user_fecha": reunion[33].strftime('%d/%m/%Y'),
                        "rol_usuario": {
                            "rol_idrol": reunion[23],
                            "rol_nombrerol": reunion[24]
                        },
                        "persona": {
                            "pers_persona": reunion[25],
                            "pers_email": reunion[26],
                            "pers_nombres": reunion[27],
                            "pers_apellidos": reunion[28],
                            "pers_telefono": reunion[29],
                            "pers_direccion": reunion[30]
                        }
                    }
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
            pa = detallepago[9:]
            tesorero = pa[:14]
            alicuota = pa[14:23]
            condomino = pa[23:37]
            alicuota_actualizada = pa[37:]
            return {
                "detpag_id": detallepago[0],
                "pago_alicuota": {
                    "pagali_id": pa[14],
                    "tesorero": {
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
                    },
                    "condomino": {
                        "cond_idcondomino": condomino[12],
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
                    },
                    "pagali_fecha": alicuota[3].strftime('%d/%m%Y'),
                    "pagali_numero": alicuota[4],
                    "pagali_subtotal": alicuota[5],
                    "pagali_iva": alicuota[6],
                    "pagali_tota": alicuota[7],
                    "estado_delete": alicuota[8]
                },
                "alicuota_actualizada": {
                    "alic_id": alicuota_actualizada[9],
                    "alicuota": {
                        "ali_idalicuota": alicuota_actualizada[4],
                        "multa": {
                            "mult_idmulta": alicuota_actualizada[0],
                            "mult_nombre": alicuota_actualizada[1],
                            "mult_valor": alicuota_actualizada[2]
                        },
                        "ali_fecha_actualizacion": alicuota_actualizada[5].strftime('%d/%m/%Y'),
                        "ali_valor_anterior": alicuota_actualizada[6],
                        "ali_valor_actual": alicuota_actualizada[7]
                    },
                    "alic_valor": alicuota_actualizada[10],
                    "alic_fecha": alicuota_actualizada[11].strftime('%d/%m/%Y')
                },
                "detpag_subtotal": detallepago[3],
                "detpag_iva": detallepago[4],
                "detpag_total": detallepago[5],
                "detpag_fecha": detallepago[6],
                "detpag_multa": detallepago[7]
            }
        else:
            return None

    @classmethod
    def listDetallePagos(self, detpags) -> list:
        return [self.detallePagoEntity(dp) for dp in detpags]

    # 07
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

    # 08
    @classmethod
    def secretarioEntity(self, secretario) -> dict:
        if secretario:
            return {
                "sec_idsecretario": secretario[12],
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

    # 09
    @classmethod
    def presidenteEntity(self, presidente) -> dict:
        if presidente:
            return {
                "pres_idpresidente": presidente[12],
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

    # 10
    @classmethod
    def condominoEntity(self, condomino) -> dict:
        if condomino:
            return {
                "cond_idcondomino": condomino[12],
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

    # 11
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

    # 12
    @classmethod
    def serviciosEntity(self, servicio) -> dict:
        if servicio:
            return {
                "serv_idservicios": servicio[0],
                "tipo_servicio": {
                    "tipserv_id": servicio[1],
                    "tipserv_nombre": servicio[2]
                },
                "serv_nombreservicio": servicio[3],
                "serv_descripcion": servicio[4],
                "serv_valor": servicio[5],
                "serv_iva": servicio[6],
                "serv_cantidad": servicio[7]
            }
        else:
            return None

    @classmethod
    def listServicios(self, servicios) -> list:
        return [self.serviciosEntity(serv) for serv in servicios]

    @classmethod
    def egresosEntity(self, e) -> dict:
        if e:
            tesorero = e[:14]
            egreso = e[14:]
            return {
                "egre_id": egreso[0],
                "tesorero": {
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
    def listEgresos(self, egresos) -> list:
        return [self.egresosEntity(egreso) for egreso in egresos]

    @classmethod
    def detalleEgresoEntity(self, detalleegreso) -> dict:
        if detalleegreso:
            doc = detalleegreso[10:35]
            e = detalleegreso[35:]
            return {
                "detegre_id": detalleegreso[0],
                "egreso": self.egresosEntity(e),
                "detegre_numerofactura": detalleegreso[2],
                "detegre_valorfactura": detalleegreso[3],
                "detegre_documento": self.documentoEntity(doc),
                "detegre_subtotal": detalleegreso[5],
                "detegre_iva": detalleegreso[6],
                "detegre_total": detalleegreso[7],
                "detegre_fecha": detalleegreso[8],
                "estado_delete": detalleegreso[9]
            }

    @classmethod
    def listDetalleEgresos(self, detaleegresos) -> list:
        return [self.detalleEgresoEntity(detaleegreso) for detaleegreso in detaleegresos]

    @classmethod
    def reservacionesEntity(self, reservacion) -> dict:
        if reservacion:
            return {
                "resv_idreservacion": reservacion[0],
                "servicios": {
                    "serv_idservicios": reservacion[1],
                    "tipo_servicio": {
                        "tipserv_id": reservacion[2],
                        "tipserv_nombre": reservacion[3]
                    },
                    "serv_nombreservicio": reservacion[4],
                    "serv_descripcion": reservacion[5],
                    "serv_valor": reservacion[6],
                    "serv_iva": reservacion[7],
                    "serv_cantidad": reservacion[8]
                },
                "resv_fecha": reservacion[9].strftime('%d/%m/%Y'),
                "resv_descripcion": reservacion[10],
                "estado_delete": reservacion[11]
            }
        else:
            return None

    @classmethod
    def listReservaciones(self, reservaciones) -> list:
        return [self.reservacionesEntity(resv) for resv in reservaciones]

    @classmethod
    def detalleReservacionesEntity(self, d) -> dict:
        if d:
            detres = d[:24]
            cab_resv = d[24:]
            return {
                "detres_iddetalle": detres[14],
                "reservacion": {
                    "resv_idreservacion": detres[0],
                    "servicios": {
                        "serv_idservicios": detres[4],
                        "tipo_servicio": {
                            "tipserv_id": detres[11],
                            "tipserv_nombre": detres[12]
                        },
                        "serv_nombreservicio": detres[5],
                        "serv_descripcion": detres[6],
                        "serv_valor": detres[7],
                        "serv_iva": detres[8],
                        "serv_cantidad": detres[9]
                    },
                    "resv_fecha": detres[1].strftime('%d/%m/%Y'),
                    "resv_descripcion": detres[2],
                    "estado_delete": detres[3]
                },
                "detres_subtotal": detres[15],
                "detres_iva": detres[16],
                "detres_total": detres[17],
                "detres_cantidad": detres[18],
                "detres_horainicio": detres[19].strftime("%H:%M:%S"),
                "detres_horafin": detres[20].strftime("%H:%M:%S"),
                "detres_fecha": detres[21].strftime('%d/%m/%Y'),
                "estado_delete": detres[22],
                "cabecera_reservacion": self.cabeceraRecervacionesEntity(cab_resv)
            }
        else:
            return None

    @classmethod
    def listDetalleReservaciones(self, detalle_reservaciones) -> list:
        return [self.detalleReservacionesEntity(dr) for dr in detalle_reservaciones]

    @classmethod
    def pago_alicuotaEntity(self, pa) -> dict:
        if pa:
            tesorero = pa[:14]
            alicuota = pa[14:23]
            condomino = pa[23:]
            return {
                "pagali_id": pa[14],
                "tesorero": {
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
                },
                "condomino": {
                    "cond_idcondomino": condomino[12],
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
                },
                "pagali_fecha": alicuota[3].strftime('%d/%m%Y'),
                "pagali_numero": alicuota[4],
                "pagali_subtotal": alicuota[5],
                "pagali_iva": alicuota[6],
                "pagali_tota": alicuota[7],
                "estado_delete": alicuota[8]
            }
        else:
            return None

    @classmethod
    def listPagoAlicuotas(self, pag_alis) -> list:
        return [self.pago_alicuotaEntity(pa) for pa in pag_alis]

    @classmethod
    def Detalle_Reservaciones(self, data) -> dict:
        if data:
            return {
                "reservacion": data[0],
                "detres_cabreservacion": data[1],
                "detres_subtotal": float(f"{data[2]:.2f}"),
                "detres_iva": float(f"{data[3]:.2f}"),
                "detres_total": float(f"{data[4]:.2f}"),
                "detres_cantidad": data[5],
                "detres_horainicio": data[6].strftime("%H:%M:%S"),
                "detres_horafin": data[7].strftime("%H:%M:%S"),
                "detres_fecha": data[8].strftime('%d/%m%Y'),
                "estado_delete_detres": data[9],
                "servicio": data[10]
            }
        else:
            return None


    @classmethod
    def Detalle_Reservaciones1(self, data) -> dict:
        if data:
            return {
                "reservacion": data[0],
                "detres_cabreservacion": data[1],
                "detres_subtotal": float(f"{data[2]:.2f}"),
                "detres_iva": float(f"{data[3]:.2f}"),
                "detres_total": float(f"{data[4]:.2f}"),
                "detres_cantidad": data[5],
                "detres_horainicio": data[6],
                "detres_horafin": data[7],
                "detres_fecha": data[8],
                "estado_delete_detres": data[9],
                "servicio": data[10]
            }
        else:
            return None

    @classmethod
    def ListDetalle_Reservaciones(self, pag_alis) -> list:
        return [self.Detalle_Reservaciones(pa) for pa in pag_alis]

    @classmethod
    def cabeceraRecervacionesEntity(self, data) -> dict:
        if data:
            condomino = data[:14]
            cab_resv = data[14:22]
            secretario = data[22:]
            return {
                "id_cabreservacion": cab_resv[0],
                "cabres_secretario": self.secretarioEntity(secretario),
                "cabres_condomino": self.condominoEntity(condomino),
                "cabres_subtotal": cab_resv[3],
                "cabres_iva": cab_resv[4],
                "cabres_total": cab_resv[5],
                "cabres_numero": cab_resv[6],
                "cabres_fecha": cab_resv[7].strftime('%d/%m/%Y'),
            }

    @classmethod
    def listCabeceraReservaciones(self, list) -> list:
        return [self.cabeceraRecervacionesEntity(cr) for cr in list]

    @classmethod
    def Detalle_Pago(self, data) -> dict:
        if data:
            return {
                "pagali_id": data[0],
                "aliact_id": data[1],
                "detpag_subtotal": float(f"{data[2]:.2f}"),
                "detpag_iva": float(f"{data[3]:.2f}"),
                "detpag_total": float(f"{data[4]:.2f}"),
                "detpag_fecha": data[5],
                "detpag_multa": data[6],
                "estado_delete_detpag": data[7]
            }
        else:
            return None

    @classmethod
    def Detalle_Egreso(self, data) -> dict:
        if data:
            return {
                "egre_id": data[0],
                "detegre_numerofactura": data[1],
                "detegre_valorfactura": data[2],
                "deteegre_documento": data[3],
                "detegre_subtotal": float(f"{data[4]:.2f}"),
                "detegre_iva": float(f"{data[5]:.2f}"),
                "detegre_total": float(f"{data[6]:.2f}"),
                "detegre_fecha": data[7],
                "estado_delete_detegre": data[8]
            }
        else:
            return None


# (1, 22, 1, '2023-5-2', '000-025', 1897.12, 458.36, 2365.45, False)
