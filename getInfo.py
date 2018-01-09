import json

#used to load the JSON file
def load(fileName):
	data = json.load(open(fileName,'r'))
	return data

#retrieves specific game
def extract(data, gameNum):
    game = data["GAME"+str(gameNum)]
    return game

def getGames(end, start = 0, jsonFile = "jsonFiles/jsonTest.json"):
	data = load(jsonFile)
	games = [None]*end
	for i in range(start,end):
		game = extract(data,i)
    	games[i] = game
	return games

result = getGames(2)
