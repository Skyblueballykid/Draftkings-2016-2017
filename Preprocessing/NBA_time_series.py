import numpy as np
import pandas as pd


NBA = pd.read_csv("CleanedData time series sorted not subtotaled.csv", sep = ',', header=0)


NBAdf = pd.DataFrame(data=NBA, index=None, columns=None, dtype=None, copy=False)

NBAdf.sort_values(['PLAYER', 'DATE'], ascending =[False,True])

NBAdf.groupby(['PLAYER']).groups.keys()

print(NBAdf.head(n=1000))


#while(date < 4/13/2016)
