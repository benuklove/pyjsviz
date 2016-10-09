"""

  Created on 8/19/2016 by Ben

  benuklove@gmail.com
  
  Google Maps with Bokeh
  Get data from csv file, display Arkansas school class sizes

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

plot.title.text = "Arkansas School Average Class Sizes"

# Get cleaned data after some wrangling
df = pd.read_csv("data/arschools.csv")
lea = df['LEA'].tolist()
class_size = df['AverageClassSize'].tolist()
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
for cs in class_size:
    if cs < 17:
        colors.append(palette[0])
    elif cs == 17:
        colors.append(palette[1])
    elif cs == 18:
        colors.append(palette[2])
    elif cs == 19:
        colors.append(palette[3])
    elif cs == 20:
        colors.append(palette[4])
    elif cs == 21:
        colors.append(palette[5])
    elif cs == 22:
        colors.append(palette[6])
    elif cs == 23:
        colors.append(palette[7])
    elif cs == 24:
        colors.append(palette[8])
    elif cs > 24:
        colors.append(palette[9])
    else:
        colors.append("#F3F1ED")

# Minimize circle size of schools with NaN class sizes
size = []
for value in class_size:
    if np.isnan(value):
        size.append(1)
    else:
        size.append(12)

# Data to be visualized (equal length arrays)
source = ColumnDataSource(
    data=dict(
        lat=latitudes,
        lon=longitudes,
        l=lea,
        class_size=class_size,
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
        ("Ave Class Size", "@class_size"),
    ]
)

# Legend info
factors = ["Less than 17", "17 students", "18 students", "19 students", "20 students",
           "21 students", "22 students", "23 students", "24 students",
           "More than 24"]
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
