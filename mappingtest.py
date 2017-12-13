"""

  Created on 8/7/2016 by Ben

  benuklove@gmail.com
  
  Take in csv data files from Arkansas School Performance Report Cards,
  http://adesrc.arkansas.gov/lea
  and put them into a single dataframe for wrangling and visualization

"""

from pandas import DataFrame
import pandas as pd
import googlemaps
import time

gmaps = googlemaps.Client(key='YOUR_API_KEY_HERE')

# Read in and merge school info and environment
dfchar = pd.read_csv('data/2015_SchoolCharacteristics.csv')
dfenv = pd.read_csv('data/2015_SchoolEnvironment.csv')
df1 = pd.merge(dfchar, dfenv, how='outer', on='LEA')
del df1['LEADescription_y']

# Read in and merge school choice with dataframe
dfchoice = pd.read_csv('data/2015_SchoolChoice.csv')
df2 = pd.merge(df1, dfchoice, how='outer', on='LEA')
del df2['LEADescription']
del df2['Enrollment']

# Read in and merge specific college entrance info with dataframe
dfcollege = pd.read_csv('data/2015_School_AchievementCollegeEntrance.csv')
collegecolumns = ['LEA', 'NumberOfStudentsTestedInGrades9Thru11',
                  'NumberOfStudentsTestedInGrade12', 'AvgReading',
                  'AvgEnglish', 'AvgMath', 'AvgScience', 'AvgComposite',
                  'NumberOfStudentsTested', 'CriticalReadingMean',
                  'MathMean', 'WritingMean',
                  'NumberOfStudentsTakingAPCourses', 'NumberOfAPExamsTaken',
                  'NumberOfAPExamsScored3OrAbove',
                  'NumberOfStudentsTakingIBCourses', 'OverallCollegeGoingRate']
dfcollege2 = dfcollege[collegecolumns]
df3 = pd.merge(df2, dfcollege2, how='outer', on='LEA')

# Read in and merge specific performance info with dataframe
dfperf = pd.read_csv('data/2015_SchoolPerformance.csv')
perfcols = ['LEA', 'OverallGraduationRate', 'DropoutRate',
            'CollegeRemediationRate', 'Rating', 'OverallPoints']
dfperf2 = dfperf[perfcols]
df4 = pd.merge(df3, dfperf2, how='outer', on='LEA')

# Read in and merge student demographics
dfdemo = pd.read_csv('data/2015_School_StudentDemographics.csv')
df5 = pd.merge(df4, dfdemo, how='outer', on='LEA')
del df5['LEADescription']
del df5['Enrollment']

# Read in and merge graduation rate demographics with dataframe
dfgradrate = pd.read_csv('data/2015_Graduation_Rate_School.csv')
# grcols with dfgradrate2 throw 'view vs copy' warning about chained
# indexing, so I added the .copy() method
grcols = ['School LEA', 'Overall Expected Grad', 'Overall Graduation Rate',
          'Hispanic Overall Grad Rate', 'Native American Overall Grad Rate',
          'Asian Overall Grad Rate', 'African American Overall Grad Rate',
          'Hawaiian/Pacific Islander Overall Grad Rate',
          'Caucasian Overall Grad Rate', 'Two or More Overall Grad Rate',
          'Economic Disadvantage Overall Grad Rate',
          'SPED Overall Grad Rate', 'LEP Overall Grad Rate']
dfgradrate2 = dfgradrate[grcols].copy()
dfgradrate2.rename(columns={'School LEA': 'LEA'}, inplace=True)
df6 = pd.merge(df5, dfgradrate2, how='outer', on='LEA')

# Some cleanup
df6.rename(columns={'LEADescription_x': 'LEADescription'}, inplace=True)
df6['MailingZip'] = df6['MailingZip'].fillna(0.0).astype(int)

# Combine relevant columns to make address strings
dfaddresscols = df6[[0, 5, 6, 7, 8]]
addresses = {}
for index, row in dfaddresscols.iterrows():
    addresses[row[0]] = (str(row[1]) + " " + str(row[2]) + " " +
                         str(row[3]) + " " + str(row[4]))
# frame = DataFrame(addresses)
# print(addresses)
# frame.to_csv('data/addresses.csv', encoding='utf-8')

""" Get latitudes and longitudes from addresses and merge with dataframe """
# Use Google Maps API Python Client for web services to geocode addresses
for lea, address in addresses.items():
    # print(lea, addresses[lea])
    geocode_result = gmaps.geocode(addresses[lea])
    addresses[lea] = ((geocode_result[0]['geometry']['location']['lat']),
                      (geocode_result[0]['geometry']['location']['lng']))
    time.sleep(0.5)

leas = []
addrs = []
for lea, address in addresses.items():
    leas.append(lea)
    addrs.append(address)
addresses = {'LEA': leas, 'latlongs': addrs}
frame = DataFrame(addresses)
# print(frame)

df7 = pd.merge(df6, frame, how='outer', on='LEA')
# print(df7)
df7.to_csv('data/arschools.csv', encoding='utf-8')
