from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging




##configuration of the data ingestion config

from networksecurity.entity.config_entity import DataIngestionConfig

import os
import sys
import numpy as np 
import pymongo
from typing import List
from sklearn.model_selection import train_test_split


from dotenv import load_dotenv
load_dotenv()


MONGO_DB_URL=os.getenv("MONGO_DB_URL")


class DataIngestion:
    def __init__(self,data_ingestion_config):
        


