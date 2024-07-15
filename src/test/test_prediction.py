import pandas as pd
import numpy as np
from pathlib import Path
import os
import sys
import joblib
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))
from prediction_module.config import config
from  prediction_module.processing import preprocessing as pp
from prediction_module.processing.data_handling import load_dataset ,save_pipeline,load_pipeline
from pathlib import Path
import os
import sys




classifiactio_pipeline=load_pipeline(pipeline_to_load=config.MODEL_NAME)
def make_prediction():
    TEST_FILE=os.path.join(config.DATASET_DIR,config.TEST_FILE)
    data=pd.read_csv(TEST_FILE)
    prediction=classifiactio_pipeline.predict(data[config.FEATURES])
    output=np.where(prediction==1,'Y','N')
    result={'prediction':list(output)}
    print(result)
    return result
if __name__ == '__main__':
    make_prediction()
