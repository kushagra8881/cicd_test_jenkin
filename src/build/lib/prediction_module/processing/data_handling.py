import os
import pandas as pd
import joblib
from prediction_module.config import config

def load_dataset(file_name):
    file_path = os.path.join(config.DATASET_DIR, file_name)
    _data=pd.read_csv(file_path)
    return _data
def save_pipeline(pipeline_to_save):
    save_path=os.path.join(config.TRAINED_MODEL_DIR,config.MODEL_NAME)
    joblib.dump(pipeline_to_save,save_path)
    print(f"MODEL SAVED at: {save_path} NAME {config.MODEL_NAME}")
def load_pipeline(pipeline_to_load):
    load_path=os.path.join(config.TRAINED_MODEL_DIR,config.MODEL_NAME)
    model_loaded=joblib.load(load_path)
    print("MODEL IS LOADED")
    return model_loaded
