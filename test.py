from getInfo import *

def example():
    games = getGames(3, '/Users/Mike/Documents/MyCode/jsonFiles/jsonTest.json')
    return games

test = example()
#test now is a list of 3 chess games, where each game is a list(list(list(int)))
