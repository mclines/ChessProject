from getInfo import *
import random
from math import sqrt

#length of the standard chess game in the dataset
GAMELENGTH = 250

#findMoves(givenGame) is the list of the optimal start index for the game
#at each state in the game.
#findMoves : list(list(list(int))) -> list(int)
def findMoves(givenGame):
    final = [0 for i in range(0,GAMELENGTH)]
    #iterate through each index of the givenGame
    for n in range(1,GAMELENGTH):
        #individual distance for each game state
        distances = [0 for i in range(0,GAMELENGTH)]
        #reiterate through all indexes up to n
        for i in range(0,n):
            partial = givenGame[i:n+1]
            #predictedGame = CNN(partial)
            predictedGame = CNN(givenGame)
            distance = norm(givenGame, predictedGame,i)
            distances[i] = distance
        best = min(distances)
        final[n] = distances.index(best)
    return final


#Practice CNN method
def CNN(partialGame):
    data = getGames(10,'/Users/Mike/Documents/MyCode/jsonFiles/jsonTest.json')
    #return partialGame
    return data[random.randint(0,9)]

#placeholder norm function
def pnorm(givenGame, predictedGame, moveNum):
    return random.randint(0,100)

#placeholder mostCommon method
def mostCommon(lst):
    return lst[0]

#optimals() is a list of integers, where the value at each index is the optimal
#starting index at each move number.
#optimals : None -> list(int)
def optimals():
    data = getGames(10,'/Users/Mike/Documents/MyCode/jsonFiles/jsonTest.json')
    best = [[] for i in range(0,GAMELENGTH)]
    for game in data:
        moves = findMoves(game)
        for i in range(0,GAMELENGTH):
             best[i].append(moves[i])
    for index, lst in enumerate(best):
        best[index] = mostCommon(lst)
    print best
    return best

#norm(givenGame, predictedGame, moveNum) is the Frobenius norm taken from the
#difference of the two matrix inputs.
#norm: matrix x matrix x moveNum -> R+
def norm(givenGame,predictedGame, moveNum):
    #return len(givenGame[moveNum])
    if moveNum == 248:
        fnorm1 = frobenius(givenGame[moveNum+1], predictedGame[moveNum+1])
        return fnorm1
    elif moveNum < 248:
        fnorm1 = frobenius(givenGame[moveNum+1], predictedGame[moveNum+1])
        fnorm2 = frobenius(givenGame[moveNum+2], predictedGame[moveNum+2])
        return fnorm1 + fnorm2
    else:
        return 0

#frobenius(givenMove, predictedMove) is the resulting frobenius norm of index subtraction
#of given matrices
def frobenius(givenMove, predictedMove):
    result = 0
    for i in range(0,8):
        for j in range(0,8):
            sum = givenMove[i][j] - predictedMove[i][j]
            result += (sum**2)
    print result
    return sqrt(result)

#execute
optimals()
