import pandas as pd

df = pd.read_csv('NBA_2016-2017_Player_Data.csv')
print(df.head())

df.set_index('Date', inplace=True)


df.to_csv('newcsv2.csv')

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


#normalize feature data
for y in list(df):
    df[y] = (df[y] - df[y].min()) / (df[y].max() - df[y].min())
df['BIAS'] = 1
df = df.round(3)


df.to_csv("NN_Normalized_Data_2.csv")
