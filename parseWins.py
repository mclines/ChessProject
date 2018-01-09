#parse(givenFile) is a list of games where each game is a list of moves
# i.e list of lists
#parse : file -> list of lists
def parse(testFile):
    parsedGames = list()
    with open(testFile,'r') as readFile:
        for game in readFile:
            #removeExtra(game) is a list of moves
            revisedGame = removeExtra(game)
            parsedGames.append(revisedGame)

    # # test output
    # for eachGame in parsedGames:
    #     print eachGame

    return parsedGames

#removeExtra is the list of moves from the given game
#removeExtra: string ->  list
def removeExtra(game):
    endCharacters = [' ', '+' ,'#']
    output = list()
    for index1, char1 in enumerate(game):
        if char1 == '.':
            for index2, char2 in enumerate(game[index1:]):
                if char2 in endCharacters:
                    start, end = index1 + 1, index2 + index1
                    move = game[start:end]
                    output.append(move)
                    break
    return output
