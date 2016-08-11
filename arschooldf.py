"""

  Created on 8/10/2016 by Ben

  benuklove@gmail.com
  
  Does not currently work - multiple value arguments for 'how'

"""

import pandas as pd

# Read in school info, environment, choice, college entrance info,
# etc
dfchar = pd.read_csv('data/2015_SchoolCharacteristics.csv')
dfenv = pd.read_csv('data/2015_SchoolEnvironment.csv')
dfchoice = pd.read_csv('data/2015_SchoolChoice.csv')
dfcollege = pd.read_csv('data/2015_School_AchievementCollegeEntrance.csv')

# Merge dataframes
df = pd.merge(dfchar, dfenv, dfchoice, dfcollege, how='outer', on='LEA')

# ADD THIS LATER WITH UPDATED DF#
# df2.rename(columns={'LEADescription_x': 'LEADescription'}, inplace=True)

# Select desired columns
df = df[df.columns[0:18]]
print(df)
