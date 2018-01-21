from urllib.request import urlopen

import json

stocks = ['AAPL', 'GOOG', 'CSCO', 'VGTSX', 'FCNKX', 'AMZN']
apiKey = "4SPQ78YFIZP982D9"
domainURL = "https://www.alphavantage.co/query?function="
quoteType = "TIME_SERIES_MONTHLY_ADJUSTED"
monthlyTimeSeriesField = "Monthly Adjusted Time Series"
fileName = "MonthlyStockQuotes.csv"

with open(fileName, 'w') as file:
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
            file.write(stock + "," + openPrice + "," + closePrice + "," + highPrice + "," + lowPrice + "\n")
file.close()
