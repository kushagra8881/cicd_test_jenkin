import pandas as pd
import numpy as np 
from pathlib import Path
import os
import sys
PACKAGE_ROOT = Path(os.path.join(os.path.dirname(__file__))).resolve().parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_module.config import config
from sklearn.pipeline import Pipeline
from prediction_module.processing import preprocessing as pp
from prediction_module.processing.data_handling import load_dataset ,save_pipeline
import prediction_module.pipeliine as pipe
import sys

def perform_traning():
    train_data=load_dataset(file_name=config.TRAIN_FILE)
    train_y=train_data[config.TARGET].map({'Y':1,'N':0})
    pipe.classification_pipeline.fit(train_data[config.FEATURES],train_y)
    save_pipeline(pipeline_to_save=pipe.classification_pipeline)
if __name__ == '__main__':
    perform_traning()