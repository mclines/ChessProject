import json
from createGames import loadGames

#gathers data in algebraic chess notation and writes it to json file
#JSON : string , string -> dictionary containing lists of lists of lists
def JSON(textFile, jsonFile):
    data = loadGames(textFile)
    with open(jsonFile, 'w') as output:
        jsonDict = dict()
        for index, game in enumerate(data):
            jsonDict["GAME"+str(index)] = game
        json.dump(jsonDict,output, sort_keys=True, separators = (',', ':'))










#test

# for index, move in enumerate(data[0]):
#     print " "
#     print "Move", index + 1
#     for row in move:
#         print row
