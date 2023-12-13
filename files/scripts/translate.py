#translate.py
#translate tickerid, ticker, or company into row from list of ids
import csv
filename = "files/documents/tickeridkey.csv"

# convert file to list
def getList():
    with open(filename, 'r') as p:
        my_list = [[x for x in rec] for rec in csv.reader(p, delimiter=',')]
        return my_list

#returns list of column at position
def getCol(list, position):
    col = []
    for row in list:
        col.append(row[position])
    return col


ticker2Dlist = getList()
tickerIDList = getCol(ticker2Dlist, 0)
symbolList = getCol(ticker2Dlist, 1)
"""nameList = getCol(ticker2Dlist, 2)
currencyList = getCol(ticker2Dlist, 3)
exchangeList = getCol(ticker2Dlist, 4)
derivativeSupportList = getCol(ticker2Dlist, 5)
countryCodeList = getCol(ticker2Dlist, 6)"""

#input: tickerID
#returns location of stock
def whereTickerID(tickerID):
    i = 0
    for id in tickerIDList:
        if id == tickerID:
            return i
        i+=1
    return -1

#input: symbol
#returns location of stock
def whereSymbol(symbol):
    i = 0
    for sy in symbolList:
        if sy == symbol:
            return i
        i+=1
    return -1

#input: position
#returns list of information about item at position
def getRow(pos):
    return ticker2Dlist[pos]

