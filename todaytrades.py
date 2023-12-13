#import history
import files.scripts.translate as translate
import os
from datetime import datetime


todaysDate = datetime.today().strftime('%Y-%m-%d')


currentDir = "files/current/"
top100path = "files/documents/top100usa05.09.23.txt"
scriptsDir = "files/scripts/"


f = open(top100path, 'r')
s = f.read()
f.close()
top100list = s.split('\n')


if not os.path.exists(currentDir):
    os.makedirs(currentDir)

def writeCurrentTicker(ticker):
    print(ticker)
    f = open(currentDir + todaysDate, 'w')
    f.write(ticker)
    f.close()

def readCurrentTicker():
    f = open(currentDir + todaysDate, 'r')
    return f.read()

if os.path.exists(currentDir + todaysDate):
    currentTicker = readCurrentTicker()
    for ticker in top100list:
        if ticker == currentTicker:
            break
        top100list.remove(ticker)


for ticker in top100list:
    writeCurrentTicker(ticker)
    if not os.path.exists("out/" + ticker + "/"):
        os.makedirs("out/" + ticker + "/")
    os.system("python3 " + scriptsDir + "history.py " + translate.getRow(translate.whereSymbol(ticker))[0] + " " + ticker + " " + todaysDate)

