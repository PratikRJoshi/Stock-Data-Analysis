import _pickle as cPickle

class Stock: pass

myFile = open("objectPickle.list", "rb")
myPickleList = cPickle.load(myFile)
for x in myPickleList:
    stock = Stock()
    stock = x
    print(stock.date, stock.symbol, stock.close, stock.volume)
