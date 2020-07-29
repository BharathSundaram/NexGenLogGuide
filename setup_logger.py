# setup_logger.py
import logging
import sys
__author__ = "Bharath Shanmugasundaram"

logging.disable(logging.CRITICAL)    
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
logger = logging.getLogger()
