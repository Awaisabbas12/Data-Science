from src.Data_Science.logger import logging
from src.Data_Science.Exception import CustomException
import sys
from src.Data_Science.components.data_ingestion import dataingestion
from src.Data_Science.components.data_ingestion import dataingestionconfig


if __name__ =='__main__':
    logging.info("The execution is Started")
    try:
       # data_ingestion_config = dataingestionconfig()
        data_ingestion = dataingestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)