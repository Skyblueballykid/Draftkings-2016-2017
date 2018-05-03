import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
import sklearn.multiclass as mk
import patsy as pt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import gradient_boosting
from patsy import dmatrix, demo_data, ContrastMatrix, Poly

from sklearn.externals.six.moves import zip

NBA = pd.read_csv("2016_2017_NBA_Binned.csv", sep = ",")

NBA = NBA.fillna( 'NA' )

NBA = NBA.as_matrix(NBA)

# split into input (X) and output (Y) variables
y = NBA.ix[:,'Binned PTS']
X = NBA.ix[:, NBA.columns != 'Binned PTS']

print(X)
print(y)



NBA = NBA.as_matrix(NBA)
contrast = [[1, 2], [3, 3], [5, 6]]

dmatrix("C('Binned PTS', contrast)", NBA)
dmatrices("y ~ X", NBA)
