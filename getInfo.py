import numpy
import json

#used to load the JSON file
def load(fileName):
	data = json.load(open(fileName,'r'))
	return data

#retrieves specific game
def extract(data, gameNum):
    game = data["GAME"+str(gameNum)]
    return game

#changeSize(game) is the resulting game of size 250 states to provide equal length games.
#changeSize : game -> game
def changeSize(game):
	desiredSize = 250
	lastMove = game[-1]
	newGame = [lastMove]*desiredSize
	for index,move in enumerate(game):
		newGame[index] = move
	return newGame

# makeArray: list(list(list(int))) -> array(array(array(int)))
def makeArray(game):
    #matrices are 64x64 numpy arrays
    listMatrices = []
    for move in game:
        #rows are
        listRows = []
        for row in move:
            r = numpy.array(row)
            listRows.append(r)
        matrix = numpy.array(listRows)
        listMatrices.append(matrix)
    final = numpy.array(listMatrices)
    return final

#getGames(end, start, jsonFile) returns a list of nested lists
# ie. a list of an array of matrices (A matrix is an array of an array)
# Each index of the return value of getGames() corresponds to a specific chess game.
# Each game is an array of matrices (array of arrays) that cooresponds to sequential moves in the game.
# The start index is preinitialized, so unless alternate start position required,
# leave as is. Only required input is number of games (end) and jsonFile, which is the number of games requested and the
# jsonFile containing desired games.
def getGames(end, jsonFile, start = 0):
	data = load(jsonFile)
	games = []
	for i in range(start,end):
		game = extract(data,i)
		game = changeSize(game)
		numGame = makeArray(game)
		games.append(numGame)
	return numpy.array(games)

games = getGames(2, '/Users/Mike/Documents/MyCode/jsonFiles/jsonTest.json')
print type(games), type(games[0]),type(games[0][0]), type(games[0][0][0]), type(games[0][0][0][0])
