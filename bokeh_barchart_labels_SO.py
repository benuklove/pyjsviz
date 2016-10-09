"""

  Created on 9/14/2016 by Ben

  benuklove@gmail.com
  
  Answering a StackOverflow question on adding labels to each bar
  of a bar chart

"""

from bokeh.charts import Bar, output_file, show
from bokeh.sampledata.autompg import autompg as df
from bokeh.layouts import gridplot

from pandas import DataFrame
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import Range1d, HoverTool

# output_file("bar.html")

""" Adding some sample labels a couple different ways.
    It really depends on the type of labels and how you are displaying
    your data.
"""

# One method
labels = []
for number in df['cyl']:
    if number == 3:
        labels.append("three")
    if number == 4:
        labels.append("four")
    if number == 5:
        labels.append("five")
    if number == 6:
        labels.append("six")
    if number == 8:
        labels.append("eight")

df['labels'] = labels


# Another method
def new_labels(x):
    if x % 2 != 0 or x == 6:
        y = "Inline"
    elif x % 2 == 0:
        y = "V"
    else:
        y = "nan"
    return y

df["more_labels"] = df["cyl"].map(new_labels)


# Specifying your labels
p1 = Bar(df, label='labels', values='mpg',
         title="Total MPG by CYL, remapped labels, p1",
         width=400, height=400, legend="top_right")
p2 = Bar(df, label=['cyl', 'more_labels'], values='mpg',
         title="Total MPG by CYL, multiple labels, p2", width=400, height=400,
         legend="top_right")


# Plot with "intermediate-level" bokeh.plotting interface
new_df = DataFrame(df.groupby(['cyl'])['mpg'].sum())
factors = ["three", "four", "five", "six", "eight"]
ordinate = new_df['mpg'].tolist()
mpg = [x * 0.5 for x in ordinate]

p3 = figure(x_range=factors, width=400, height=400,
            title="Total MPG by CYL, using 'rect' instead of 'bar', p3")
p3.rect(factors, y=mpg, width=0.75, height=ordinate)
p3.y_range = Range1d(0, 6000)
p3.xaxis.axis_label = "x axis name"
p3.yaxis.axis_label = "Sum(Mpg)"


# With HoverTool, using 'quad' instead of 'rect'
top = [int(x) for x in ordinate]
bottom = [0] * len(top)
left = []
[left.append(x-0.2) for x in range(1, len(top)+1)]
right = []
[right.append(x+0.2) for x in range(1, len(top)+1)]
cyl = ["three", "four", "five", "six", "eight"]
source = ColumnDataSource(
    data=dict(
        top=[int(x) for x in ordinate],
        bottom=[0] * len(top),
        left=left,
        right=right,
        cyl=["three", "four", "five", "six", "eight"],
    )
)

hover = HoverTool(
    tooltips=[
        ("cyl", "@cyl"),
        ("sum", "@top")
    ]
)

p4 = figure(width=400, height=400,
            title="Total MPG by CYL, with HoverTool and 'quad', p4")
p4.add_tools(hover)
p4.quad(top=[int(x) for x in ordinate], bottom=[0] * len(top),
        left=left, right=right, color="green", source=source)
p4.xaxis.axis_label = "x axis name"

grid = gridplot([[p1, p2], [p3, p4]])
show(grid)
