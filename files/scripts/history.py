import requests
import time
import sys

args = sys.argv
tickerID = args[1]
name = "out/" + args[2] + "/" + args[3]
url_1 = "https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=1000&timestamp="
url_2 = "&tickerId=" + tickerID

initTime = str((int)(time.time() * 1000))


def getJson(timestamp):
    request = requests.get(url_1 + timestamp + url_2, timeout=60)
    jsonstring = str(request.content, 'utf-8')
    return jsonstring

def getNextTimestamp(jsonfile):
    nextTimestamp = jsonfile[38:]
    nextTimestamp = nextTimestamp[:13]
    return nextTimestamp

def cleanJson(jsonfile):
    jsonfile = jsonfile[62:]
    jsonfile = jsonfile.replace("\"", "")
    jsonfile = jsonfile.replace("},{", "\n")
    jsonfile = jsonfile.replace("}],hasNbbo", "\n")
    jsonfile = jsonfile[:jsonfile.rfind('\n')]
    jsonfile = jsonfile.replace("tradeTime:", "")
    jsonfile = jsonfile.replace("tradeStamp:", "")
    jsonfile = jsonfile.replace("price:", "")
    jsonfile = jsonfile.replace("volume:", "")
    jsonfile = jsonfile.replace("trdBs:", "")
    jsonfile = jsonfile.replace("trdEx:", "")
    jsonfile = jsonfile.replace("trdSeq:", "")
    return jsonfile


currentTimeStamp = initTime
f = open(name + ".csv", "w")
jsontext = "Asjdneronuonieinwg0inewr0gijwe0ringf0eing=0n342g58n0843ngue4nbgvouenwsougvno9wung9une9gouneungouewrngoune4o9rugnoulwnfgouwengounerwogunweorug"
while(len(jsontext) > 100):
    #print(currentTimeStamp)
    jsontext = getJson(currentTimeStamp)
    currentTimeStamp = getNextTimestamp(jsontext)
    f.write(cleanJson(jsontext) + "\n")
