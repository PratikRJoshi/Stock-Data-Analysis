import _pickle as cPickle

myFile = open("resources/stockPickle.dat", "rb")
myPickleList = cPickle.load(myFile)
for x in myPickleList:
    print(x[0], x[1], x[6])
