from src.Data_Science.logger import logging
from src.Data_Science.Exeption import CustomException
import sys


if __name__ =='__main__':
    logging.info("The execution is Started")
    try:
        a=1/0
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)