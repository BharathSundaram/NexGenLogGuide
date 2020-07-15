# setup_logger.py
import logging
import sys
#logging.disable(logging.NOTSET)    
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
logger = logging.getLogger()
