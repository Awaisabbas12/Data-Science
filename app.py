from src.Data_Science.logger import logging
from src.Data_Science.Exception import CustomException
import sys
from src.Data_Science.components.data_ingestion import dataingestion
from src.Data_Science.components.data_ingestion import dataingestionconfig
from src.Data_Science.components.data_transformation import Datatransformationconfig,Datatransformation


if __name__ =='__main__':
    logging.info("The execution is Started")
    try:
       # data_ingestion_config = dataingestionconfig()
        data_ingestion = dataingestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        data_tranformations = Datatransformation()
        data_tranformations.initiate_data_transformation(train_data_path,test_data_path)



    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)