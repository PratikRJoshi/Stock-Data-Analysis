import csv
from dateutil.parser import parse

# Goal: calculate value of holdings over time
# Goal: calculate and sort daily diff of holdings over time
# https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=MSFT

shares = {"MSFT": 10, "F": 1000}
marketDates = []
myDict = {}  # key is tuple(symbol, date) value is tuple (open, close)

for stocks in shares.keys():
    stockSymbol = stocks
    fileName = "resources/" + stockSymbol + ".csv"
    f = open(fileName, "r")
    reader = csv.reader(f)
    next(reader, None) # skip Headers
    # Date, Open, High, Low, Close, Volume
    for data in reader:
        if(parse(data[0])) not in marketDates:
            marketDates.append(parse(data[0]))
        myDict[(stockSymbol, parse(data[0]))] = (float(data[1]), float(data[4]))

total = {}
for date in sorted(marketDates):
    for stock in shares.keys():
        if date in total:
            total[date] = total[date] + myDict[(stock, date)][1] * shares[stock]
        else:
            total[date] = myDict[(stock, date)][1] * shares[stock]

for date in sorted(marketDates):
    print(date, total[date])
