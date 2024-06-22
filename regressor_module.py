# This modukle provides a regressor

# some basic packages / modules
import pandas as pd

# estimator libraries
from sklearn.svm import SVR

# library for estimator base class
from sklearn.base import BaseEstimator,TransformerMixin


# this regressor does not take the given values directly but it substracts or adds an offset to account for the relative course evaluation
class special_regressor(BaseEstimator,TransformerMixin):
    def __init__(self, estimator=SVR()): 
        """constructor function"""
        
        self.set_params(estimator) 
        return None

    def set_params(self, estimator=SVR()):
        """parameters are set"""
        self.estimator = estimator

        return self

    def score(self, X, y):
        """scoring function"""
        print("score")
        return self.estimator.score(X, y)

    def transform(self, X):
        """transform function"""
        self.offset=X.mean(axis=1)
        columns=X.columns
        X2=pd.DataFrame(pd.concat([X.iloc[:,i].sub(self.offset.values) for i in range(len(columns))],axis=1).values,columns=columns)

        return X2

    def fit(self, X, y=None):
        """fit procedure covering all classifiers for each target"""

        X2=self.transform(X)
        y2=y-(self.offset.values)
        self.estimator.fit(X2, y2)# ,sample_weight=np.array([(float(i)/len(y2))**5 for i in range(len(y2))]))# , sample_weight=np.array([float(i)/len(y2)**0.25+3.3*((len(y2)-i)%5==0) for i in range(len(y2))]))
        return self

    def predict(self, X):
        """predict-funtion for the only one target value"""
        X2=self.transform(X)
        y_pred = self.estimator.predict(X2) + self.offset.values
        return y_pred


