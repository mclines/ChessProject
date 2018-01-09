import chess
import sys
from parseWins import parse

#each game is a list of moves in chess algebraic notation
#loadGames : file -> list of states
def loadGames(textFile):
    rawGames = parse(textFile)
    convertedGames = list()
    for index,rg in enumerate(rawGames):
        cg = list()
        board = chess.Board()
        cg.append(convert(board.fen()))
        for move in rg:
            try: board.push_san(move)
            except ValueError:
                print "CAUGHT ERROR(ValueError): Line", index + 1 , "invalid in", textFile
                cg = []
                break
            else:
                currentState = board.fen()

                #convert(currentState) changes the fen format to integer format
                tempState = convert(currentState)
                cg.append(tempState)
        convertedGames.append(cg)
    # for index, move in enumerate(convertedGames[0]):
    #     print " "
    #     print "Move", index + 1
    #     for row in move:
    #         print row

    return convertedGames

#convert(rawState) is the cooresponding integer representation for the given FEN state
#rawState is a string consisting of the current FEN state
#gameState is an 8x8 matrix
#convert : str -> list of lists
def convert(rawState):
    tempState = ""
    gameState = list()
    for index, char in enumerate(rawState):
        if char == ' ':
            tempState = rawState[:index]
            break
    gameState = tempState.split('/')
    finalState = list()
    for index, fenRow in enumerate(gameState):
        finalState.append(integerRep(fenRow))
    #test
    #for i in reversed(finalState): print i
    return finalState

#integerRep(fenRow) converts a string of a FEN row to the integer representation of that row
#integerRep : string -> list
def integerRep(fenRow):
    intRow = list()
    for char in fenRow:
        if char in conversion: intRow.append(conversion[char])
        else:
            num0 = int(char)
            for i in range(0,num0):
                intRow.append(0)
    return intRow

conversion = {
    'P' : 1,    #white pawn
    'N' : 2,    #white knight
    'R' : 3,    #white rook
    'B' : 4,    #white bishop
    'Q' : 5,    #white queen
    'K' : 6,    #white king
    'p' : 7,    #black pawn
    'n' : 8,    #black knight
    'r' : 9,    #black rook
    'b' : 10,   #black bishop
    'q' : 11,   #black queen
    'k' : 12    #black king
}
