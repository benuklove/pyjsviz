"""

  Created on 8/19/2016 by Ben

  benuklove@gmail.com
  
  Google Maps with Bokeh
  Get data from csv file, display Arkansas school district average spending per pupil

"""

import pandas as pd
import numpy as np

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.palettes import RdYlGn10 as palette
from bokeh.models import (
    GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool,
    WheelZoomTool, HoverTool
)
from apikey import apikey

# output_file("gmap_plot.html")

map_options = GMapOptions(lat=34.713, lng=-92.464, map_type="roadmap", zoom=7)

plot = GMapPlot(
    api_key=apikey,
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options,
)

plot.title.text = "AR District Avg Annual Spending/Pupil" \
                  " (State Avg = $9,641.65, Nat'l Avg = $11,008.94)"

# Get cleaned data after some wrangling
df = pd.read_csv("data/arschools.csv")
lea = df['LEA'].tolist()
spending = df['DistrictAverageSpendingPerPupil'].tolist()
latlngs = df['latlongs'].tolist()

# Convert latlng strings to individual lats & lngs as floats in separate lists
latlonglist = []
for ll in latlngs:
    newlatlong = ll.strip('()').partition(',')
    latlonglist.append(newlatlong)
latitudes = []
longitudes = []
for tupl in latlonglist:
    latitudes.append(float(tupl[0]))
    longitudes.append(float(tupl[2]))

# Color mapping (there must be a better way)
palette.reverse()
colors = []
for amount in spending:
    if amount <= 6000:
        colors.append(palette[0])
    elif 6000 < amount <= 7000:
        colors.append(palette[1])
    elif 7000 < amount <= 8000:
        colors.append(palette[2])
    elif 8000 < amount <= 9000:
        colors.append(palette[3])
    elif 9000 < amount <= 10000:
        colors.append(palette[4])
    elif 10000 < amount <= 11000:
        colors.append(palette[5])
    elif 11000 < amount <= 12000:
        colors.append(palette[6])
    elif 12000 < amount <= 13000:
        colors.append(palette[7])
    elif 13000 < amount <= 14000:
        colors.append(palette[8])
    elif amount > 14000:
        colors.append(palette[9])
    else:
        colors.append("#F3F1ED")

# Minimize circle size of schools with NaN or very low (outlier) spending
size = []
for value in spending:
    if np.isnan(value) or value < 6500:
        size.append(1)
    else:
        size.append(15)

# Data to be visualized (equal length arrays)
source = ColumnDataSource(
    data=dict(
        lat=latitudes,
        lon=longitudes,
        l=lea,
        daspp=spending,
        c=colors,
        s=size,
    )
)

# Circle glyph with relevant properties for plotting
circle = Circle(x="lon", y="lat", size="s", fill_color="c",
                fill_alpha=0.8, line_color=None)

# Information to be displayed when hovering over glyphs
hover = HoverTool(
    tooltips=[
        ("(lat,lng)", "(@lat, @lon)"),
        ("LEA", "@l"),
        ("Spending/Pupil", "@daspp"),
    ]
)

# Legend info
factors = ["Less than $6k", "$6k to $7k", "$7k to $8k", "$8k to $9k",
           "$9k to $10k", "$10k to $11k", "$11k to $12k", "$12k to $13k",
           "$13k to $14k", "More than $14k"]
x = [0] * 10
y = factors

p = figure(width=150, toolbar_location=None, y_range=factors)
p.rect(x, y, color=palette, width=10, height=1)
p.xaxis.major_label_text_color = None
p.xaxis.major_tick_line_color = None
p.xaxis.minor_tick_line_color = None

# Render the plot
plot.add_glyph(source, circle)
plot.add_tools(PanTool(), WheelZoomTool(), hover)

show(row(plot, p))
