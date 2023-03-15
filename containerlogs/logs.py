import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
counter =0
while True:
    logging.info('This is an info message, counter is %d', counter)
    time.sleep(3)
    counter=counter+1


