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
# The start index is preinitialized, so unless alternate start position required,
# leave as is. Only required input is number of games (end) and jsonFile, which is the number of games requested and the
# jsonFile containing desired games.
def getGames(end, jsonFile, start = 0):
	data = load(jsonFile)
	games = []
	for i in range(start,end):
		game = extract(data,i)
		#print( len(games) )
		games.append(game)
	return games

#test = getGames(4,'/Users/Mike/Documents/MyCode/jsonFiles/jsonTest.json')
#print len(test)
