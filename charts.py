import pygal
from pygal.style import DarkGreenStyle
from pygal.style import CleanStyle

data1 = {}
data1[1] = 10
data1[2] = 20
data1[3] = 30
data1[4] = 25
data1[5] = 17

data2 = {1: 40, 2: 33, 3: 20, 4: 15, 5: 11}

# Plot Charts
bar_chart = pygal.Bar(style=DarkGreenStyle)
bar_chart.title = "Bar Chart"
bar_chart.x_labels = [1,2,3,4,5] # X-axis
bar_chart.add("data1", data1)
bar_chart.add("data2", data2)

# Save the generated svg to a file
bar_chart.render_to_file("resources/bar_chart_both.svg")

line_chart = pygal.Line(style=CleanStyle)
line_chart.title = "Line Chart"
line_chart.x_labels = [1,2,3,4,5] # X-axis
line_chart.add("data1", data1)
line_chart.add("data2", data2)

# Save the generated svg to a file
line_chart.render_to_file("resources/line_chart_both.svg")