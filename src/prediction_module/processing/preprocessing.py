from sklearn.base import BaseEstimator, TransformerMixin
from pathlib import Path
import pandas as pd
import numpy as np
import os,sys

PaCKAGE_ROOT = Path(os.path.join(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PaCKAGE_ROOT))
from prediction_module.config import config
import numpy as np


class MeanImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None):
        self.imputer_dict_ = {}
        for feature in self.variables:
            self.imputer_dict_[feature] = X[feature].mean()
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna(self.imputer_dict_[feature])
        return X
    

class ModeImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables

    def fit(self, X, y=None):
        self.mode_dict = {}
        for col in self.variables:
            self.mode_dict[col] = X[col].mode()[0]
        return self

    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col] = X[col].fillna(self.mode_dict[col])
        return X


class DropColums(BaseEstimator,TransformerMixin):
    def  __init__(self,variables_to_drop=None):
     self.variables_to_drop = variables_to_drop
    def fit(self,X,y=None):
        return self
    def transform(self,X):
       X=X.copy()
       X=X.drop(self.variables_to_drop,axis=1)
       return X

class DomainProcessing(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_modify=None, variables_to_add=None):
        self.variables_to_modify = variables_to_modify
        self.variables_to_add = variables_to_add
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        for feature in self.variables_to_modify:
            if all(var in X.columns for var in self.variables_to_add):
                # Ensure all specified columns are present in the DataFrame
                added_columns = X[self.variables_to_add].sum(axis=1)
                if len(X[feature]) == len(added_columns):
                    X[feature] = X[feature] + added_columns
                else:
                    raise ValueError(f"Length of columns to add does not match the length of the feature column {feature}")
            else:
                raise ValueError("One or more columns specified in variables_to_add are not present in the DataFrame")
        return X


class CustomLabelEncoder(BaseEstimator,TransformerMixin):
    def __init__(self, variables=None):
        self.variables=variables
    
    def fit(self, X,y):
        self.label_dict = {}
        for var in self.variables:
            t = X[var].value_counts().sort_values(ascending=True).index 
            self.label_dict[var] = {k:i for i,k in enumerate(t,0)}
        return self
    
    def transform(self,X):
        X=X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.label_dict[feature])
        return X
    

class LogTransformer(BaseEstimator,TransformerMixin):
    def  __init__(self,variables=None):
     self.variables = variables
    def fit(self,X,y=None):
        return self
    def transform(self,X):
       X=X.copy()
       for feature in self.variables:
           X[feature]=np.log(X[feature])
       return X