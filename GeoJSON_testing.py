"""

  Created on 8/19/2016 by Ben

  benuklove@gmail.com
  
  Playing with GeoJSON DataSource option in bokeh

"""

from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
from bokeh.sampledata.sample_geojson import geojson

geo_source = GeoJSONDataSource(geojson=geojson)

p = figure()
p.circle(x='x', y='y', alpha=0.9, source=geo_source)
output_file("geojsontest.html")
show(p)
