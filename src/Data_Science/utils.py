import os
import sys
from src.Data_Science.Exception import CustomException
from src.Data_Science.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_QSL_data():
    logging.info("Reading SQL data started")

    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )
        logging.info("Connection established",mydb)
        df = pd.read_sql_query("select * from student",mydb)
        print(df.head())

        return df
    except Exception as e:
        raise CustomException(e,sys)

