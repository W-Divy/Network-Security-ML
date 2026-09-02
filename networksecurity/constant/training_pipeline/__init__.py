import os 
import sys
import numpy as np
import pandas as pd

"""defining common constant variable for training pipeline"""

TARGET_COLUMN="Result"
PIPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="Artifacts"
FILE_NAME:str="phisingData.csv"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"


"""data ingestion related constant start with DSA_ingestion var name"""

DATA_INGESTON_COLLECTION_NAME:str="NetworkData"
DATA_INGESTON_DATABASE_NAME:str="KanyeWest"
DATA_INGESTON_DIR_NAME:str="data_ingestion"
DATA_INGESTON_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTON_TRAIN_TEST_SPLIT_RATION:float=0.2