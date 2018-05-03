from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
import matplotlib as plt
# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

# load data
dataset = pd.read_csv("CleanedData.csv")

# split into input (X) and output (Y) variables
Y = dataset['DKPTS']
X = dataset.ix[:, dataset.columns != 'DKPTS']

inputsize = len(list(X))

learningrate = [.001, .01, .1]
hidlaysize = [x for x in range(10,45,5)]
batchsize = [10, 20, 30]
epochs = [10, 25, 50]
minloss = 1000

for a, b, c, d in [(a,b,c,d) for a in learningrate for b in hidlaysize for c in batchsize for d in epochs]:
    Network = Sequential()
    Network.add(Dense(b,  input_dim=inputsize, init='uniform', activation='relu', bias=True))
    Network.add(Dense(b,init='uniform', activation='relu'))
    Network.add(Dense(b,init='uniform', activation='tanh'))
    Network.add(Dense(1, init='uniform', activation ='sigmoid'))
    Network.compile(loss='mean_squared_error', optimizer ='sgd', metrics=['accuracy'])
    run = Network.fit(X.values, Y.values, nb_epoch = d, batch_size=c, verbose=0)
    if min((np.sqrt(run.history['loss']))) < minloss:
        best_run = min((np.sqrt(run.history['loss'])))
        best_LR = a
        best_HLS = b
        best_BS = c
        best_ES = d
        runhist = run.history['loss']
        runvalloss = run.history['val_loss']

plt.plot(np.sqrt(runhist))
plt.plot(np.sqrt(runvalloss))
plt.title('Error')
plt.ylabel('FPTs')
plt.xlabel('Epoch')
plt.legend(['Train'], loc='upper left')

print ("Best network has the following parameters:")
print ("Loss Function: " + str(best_run))
print ("Learn Rate: " + str(best_LR))
print ("Hidden Layer Size: " + str(best_HLS))
print ("Batch Size: " + str(best_BS))
print ("Epochs: " + str(best_ES))
plt.show()


