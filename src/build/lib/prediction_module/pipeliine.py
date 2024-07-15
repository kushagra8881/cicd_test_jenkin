from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from  prediction_module.config import config
from prediction_module.processing import preprocessing as pp
from sklearn.preprocessing import MinMaxScaler
classification_pipeline = Pipeline(
[

  ('Mean Imputation',pp.MeanImputer(variables=config.NUM_FEATURES)),
  ('Mode Imputation',pp.ModeImputer(variables=config.CAT_FEATURES)),
  ('Domain Processing',pp.DomainProcessing(variables_to_modify=config.FEATURES_TO_MODIFY,variables_to_add=config.FEATURES_TO_ADD)),
  ('Drop Columns',pp.DropColums(variables_to_drop=config.DROP_FEATURES)),
  ('Label Encoding',pp.CustomLabelEncoder(variables=config.FEATURES_TO_ENCODE)),
  ('Log Transformation',pp.LogTransformer(variables=config.LOG_FEATURES)),
  ('Min Max Scaler', MinMaxScaler()),
  ('Logistic Regression',LogisticRegression(random_state=0) )
]

)