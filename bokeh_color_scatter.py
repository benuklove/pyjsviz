"""

  Created on 9/7/2016 by Ben

  benuklove@gmail.com
  
  

"""

import numpy as np

from bokeh.plotting import figure, show, output_file

N = 4000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
]
print(type(colors))
print(len(colors))
# print(colors)
print(type(x))
print(len(x))
TOOLS = "hover,crosshair,pan,wheel_zoom,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select"

p = figure(tools=TOOLS)

p.scatter(x, y, radius=radii,
          fill_color=colors, fill_alpha=0.6,
          line_color=None)

# output_file("color_scatter.html", title="color_scatter.py example")

# show(p)  # open a browser