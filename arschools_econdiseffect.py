"""

  Created on 8/19/2016 by Ben

  benuklove@gmail.com
  
  Google Maps with Bokeh
  Get data from csv file, display difference in Arkansas school district
  percent economically disadvantaged graduation rate and overall
  graduation rate

"""

import pandas as pd

from bokeh.io import output_file, show
from bokeh.charts import Bar
from bokeh.plotting import figure
from bokeh.layouts import gridplot
from bokeh.palettes import RdYlGn11 as palette
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

plot.title.text = "Effect of Poverty on Graduation Rate " \
                  "- Where the Disadvantaged Fare Worse"

# Get cleaned data after some wrangling
df = pd.read_csv("data/arschools.csv")
leas = df['LEA'].tolist()
latslngs = df['latlongs'].tolist()
econdis_gradrate = df['Economic Disadvantage Overall Grad Rate']\
    .fillna(0).replace('RV', 0).tolist()
overall_gradrate = df['OverallGraduationRate']\
    .fillna(0).replace('RV', 0).tolist()

# Cast strings to floats
index = 0
while index < len(overall_gradrate):
    overall_gradrate[index] = float(overall_gradrate[index])
    econdis_gradrate[index] = float(econdis_gradrate[index])
    index += 1

# Get difference between graduation rates (econ disadvantaged vs non-)
# Also select associated lea and latlng for each
gradrate_diff = []
lea = []
latlngs = []
i = 0
for item in econdis_gradrate:
    diff = round((item - overall_gradrate[i]), 2)
    if diff > -50 and diff != 0.0:
        gradrate_diff.append(diff)
        lea.append(leas[i])
        latlngs.append(latslngs[i])
    i += 1

# Create bar chart to display these differences
bardata = {
    "lea": lea,
    "difference, %": gradrate_diff
}
bar = Bar(bardata, values="difference, %",
          title="Percent Difference in Graduation Rate for"
                " Economically Disadvantaged Compared to Economically"
                " Stable (E.D. = below 130% poverty level)",
          legend=None, plot_width=1100, xlabel="Arkansas Secondary Schools",
          xscale=None)

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
for amount in gradrate_diff:
    if amount <= -8:
        colors.append(palette[0])
    elif -8 < amount <= -6:
        colors.append(palette[1])
    elif -6 < amount <= -4:
        colors.append(palette[2])
    elif -4 < amount <= -2:
        colors.append(palette[3])
    elif -2 < amount <= -1:
        colors.append(palette[4])
    elif -1 < amount <= 0:
        colors.append(palette[5])
    elif 0 < amount <= 2.5:
        colors.append(palette[7])
    elif amount > 2.5:
        colors.append(palette[10])
    else:
        colors.append("#F3F1ED")

# Data to be visualized (equal length arrays)
source = ColumnDataSource(
    data=dict(
        lat=latitudes,
        lon=longitudes,
        l=lea,
        diff=gradrate_diff,
        c=colors,
    )
)

# Circle glyph with relevant properties for plotting
circle = Circle(x="lon", y="lat", size=15, fill_color="c",
                fill_alpha=0.8, line_color=None)

# Information to be displayed when hovering over glyphs
hover = HoverTool(
    tooltips=[
        ("(lat,lng)", "(@lat, @lon)"),
        ("LEA", "@l"),
        ("Difference in Grad Rate, %", "@diff"),
    ]
)

# External legend info
factors = ["More than 8% lower", "6% to 8% lower", "4% to 6% lower",
           "2% to 4% lower", "1% to 2% lower", "0 to 1% lower",
           "0% to 2.5% higher", "More than 2.5% higher"]
x = [0] * 10
y = factors
rect_colors = palette[0:6]
rect_colors.append(palette[7])
rect_colors.append(palette[10])

# Instantiate the figure for the legend
p = figure(width=150, toolbar_location=None, y_range=factors)
p.rect(x, y, color=rect_colors, width=10, height=1)
p.xaxis.major_label_text_color = None
p.xaxis.major_tick_line_color = None
p.xaxis.minor_tick_line_color = None

# Render the plot
plot.add_glyph(source, circle)
plot.add_tools(PanTool(), WheelZoomTool(), hover)

grid = gridplot([[bar], [plot, p]])
show(grid)
