import logging

from utils.gen import create_date, separate_rut

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def payload_transform(val):
    detalle = val["detail"]
    detalle["totalAmount"] = str(detalle["totalAmount"])
    return detalle
