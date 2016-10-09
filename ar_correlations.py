"""

  Created on 10/6/2016 by Ben

  benuklove@gmail.com
  
  Generates scatter plots of specified variables

"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
# df = pd.read_csv("data/arschools.csv",
#                  usecols=[10, 11, 12, 19, 20, 27, 34, 36, 37, 38, 39, 41, 61])

df = pd.read_csv("data/arschools.csv",
                 usecols=[10, 11, 12, 19, 20, 27, 34, 36, 37, 38, 39,
                          41, 49, 61], na_values="RV")

x = ["AverageClassSize", "AverageYearsTeachingExperience",
     "DistrictAverageSpendingPerPupil", "SchoolEnrollment",
     "SchoolChoiceTotal", "EconDisadvantaged",
     "Economic Disadvantage Overall Grad Rate"]
y = ["AvgComposite", "NumberOfAPExamsScored3OrAbove",
     "OverallCollegeGoingRate", "OverallPoints",
     "OverallGraduationRate", "DropoutRate",
     "CollegeRemediationRate"]

count = 0
for i in range(0, 7):
    for j in range(0, 7):
        df.plot.scatter(x=x[i], y=y[j])
        s = "data/plots/p"
        count += 1
        fname = s + str(count)
        plt.savefig(fname)
        plt.close()
        print(fname)

s1 = df.plot.scatter(x='DropoutRate', y='CollegeRemediationRate')
s1.axes.set_xlim([0, 10])
plt.savefig('data/plots/p1')

s2 = df.plot.scatter(x='AverageClassSize', y='AvgComposite')
# s2.axes.set_xlim([0, 10])
plt.savefig('data/plots/p2')

s3 = df.plot.scatter(x='AverageClassSize', y='NumberOfAPExamsScored3OrAbove')
plt.savefig('data/plots/p3')

s4 = df.plot.scatter(x='AverageClassSize', y='OverallCollegeGoingRate')
plt.savefig('data/plots/p4')

s5 = df.plot.scatter(x='AverageClassSize', y='CollegeRemediationRate')
plt.savefig('data/plots/p5')

s6 = df.plot.scatter(x='AverageClassSize', y='OverallGraduationRate')
plt.savefig('data/plots/p6')

s99 = df.plot.scatter(x='AverageYearsTeachingExperience', y='AvgComposite')
plt.savefig('data/plots/p99')

# I thought I would see something here, and I don't
s100 = df.plot.scatter(x='OverallCollegeGoingRate', y='CollegeRemediationRate')
# s100.axes.set_xlim([0, 10])
plt.savefig('data/plots/p100')

# scatmat = scatter_matrix(df, alpha=0.5, figsize=(12, 12), diagonal='kde')
# # Format for clarity
# # Change label rotation for each axis
# [s.xaxis.label.set_rotation(45) for s in scatmat.reshape(-1)]
# [s.yaxis.label.set_rotation(0) for s in scatmat.reshape(-1)]
# # May need to offset label when rotating to prevent overlap of figure
# [s.get_yaxis().set_label_coords(-0.3, 0.5) for s in scatmat.reshape(-1)]
# # Hide all ticks
# [s.get_yaxis().set_label_coords(-0.3, 0.5) for s in scatmat.reshape(-1)]
# # y ticklabels
# [plt.setp(item.yaxis.get_majorticklabels(), 'size', 1) for item in scatmat.ravel()]
# # x ticklabels
# [plt.setp(item.xaxis.get_majorticklabels(), 'size', 1) for item in scatmat.ravel()]
# # y labels
# [plt.setp(item.yaxis.get_label(), 'size', 5) for item in scatmat.ravel()]
# # x labels
# [plt.setp(item.xaxis.get_label(), 'size', 5) for item in scatmat.ravel()]
# plt.savefig('data/plots/scatmat.png')
