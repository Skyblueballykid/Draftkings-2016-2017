import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
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

NBA = loadtxt('2016_2017_NBA_Binned_4.csv', delimiter=",")

# split into input (X) and output (Y) variables
# split into input (X) and output (Y) variables
X = NBA[:,0:16:]
y = NBA[:,17]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.75, random_state=0)


# fit model no training data
model = xgboost.XGBRegressor(max_depth=2, learning_rate=0.45, n_estimators=800, silent=True, objective='reg:linear', nthread=-1, gamma=0.008, min_child_weight=1, max_delta_step=1, subsample=1, colsample_bytree=1, colsample_bylevel=1, reg_alpha=0, reg_lambda=1, scale_pos_weight=1, base_score=0.5, seed=0, missing=None)
model.fit(X_train, y_train)

# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

print(predictions)

# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
