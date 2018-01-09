import json

#used to load the JSON file
def load(fileName):
	data = json.load(open(fileName,'r'))
	return data

#retrieves specific game
def extract(data, gameNum):
    game = data["GAME"+str(gameNum)]
    return game

#getGames(end, start, jsonFile) returns a list of nested lists
# ie. a list of a list of a list.
# Each index of the return value of getGames() corresponds to a specific chess game.
# Each game is a list of matrices (list of lists) that cooresponds to sequential moves in the game.
# the jsonFile and the start index and preinitialized, so unless alternate file or start position required,
# leave as is. Only required input is end, which is the number of games requested.
def getGames(end, start = 0, jsonFile = "jsonFiles/jsonTest.json"):
	data = load(jsonFile)
	games = [None]*end
	for i in range(start,end):
		game = extract(data,i)
    	games[i] = game
	return games

result = getGames(2)
