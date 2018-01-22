import pygal
import csv
from pygal.style import CleanStyle

# Download goog.csv amd amzn.csv
stockPrices = {}    # key is symbol, value is list of closing prices
stockSymbols = ["MSFT", "GOOGL", "INFY"]
for symbol in stockSymbols:
    fileName = "resources/" + symbol + ".csv"
    f = open(fileName, "r")
    reader = csv.reader(f)
    next(reader)
    dates = []
    dataset = []
    # Date, Open, High, Low, Close, Volume
    count = 0
    for x in reader:
        count = count + 1
        if count % 10 == 0:
            dates.append(x[0])
            dataset.append(float(x[4]))
    stockPrices[symbol] = list(reversed(dataset))

# Plot the chart
line_chart = pygal.Line(style=CleanStyle)
line_chart.title = "Stock Prices"
line_chart.x_labels = dates # List of dates (string)
for symbol in stockSymbols:
    line_chart.add(symbol, stockPrices[symbol]) # List of closing prices (float)

# Save the svg to a file
line_chart.render_to_file("resources/stock-charts.svg")
