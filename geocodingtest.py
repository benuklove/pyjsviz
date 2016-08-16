"""

  Created on 8/12/2016 by Ben

  benuklove@gmail.com
  
  Testing the geopy 1.11.0 package

"""

import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
location2 = geolocator.geocode('301 N Jackson St DeWitt AR 72042')
# print(location.address)
print(location2.latitude, location2.longitude)

df = pd.read_csv('data/ex1.csv')
df[['c']] = (df[['c']] * 2)
df['c'] = df['c'].astype(int)
dfsmall = df[[0, 1, 4]]
# for row in dfsmall.itertuples(index=False):
#     print(row)
newdict = {}
for index, row in dfsmall.iterrows():
    print(row)
    print(str(row[0]) + " " + str(row[1]))
    newdict[row[2]] = (str(row[0]) + " " + str(row[1]))
print(newdict)
# print(df)
