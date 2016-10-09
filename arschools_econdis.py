"""

  Created on 8/19/2016 by Ben

  benuklove@gmail.com
  
  Google Maps with Bokeh
  Get data from csv file, display Arkansas school district percent
  economically disadvantaged

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

plot.title.text = "Arkansas Schools - % Economically Disadvantaged" \
                  " (at or below 130% of poverty level)"

# Get cleaned data after some wrangling
df = pd.read_csv("data/arschools.csv")
lea = df['LEA'].tolist()
econdis = df['EconDisadvantaged'].tolist()
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
colors = []
for amount in econdis:
    if amount <= 20:
        colors.append(palette[0])
    elif 20 < amount <= 40:
        colors.append(palette[1])
    elif 40 < amount <= 50:
        colors.append(palette[2])
    elif 50 < amount <= 60:
        colors.append(palette[3])
    elif 60 < amount <= 65:
        colors.append(palette[4])
    elif 65 < amount <= 70:
        colors.append(palette[5])
    elif 70 < amount <= 80:
        colors.append(palette[6])
    elif 80 < amount <= 90:
        colors.append(palette[7])
    elif 90 < amount <= 98:
        colors.append(palette[8])
    elif amount > 98:
        colors.append(palette[9])
    else:
        colors.append("#F3F1ED")

# Minimize circle size of schools with NaN or very low (outlier) spending
size = []
for value in econdis:
    if np.isnan(value):
        size.append(1)
    else:
        size.append(15)

# Data to be visualized (equal length arrays)
source = ColumnDataSource(
    data=dict(
        lat=latitudes,
        lon=longitudes,
        l=lea,
        econdis=econdis,
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
        ("Economically Disadvantaged", "@econdis"),
    ]
)

# Legend info
factors = ["Less than 20%", "20% to 40%", "40% to 50%", "50% to 60%",
           "60% to 65%", "65% to 70%", "70% to 80%", "80% to 90%",
           "90% to 98%", "More than 98%"]
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
