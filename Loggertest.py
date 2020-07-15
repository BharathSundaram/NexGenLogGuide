#importing module 
import logging 
  
#Create and configure logger 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s' ) 
  
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
#logger.setLevel(logging.DEBUG) 
  
#Test messages 
if __name__ == "__main__":
    logger.debug(__name__,"Harmless debug Message") 
    logger.info("Just an information") 
    logger.warning("Its a Warning") 
    logger.error("Did you try to divide by zero") 
    logger.critical("Internet is down") 