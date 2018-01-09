import chess
import time
from getInfo import *
from createJSON import JSON

def main():
    textFile, jsonFile = "textFiles/testRaw.txt", "jsonFiles/jsonTest.json"
    print textFile
    JSON(textFile, jsonFile)
    #time0 = time.time()
    data = load(jsonFile)
    #time1 = time.time()
    #print time1 - time0
    for i in range(0,2):
        extract(data,i)
    return None

main()
