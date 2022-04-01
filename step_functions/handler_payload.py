import logging
import simplejson

from utils.payloads_setup import payload_transform

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(message, context):
    """ Solo recibe un payload """
    try:
        event_detail = payload_transform(message)
        event_detail["mensaje"] = "Se transformó correctamente el payload"
        return event_detail

    except Exception as e:
        logger.exception(str(e))
        raise Exception(500, e, simplejson.dumps(message), 'handler_payload')
