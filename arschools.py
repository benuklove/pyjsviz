"""

  Created on 8/19/2016 by Ben

  benuklove@gmail.com
  
  Google Maps with Bokeh

"""

import pandas as pd
from bokeh.io import output_file, show
from bokeh.models import (
    GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool,
    WheelZoomTool, HoverTool
)

map_options = GMapOptions(lat=34.713, lng=-92.464, map_type="roadmap", zoom=7)

plot = GMapPlot(
    api_key='YOUR API KEY',
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options
)
plot.title.text = "Arkansas Schools"

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

# print(lea)
# print(avcomp)

# source = ColumnDataSource(
#     data=dict(
#         lat=[36.29, 34.20, 35.29],
#         lon=[-94.30, -92.74, -90.78],
#     )
# )

source = ColumnDataSource(
    data=dict(
        lat=latitudes,
        lon=longitudes,
    )
)

circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8,
                line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), HoverTool())
output_file("gmap_plot.html")
show(plot)
