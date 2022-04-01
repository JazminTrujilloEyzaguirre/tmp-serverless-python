import logging
import simplejson

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def setea_respuesta(res, step_name):
        print("res:")
        print(res)
        logger.info("EL STATUS CODE ES: " + str(res.status_code))
        if res.status_code == 201 or res.status_code == 200:
            response = simplejson.loads(res.text)
            retorno = {
                "status_code":res.status_code,
                "response": response
            }
            return retorno
        else:
            logger.info("el codigo no es 200")
            logger.info(res.text)
            res_json = simplejson.loads(res.text)
            if "message" in res_json:
                response = res_json['message']
            else:
                response = res_json['descripcion']

            retorno = {
                "status_code":res.status_code,
                "response": response
            }
            return retorno
