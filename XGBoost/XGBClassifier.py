import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import sklearn.multiclass as mk
import patsy as pt
import xgboost as xgboost
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import gradient_boosting
from patsy import dmatrix, dmatrices, demo_data, ContrastMatrix, Poly
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

NBA = loadtxt('2016_2017_NBA_Binned_5.csv', delimiter=",")

# split into input (X) and output (Y) variables
X = NBA[:,0:17]
Y = NBA[:,18]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.75, random_state=0)


# fit model no training data
model = xgboost. XGBClassifier(base_score=0.5, colsample_bylevel=1, colsample_bytree=1,
       gamma=1.005, learning_rate=0.1, max_delta_step=0, max_depth=3,
       min_child_weight=1, missing=None, n_estimators=100, nthread=-1,
       objective='binary:logistic', reg_alpha=0, reg_lambda=1,
       scale_pos_weight=1, seed=0, silent=True, subsample=1)
model.fit(X_train, y_train)

# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
