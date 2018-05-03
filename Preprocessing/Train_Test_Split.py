import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import sklearn.multiclass as mk
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import gradient_boosting

from sklearn.externals.six.moves import zip


NBA = pd.read_csv("2016_2017_NBA_Binned.csv", sep = ";")

X_train, X_test, y_train, y_test = train_test_split(NBA, NBA, test_size=0.75, random_state=0)

print(NBA)

print(y_test.ix[:200])
