import os
import sys
'''

# Get the absolute path to the src directory
src_dir = os.path.dirname(os.path.abspath(__file__))

# Add the src directory to the Python path
sys.path.insert(0, src_dir)

# Now you can import modules from src
# from logger import logging
# from exception import CustomException
'''

# Get the absolute path to the project directory
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project directory to the Python path
sys.path.insert(0, project_dir)

# Now you can import modules from src

# from src.exception import CustomException   error show
# from src.logger import logging
from exception import CustomException
from logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Get the absolute path to the project directory
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project directory to the Python path
sys.path.insert(0, project_dir)

from data_transformation import DataTransformation
from data_transformation import DataTransformationConfig

from model_trainer import ModelTrainerConfig
from model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('S:\\Coding\\vs_code\\ML\\mlproject\\notebook\\data\\stud.csv')
            # df=pd.read_csv('notebook\data\stud.csv')error
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))