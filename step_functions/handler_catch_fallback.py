import logging

import simplejson

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(message, context):
    """ se encarga de manejar y notificar por sns las excepciones que se presenten en el proceso """
    try:
        logger.info("Enviando alarmas")
        mensaje = simplejson.loads(message['Cause'])
        mensaje_labs = mensaje['errorMessage']
        logger.info(mensaje_labs)
        raise ValueError(mensaje_labs)
    except Exception as e:
        logger.exception(str(e))
        raise Exception(500, e, "Error en el proceso", "handler_catch_fallback.handler")
