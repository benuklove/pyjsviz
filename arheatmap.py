"""

  Created on 8/12/2016 by Ben

  benuklove@gmail.com
  
  

"""

from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_counties import data as counties

# Prepare the data
counties = {
    code: county for code, county in counties.items() if county["state"] == "ar"
}
county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]
county_names = [county['name'] for county in counties.values()]

source = ColumnDataSource(data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
))

# Output to static HTML file
output_file("arheatmap.html")

# Create the plot by calling 'figure' with some options
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"

p = figure(title="Arkansas Schools", tools=TOOLS,
           x_axis_location=None, y_axis_location=None)

p.grid.grid_line_color = None

p.patches('x', 'y', source=source,
          fill_color='#29a329', fill_alpha=0.7,
          line_color="black", line_width=0.5)

hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("Name", "@name"),
    # ("Unemployment rate)", "@rate%"),
    ("(Long, Lat)", "($x, $y)"),
]

# Ask Bokeh to show results
show(p)
