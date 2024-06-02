import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import os
from src.Data_Science.Exception import CustomException
from src.Data_Science.logger import logging
from src.Data_Science.utils import save_object
@dataclass
class Datatransformationconfig:
    preprocessor_obj_file_path=os.path.join('artifact','preprocessor.pkl')

class Datatransformation:
    def __init__(self):
        self.data_transformation_config = Datatransformationconfig

    def get_data_tranformer_obj(self) :
        '''
        This function is responsible for data transformation

        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
            ])
            cat_pipline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder())
            ])
            logging.info(f"Categorical columns:{cat_pipline}")
            logging.info(f"Numerical columns:{num_pipline}")

            preprocessor = ColumnTransformer([
                ("numerical_pipline",num_pipline,numerical_columns),
                ("catogerical_pipline",cat_pipline,categorical_columns)
            ])
            return preprocessor
        except Exception as e:

            raise CustomException (e,sys)
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading the train and test file")

            preprocessing_obj = self.get_data_tranformer_obj()
            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            ## divide the train dataset to independent and dependent feature

            input_features_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            ## divide the test dataset to independent and dependent feature

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info("Applying Preprocessing on training and test dataframe")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)


            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (

                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        