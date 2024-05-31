import os
import sys
from src.Data_Science.Exception import CustomException
from src.Data_Science.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.Data_Science.utils import read_QSL_data
from sklearn.model_selection import train_test_split
@dataclass

class dataingestionconfig:
    train_data_path:str = os.path.join('artifact','train.csv')
    test_data_path:str = os.path.join('artifact','test.csv')
    Raw_data_path:str = os.path.join('artifact','Raw.csv')

class dataingestion:
    def __init__(self):
        self.ingestion_config = dataingestionconfig()

    def initiate_data_ingestion(self):
        try:
            ##reading code
            df = read_QSL_data()
            logging.info("Reading completed from MySQL")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.Raw_data_path,index=False,header=True)

            train_set,test_set = train_test_split(df,test_size=0.2)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            logging.info("Data ingestion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)