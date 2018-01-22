from urllib.request import urlopen

import json
import _sqlite3

# 1. Get all the stock data, create tuples out of every data point and finally add it to a list
stocks = ['AAPL', 'GOOG', 'CSCO', 'VGTSX', 'FCNKX', 'AMZN']
apiKey = "4SPQ78YFIZP982D9"
domainURL = "https://www.alphavantage.co/query?function="
quoteType = "TIME_SERIES_MONTHLY_ADJUSTED"
monthlyTimeSeriesField = "Monthly Adjusted Time Series"

myList = []
for stock in stocks:
    url = domainURL + quoteType + "&" + "symbol="+stock+"&apikey="+apiKey
    print("URL Requested: " + url + "\n")
    sourceCode = urlopen(url).read().decode('utf-8')
    jsonData = json.loads(sourceCode)
    stockQuotes = jsonData[monthlyTimeSeriesField]
    for date in stockQuotes:
        openPrice = stockQuotes[date]["1. open"]
        closePrice = stockQuotes[date]["4. close"]
        highPrice = stockQuotes[date]["2. high"]
        lowPrice = stockQuotes[date]["3. low"]
        volume = stockQuotes[date]["6. volume"]
        stockTuple = (date, openPrice, closePrice, highPrice, lowPrice, volume, stock)
        myList.append(stockTuple)


# 2. Add the above list to a database
pathToDB = "/Users/pratik.joshi/Documents/Projects/Python/stocks.db"

connection = _sqlite3.connect(pathToDB)
cursor = connection.cursor()
cursor.executemany('INSERT INTO stockprices VALUES (?,?,?,?,?,?,?)', myList)
connection.commit()
connection.close()

print(cursor.rowcount)
