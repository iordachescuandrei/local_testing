import logging
import time

def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

if __name__ == "__main__":
    print ("Start job here")
    while (1):
        get_module_logger(__name__).info("Still Alive")
        time.sleep(2)


#this script is sending logs every 3 seconds