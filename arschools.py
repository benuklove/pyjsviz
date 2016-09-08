"""

  Created on 8/19/2016 by Ben

  benuklove@gmail.com
  
  Google Maps with Bokeh

"""

import pandas as pd
import numpy as np

from bokeh.io import output_file, show
from bokeh.palettes import RdYlGn10 as palette
from bokeh.models import (
    GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool,
    WheelZoomTool, HoverTool
)

map_options = GMapOptions(lat=34.713, lng=-92.464, map_type="roadmap", zoom=7)

plot = GMapPlot(
    api_key='AIzaSyBQRQEAGrUDyGZvzLGUD4nayxwYHhuL6xw',
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options
)

plot.title.text = "Arkansas Schools' Average ACT Scores"

# Get cleaned data after wrangling
df = pd.read_csv("data/arschools.csv")
lea = df['LEA'].tolist()
avcomp = df['AvgComposite'].tolist()
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
for act in avcomp:
    if act <= 16:
        colors.append(palette[0])
    elif 16 < act <= 17:
        colors.append(palette[1])
    elif 17 < act <= 18:
        colors.append(palette[2])
    elif 18 < act <= 19:
        colors.append(palette[3])
    elif 19 < act <= 20:
        colors.append(palette[4])
    elif 20 < act <= 21:
        colors.append(palette[5])
    elif 21 < act <= 22:
        colors.append(palette[6])
    elif 22 < act <= 24:
        colors.append(palette[7])
    elif 24 < act <= 26:
        colors.append(palette[8])
    elif act > 26:
        colors.append(palette[9])
    else:
        colors.append("#F3F1ED")

# Minimize circle size of schools not taking ACT (primaries, etc)
size = []
for value in avcomp:
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
        act=avcomp,
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
        ("Average Composite ACT", "@act"),
    ]
)

# Render the plot
plot.add_glyph(source, circle)
plot.add_tools(PanTool(), WheelZoomTool(), hover)
output_file("gmap_plot.html")
show(plot)
