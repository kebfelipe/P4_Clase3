from controller.bitacora import configurar_logger, guardar_log
from controller.bdd import bddMongo

principal = configurar_logger("principal")

bases = configurar_logger("bases")

estudiante = bddMongo('localhost','8001','ADMIN','admin','estudiante')

estudianteNuevo = {
    "nombre":"Mynor",
    "nota":25,
    "clasificacion":"alta"
}

estudiante.insertar(estudianteNuevo,"estudiantes")