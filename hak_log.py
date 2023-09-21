import logging


logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                    level=logging.DEBUG)

LEVEL_MAP = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'error': logging.ERROR
}

class log:
    def info(msg : str):
        logging.info(msg)
    
    def error(msg : str):
        logging.error(msg)
    
    def debug(msg : str):
        logging.debug(msg)
    
