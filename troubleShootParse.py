from parseWins import parse
import chess

def problemGames():
    #line numbers for problem games in dataset
    whiteProblems = [56,12737,12741,16463,18579,27662,30620,34131,34404,35040,35620,37180,37527,39893,40730,41367,47190,48783,50419,52168,52285,53688,55481,55497,55500,56715,59181,59981,64470,69482,73042,73290]
    blackProblems = [15847, 18714,23150,23914,24667,26401,28388, 28240,29728,35317,37543,37546,37925,40769,41990,42754,43052,43365,48149,48341,52669,53672,58812,60211,60740]
    output = open('ChessProject/textFiles/problemGames.txt', 'w')
    for index,num in enumerate(whiteProblems):
        whiteProblems[index] = num - 1
    for index,num in enumerate(blackProblems):
        blackProblems[index] = num - 1
    with open('rawWinsW.txt', 'r') as inputFileW:
        i = 0
        for line in inputFileW:
            if i in whiteProblems:
                output.write(line)
            i += 1
    with open('rawWinsB.txt', 'r') as inputFileB:
        i = 0
        for line in inputFileB:
            if i in blackProblems:
                output.write(line)
            i += 1
    output.close()
    parsedProblems = parse('problemGames.txt')

    return findError(parsedProblems)

def findSimilar(parsedProblems):
    similar = []
    for primary in parsedProblems:
        temp = parsedProblems
        temp.remove(primary)
        for move in primary:
            for secondary in temp:
                if move in secondary:
                    if move not in similar:
                        similar.append(move)

    for move in similar:
        print move
    return similar


def findError(parsedProblems):
    problems = []
    for game in parsedProblems:
        board = chess.Board()
        for move in game:
            try: board.push_san(move)
            except ValueError:
                problems.append(move)
                break
    problems.sort()
    for prob in problems:
        print prob
    print '\n',len(problems)
    return problems

problemGames()
