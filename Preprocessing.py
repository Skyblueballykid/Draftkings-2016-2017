import pandas as pd
import numpy as np
from datetime import datetime


NBA = pd.read_csv("/Users/thomaskalnik/Desktop/nba_2016_2017_master.csv", sep = ",")

NBA = pd.DataFrame(NBA, columns = ['Rk', 'Player', 'Age', 'Pos', 'Date', 'Tm', 'Opp', 'GS',	'MP', 'FG',	'FGA', 'FG%', '2P', '2PA', '2P%', '3P', '3PA', '3P%', 'FT',	'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK',	'TOV', 'PF', 'PTS',	'GmSc'])

bins = [0, 10, 20, 30, 40, 50, 60, 70]

group_names = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70']

categories = pd.cut(NBA['PTS'], bins, labels = group_names)
NBA['Binned PTS'] = pd.cut(NBA['PTS'], bins, labels = group_names)

print(NBA['Binned PTS'])

import os
path = r'/Users/thomaskalnik/PycharmProjects'
NBA.to_csv(os.path.join(path,r"2016_2017_NBA_Binned.csv"))
