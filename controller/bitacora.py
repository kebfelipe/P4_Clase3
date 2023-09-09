import logging

def configurar_logger(nombre_archivo):
    logger = logging.getLogger(nombre_archivo)
    logger.setLevel(logging.DEBUG)

    #Crearel formato
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    #Preparamos el archivo
    archi = logging.FileHandler(nombre_archivo + '.log')
    archi.setFormatter(formatter)
    archi.setLevel(logging.DEBUG)

    #Preparar la consola
    consol = logging.StreamHandler()
    consol.setFormatter(formatter)
    consol.setLevel(logging.DEBUG)

    logger.addHandler(archi)
    logger.addHandler(consol)

    return logger

def guardar_log(tipo, mensaje, logger):
    tipo = tipo.lower()
    mensaje = mensaje.lower()

    if tipo not in ['info', 'error', 'alerta']:
        raise ValueError('El tipo de bitacora debe ser info, error o alerta.')
    
    if tipo == 'info':
        logger.info(mensaje)
    elif tipo == 'error':
        logger.error(mensaje)
    elif tipo == 'alerta':
        logger.warning(mensaje)
    