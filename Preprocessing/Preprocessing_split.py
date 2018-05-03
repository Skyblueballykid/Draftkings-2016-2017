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
from patsy import dmatrix, dmatrices, demo_data, ContrastMatrix, Poly

from sklearn.externals.six.moves import zip

NBA = pd.read_csv("2016_2017_NBA_Binned.csv", sep = ",")

NBA = NBA.fillna( 'NA' )



# split into input (X) and output (Y) variables
y = NBA.ix[:,'PTS']
X = NBA.ix[:, NBA.columns != 'Binned PTS, Name, Player, Age, Pos, Date, Tm, Opp, GS']


print(X)
print(y)

