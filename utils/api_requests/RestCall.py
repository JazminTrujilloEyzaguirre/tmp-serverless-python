import logging

import os
import simplejson
import requests
import boto3
from utils.gen import set_produccion

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from utils.responses_setup import setea_respuesta

header_polizas = {
        'Content-Type': 'application/json',
        'charset': 'utf-8',
        'User-Agent': 'PostmanRuntime/7.26.10',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Conneection': 'keep-alive'
    }

lambda_client = boto3.client("lambda", region_name=os.getenv('REGION_NAME_BY_STAGE'))

class ExternalApiFailed(Exception):
    """ excepciones para retry """
    pass

class RestCall:
    def __init__(self, payload, id_lead):
        self.id_lead = id_lead
        self.payload = payload

    def service_get(self):
        try:
            payload = self.payload
            res = requests.get(
                "https://apidev.bicevida.cl/v1/personas/13687060/", headers=header_polizas, data=payload.encode("utf-8")
            )
            response = setea_respuesta(res, "get-persona")
            logger.info(response)
            return response

        except Exception as e:
            logger.exception("[ service_clonar_poliza ] ocurrio una excepcion: " + str(e))


