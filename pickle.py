import _sqlite3
import _pickle as cPickle

# create list of tuples
def getStocks():
    stockList = []
    pathToDB = "/Users/pratik.joshi/Documents/Projects/Python/stocks.db"
    connection = _sqlite3.connect(pathToDB)
    cursor = connection.cursor()
    cursor.execute('SELECT date, close, high, low, open, volume, symbol from stockprices')
    for row in cursor.fetchall():
        stockTuple = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        stockList.append(stockTuple)
    return stockList


# get intial list
stockList = []
stockList = getStocks()
print(len(stockList))

# write pickle
myfile = open("stockPickle.dat", "wb")
cPickle.dump(stockList, myfile, 2)
myfile.close()