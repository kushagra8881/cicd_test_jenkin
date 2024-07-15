import pathlib
import os
import prediction_module
PACKAGE_ROOT=pathlib.Path(prediction_module.__file__).resolve().parent
TRAINED_MODEL_DIR = os.path.join(PACKAGE_ROOT, "trainedmodels")

DATASET_DIR = os.path.join(PACKAGE_ROOT, "datasets")
TRAIN_FILE="train.csv"
TEST_FILE="test.csv"
TARGET='Loan_Status'
MODEL_NAME='ClassificationModel'
# Features Final
FEATURES=[ 'Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']
NUM_FEATURES = ['ApplicantIncome', 'LoanAmount',
       'Loan_Amount_Term']
CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
           'Credit_History', 'Property_Area']
FEATURES_TO_ENCODE=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
           'Credit_History', 'Property_Area']
FEATURES_TO_MODIFY=['ApplicantIncome']
FEATURES_TO_ADD=['CoapplicantIncome']
DROP_FEATURES=['CoapplicantIncome'] 
LOG_FEATURES=['ApplicantIncome','LoanAmount']
