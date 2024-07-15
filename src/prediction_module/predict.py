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




classifiaction_pipeline=load_pipeline(pipeline_to_load=config.MODEL_NAME)

def generate_predictions(data_input):
    data = pd.DataFrame(data_input)
    pred = classifiaction_pipeline.predict(data[config.FEATURES])
    output = np.where(pred==1,'Y','N')
    result = {"prediction":output}
    return result
if __name__ == '__main__':
    generate_predictions()
