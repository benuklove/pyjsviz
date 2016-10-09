"""

  Created on 10/6/2016 by Ben

  benuklove@gmail.com
  
  Generates a pdf of the specified plots from ar_correlations.py

"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from pandas.tools.plotting import scatter_matrix

df = pd.read_csv("data/arschools.csv",
                 usecols=[10, 11, 12, 19, 20, 27, 34, 36, 37, 38, 39, 41, 49, 61])

# Plots of note, put into pdf
with PdfPages('data/multi_page.pdf') as pdf:

    df.plot.scatter(x='AvgComposite', y='CollegeRemediationRate')
    plt.title('Chart One')
    pdf.savefig()
    plt.close()

    df.plot.scatter(x='OverallCollegeGoingRate',
                    y='CollegeRemediationRate')
    plt.title('Chart Two')
    pdf.savefig()
    plt.close()

    p1 = df.plot.scatter(x='DropoutRate', y='CollegeRemediationRate')
    p1.axes.set_xlim([0, 10])
    plt.title("College Remediation Rate vs Dropout Rate for Secondary Schools")
    pdf.savefig()
    plt.close()

    # First 11 categories, scattered, vs each other
    sm = scatter_matrix(df, alpha=0.5, figsize=(15, 15), diagonal='kde')
    # Format for clarity
    # Change label rotation for each axis
    [s.xaxis.label.set_rotation(45) for s in sm.reshape(-1)]
    [s.yaxis.label.set_rotation(0) for s in sm.reshape(-1)]
    # May need to offset label when rotating to prevent overlap of figure
    [s.get_yaxis().set_label_coords(-0.3, 0.5) for s in sm.reshape(-1)]
    # Hide all ticks
    [s.get_yaxis().set_label_coords(-0.3, 0.5) for s in sm.reshape(-1)]
    # y ticklabels
    [plt.setp(item.yaxis.get_majorticklabels(), 'size', 1) for item in sm.ravel()]
    # x ticklabels
    [plt.setp(item.xaxis.get_majorticklabels(), 'size', 1) for item in sm.ravel()]
    # y labels
    [plt.setp(item.yaxis.get_label(), 'size', 5) for item in sm.ravel()]
    # x labels
    [plt.setp(item.xaxis.get_label(), 'size', 5) for item in sm.ravel()]

    pdf.savefig()
    plt.close()
