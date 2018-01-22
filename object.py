import _sqlite3
import _pickle as cPickle

class Stock: pass

# create list of tuples
def getStocks():
    stockList = []
    pathToDB = "/Users/pratik.joshi/Documents/Projects/Python/stocks.db"
    connection = _sqlite3.connect(pathToDB)
    cursor = connection.cursor()
    cursor.execute('SELECT date, close, high, low, open, volume, symbol from stockprices')
    for row in cursor.fetchall():
        stockTuple = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        stock = Stock()
        stock.date = row[0]
        stock.close = row[1]
        stock.high = row[2]
        stock.low = row[3]
        stock.open = row[4]
        stock.volume = row[5]
        stock.symbol = row[6]
        stockList.append(stock)
    return stockList


# get intial list
stockList = []
stockList = getStocks()
print(len(stockList))

# print the object contents
for x in stockList:
    print(x.date, x.close, x.symbol)

# write data to picke file
myFile = open("objectPickle.list", "wb")
cPickle.dump(stockList, myFile, 2)
myFile.close()
