import pandas as pd
import numpy as np
from datetime import datetime

# Create empty dataframe
df = pd.read_csv("NBA_2016-2017_Player_Data.csv",low_memory=False)

flds = list(df)

# Loop through rows in dataset and calculate previous weeks statistics, inserting
# them into a series. Then append those statistics to the new NNdat.csv file
for x in data.iterrows():
    active_date = x[1][3]
    active_player = x[1][0]
    active_team = x[1][4]
    active_opp = x[1][6]
    prev = df[(df['DATE'] < active_date) & (active_player == df['PLAYER'])].sort_values('DATE', ascending=False)

    if prev.shape[0] > 4:
        newrow = pd.Series(df = np.empty(len(list(df))), dtype=float, index=flds)
        newrow['HOME'] = x[1]['HOME']
        newrow['AGE'] = x[1]['AGE']
        newrow['VEGAS'] = x[1]['LINE']
        newrow['SPREAD'] = x[1]['O/U']

        #convert position to binary
        if x[1]['POS'] == 'PG':
            newrow['PG'] = 1
            newrow['PF','SF', 'C','SG'] = 0
        elif x[1]['POS'] == 'PF':
            newrow['PF'] = 1
            newrow['PG','SF', 'C','SG'] = 0
        elif x[1]['POS'] == 'SF':
            newrow['SF'] = 1
            newrow['PG','PF', 'C','SG'] = 0
        elif x[1]['POS'] == 'C':
            newrow['C'] = 1
            newrow['PG','PF', 'SF','SG'] = 0
        elif x[1]['POS'] == 'SG':
            newrow['SG'] = 1
            newrow['PG','PF', 'C','SF'] = 0

        # Season Average Statistics
        newrow['SAP'] = np.average(prev['PTS'])                 #points
        newrow['SAR'] = np.average(prev['ORB']+prev['DRB'])     #rebounds
        newrow['SAS'] = np.average(prev['STL'])
        newrow['SAA'] = np.average(prev['AST'])
        newrow['SAB'] = np.average(prev['BLK'])
        newrow['SATOV'] = np.average(prev['TOV'])
        newrow['SATWOP'] = np.average(prev['2P'])
        newrow['SATREP'] = np.average(prev['3P'])
        newrow['SAFT'] = np.average(prev['FT'])
        newrow['SAMP'] = np.average(prev['MP'])
        newrow['SWP'] = float(np.sum(prev['WIN']))/float(prev.shape[0])


        # Last 3 games statistics
        newrow['L3GDKPTS'] = np.average(prev['DKPTS'][0:3].astype(float))
        newrow['L3GP'] = np.average(prev['PTS'][0:3])
        newrow['L3GR'] = np.average(prev['ORB'][0:3]+prev['DRB'][0:3])
        newrow['L3GA'] = np.average(prev['AST'][0:3])
        newrow['L3GTREP'] = np.average(prev['3P'][0:3])
        newrow['L3GTWOP'] = np.average(prev['2P'][0:3])
        newrow['L3GMP'] = np.average(prev['MP'][0:3])

        # Recent game streaks
        newrow['LGW'] = int(prev['WIN'].iloc[0])
        newrow['L2GW'] = int(np.sum(prev['WIN'][0:2]))
        newrow['L3GW'] = int(np.sum(prev['WIN'][0:3]))

        newrow['DKPTS'] = x[1]['DKPTS']

        df = df.append(newrow, ignore_index=True)


#normalize feature data
for y in list(df):
    df[y] = (df[y] - df[y].min()) / (df[y].max() - df[y].min())
df['BIAS'] = 1
df = df.round(3)


df.to_csv("NN_Normalized_Data_2.csv")
