"""

  Created on 9/11/2016 by Ben

  benuklove@gmail.com
  
  StackOverflow example for stacked bar graph grouped by month

"""

import pandas as pd
from pandas import Series
from dateutil.parser import parse
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.charts import Bar, output_file, show
from bokeh.charts.attributes import cat, color
from bokeh.charts.operations import blend

# output_file("datestats.html")


# Sample data
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dates = ["01-01-2015", "02-01-2015", "03-01-2015", "04-01-2015",
         "01-02-2015", "02-02-2015", "03-02-2015", "04-02-2015",
         "01-03-2015", "02-03-2015", "03-03-2015", "04-03-2015"
         ]
# Format data as pandas datetime objects with day-first custom
days = []
days.append(parse(x, dayfirst=True) for x in dates)
# print(days)

# Put data into dataframe broken into min, mean, and max values each for month
ts = Series(vals, index=days[0])
firstmerge = pd.merge(ts.resample('M').min().to_frame(name="min"),
                      ts.resample('M').mean().to_frame(name="mean"),
                      left_index=True, right_index=True)
frame = pd.merge(firstmerge, ts.resample('M').max().to_frame(name="max"),
                 left_index=True, right_index=True)

# You can use DataFrame index for bokeh x values but it doesn't like timestamp
frame['Month'] = frame.index.strftime('%m-%Y')

# Main object to render with stacking
bar = Bar(frame,
          values=blend('min', 'mean', 'max',
                       name='values', labels_name='stats'),
          label=cat(columns='Month', sort=False),
          stack=cat(columns='values', sort=False),
          color=color(columns='values',
                      palette=['SaddleBrown', 'Silver', 'Goldenrod'],
                      sort=True),
          legend=None,
          title="Statistical Values Grouped by Month",
          tooltips=[('Value', '@values')]
          )

# Legend info (if legend attribute is used it gets ugly with large dataset)
factors = ["min", "mean", "max"]
x = [0] * len(factors)
y = factors
pal = ['SaddleBrown', 'Silver', 'Goldenrod']
p = figure(width=100, toolbar_location=None, y_range=factors)
p.rect(x, y, color=pal, width=10, height=1)
p.xaxis.major_label_text_color = None
p.xaxis.major_tick_line_color = None
p.xaxis.minor_tick_line_color = None

# Display chart
show(row(bar, p))
