import logging

from utils.api_requests import RestCall
from utils.api_requests.Exceptions import TooManyRequestsException, ServerUnavailableException, UnknownException

import simplejson

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(message, context):
    """ se consulta un endpoint api personas """
    try:
        res_call = RestCall()
        response = res_call.service_get()
        statuscode = response["statuscode"]
        if statuscode == "429":
            raise TooManyRequestsException('429 Too Many Requests')
        elif statuscode == "503":
            raise ServerUnavailableException('503 Server Unavailable')
        elif statuscode == "200":
            return '200 OK'
        else:
            raise UnknownException('Unknown error')

        #return response

    except Exception as e:
        raise Exception(500, e, simplejson.dumps(message), 'handler_exceptions')
