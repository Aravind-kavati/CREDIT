import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import Dataingestion

if __name__=='__main__':
    obj=Dataingestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()