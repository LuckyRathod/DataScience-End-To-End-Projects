import os 
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass ##It is used to create class variables
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

## It includes all the inputs which are required for data ingestion
## You can directly define your class variable without using __init__ with the help of dataclass
## All outputs will be saved in artifacts folder
## DataIngestionConfig knows where to save the train path and test path 
@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts',"train.csv")
    test_data_path : str = os.path.join('artifacts',"test.csv")
    raw_data_path : str = os.path.join('artifacts',"data.csv")

class DataIngestion:
     def __init__(self):
          ## As soon as you call DataIngestionConfig . All above three variable will get stored in ingestion_config
          self.ingestion_config = DataIngestionConfig()
    
     ## Read the dataset 
     def initiate_data_ingestion(self):
          logging.info("Entered the data ingestion method or component")
          try:
               df = pd.read_csv('/Users/mfho-27019739/Desktop/AIML/Github/End-To-End-Projects/Machine_Learning/Projects/p1/notebook/data/stud.csv')
               logging.info("Have read the dataset as dataframe")

               ## Now we will create the folders which are mentioned in DataIngestionConfig 
               os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
               df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

               logging.info('Train Test split initiated')
               train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
               train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
               test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
               logging.info("Ingestion of data is complted")

               return (
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path,
               )

          except Exception as e:
               raise CustomException(e,sys)
          

if __name__ == "__main__":
     obj = DataIngestion()
     train_data,test_data = obj.initiate_data_ingestion() 
     
     data_transformation = DataTransformation()
     train_arr,test_arr,_= data_transformation.initiate_data_transformation(train_data,test_data)

     model_trainer = ModelTrainer()
     print(model_trainer.initiate_model_trainer(train_arr,test_arr))

   