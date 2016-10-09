"""

  Created on 8/19/2016 by Ben

  benuklove@gmail.com
  
  Google Maps with Bokeh
  Get data from csv file, display Arkansas school ratings
  Rating determination info at:
  http://www.arkansased.gov/public/userfiles/Public_School_Accountability/School_Performance/Parent_Handout_4_4_2016.pdf

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

plot.title.text = "Arkansas School Ratings"

# Get cleaned data after some wrangling
df = pd.read_csv("data/arschools.csv")
lea = df['LEA'].tolist()
rating = df['OverallPoints'].tolist()
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
for rate in rating:
    if rate <= 180:
        colors.append(palette[0])
    elif 180 < rate <= 208:
        colors.append(palette[1])
    elif 208 < rate <= 214:
        colors.append(palette[2])
    elif 214 < rate <= 220:
        colors.append(palette[3])
    elif 220 < rate <= 226:
        colors.append(palette[4])
    elif 226 < rate <= 232:
        colors.append(palette[5])
    elif 232 < rate <= 238:
        colors.append(palette[6])
    elif 238 < rate <= 244:
        colors.append(palette[7])
    elif 244 < rate <= 269:
        colors.append(palette[8])
    elif rate > 269:
        colors.append(palette[9])
    else:
        colors.append("#F3F1ED")

# Minimize circle size of schools without ratings
size = []
for value in rating:
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
        rating=rating,
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
        ("School Rating", "@rating"),
    ]
)

# Legend info
factors = ["Points <= 180  (F)", "180 < Points <= 208  (D)",
           "208 < Points <= 214  (C)",
           "214 < Points <= 220  (C)",
           "220 < Points <= 226  (C)",
           "226 < Points <= 232  (C)",
           "232 < Points <= 238  (C)",
           "238 < Points <= 244  (C)",
           "244 < Points <= 269 (B)",
           "Points > 269 (A)"]
x = [0] * 10
y = factors

p = figure(width=200, toolbar_location=None, y_range=factors)
p.rect(x, y, color=palette, width=10, height=1)
p.xaxis.major_label_text_color = None
p.xaxis.major_tick_line_color = None
p.xaxis.minor_tick_line_color = None

# Render the plot
plot.add_glyph(source, circle)
plot.add_tools(PanTool(), WheelZoomTool(), hover)

show(row(plot, p))
