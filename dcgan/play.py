#!/usr/bin/env python3
#
# Brandon Amos (http://bamos.github.io)
# License: MIT
# 2016-08-05

"""
This file will use the trained dcgan model in order to play a game of chess with the user.
The user will input their move in SAN (Standard Algebraic Notation) and the computer will output it's
move with the cooresponding gameboard until end game is reached, or the user enters 'quit'.
"""
import argparse
import os
import tensorflow as tf
import chess
from model import DCGAN
import operator
import numpy as np
<<<<<<< HEAD
from PIL import Image
=======
>>>>>>> master

MATRIXLENGTH = 16
BOARDLENGTH = 9

parser = argparse.ArgumentParser()
parser.add_argument('--approach', type=str,
                    choices=['adam', 'hmc'],
                    default='adam')
parser.add_argument('--lr', type=float, default=0.001)
parser.add_argument('--beta1', type=float, default=0.9)
parser.add_argument('--beta2', type=float, default=0.999)
parser.add_argument('--eps', type=float, default=1e-8)
parser.add_argument('--hmcBeta', type=float, default=0.2)
parser.add_argument('--hmcEps', type=float, default=0.001)
parser.add_argument('--hmcL', type=int, default=100)
parser.add_argument('--hmcAnneal', type=float, default=1)
parser.add_argument('--nIter', type=int, default=100)
parser.add_argument('--imgSize', type=int, default=128)
parser.add_argument('--lam', type=float, default=0.1)
parser.add_argument('--checkpointDir', type=str, default='checkpoint')
parser.add_argument('--outDir', type=str, default='completions')
parser.add_argument('--outInterval', type=int, default=50)
#parser.add_argument('--maskType', type=str,
                    #choices=['random', 'center', 'left', 'full', 'grid', 'lowres'],
                    #default='center')
parser.add_argument('--centerScale', type=float, default=0.25)
#parser.add_argument('imgs', type=str, nargs='+')

args = parser.parse_args()

assert(os.path.exists(args.checkpointDir))


#FUNCTIONS#
#returns list of legal moves and list of the cooresponding gameboards in fen notation
def get_legals(board):
    #Pick best fit board based on all valid move.
    uci_moves = board.legal_moves
    #list of all legal moves in uci form.
    legal_moves = []
    #list of all legal boards in converted 2d integer form.
    legal_boards = []
    for move in uci_moves:
        #san_move is a string representing the SAN of the current legal move.
        san_move = chess.Move.from_uci(str(move))
        temp_board = board.copy()
        temp_board.push(san_move)
        #add values to list
        legal_moves.append(san_move)
        legal_boards.append(convert(temp_board.fen()))
    return legal_moves, legal_boards

#update_image(image, board, move_num) is the cooresponding game image based on adding the
#given board to the given image based on the move_num
#image is a 2d array of integers, size 128x128
#board is a 2d array of integers, size 8x8
#move_num is an integer
def update_image(image, board, move_num):
    #If the row_num is even, then left to right.
    #right to left if quotient is odd
    row_num = move_num // 16
    if row_num % 2 == 0:
        x1 = (move_num % 16)  * 8
        x2 = x1 + 8
    else:
        x2 = 128 - ((move_num % 16) * 8)
        x1 = x2 - 8
    y1 = row_num*8
    y2 = y1 + 8
    for x in range(x1,x2):
        for y in range(y1,y2):
            image[y][x] = board[y%8][x%8]
    return image

#max_diff(boardA, boardB) is the norm that takes the max magnitude of the resulting
#matrix of the difference between boardA and boardB
#board is an 8x8 matrix of integers
def max_diff(boardA, boardB):
    diffMatrix = [map(operator.sub,boardA[i],boardB[i]) for i in range(len(boardA))]
    max_val = 0
    for row in diffMatrix:
        row_max = max(map(abs,row))
        if row_max > max_val: max_val = row_max
    return max_val


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
                intRow.append(1)
    return intRow

conversion = {
    'P' : 7*20,    #white pawn
    'N' : 8*20,    #white knight
    'R' : 9*20,    #white rook
    'B' : 10*20,    #white bishop
    'Q' : 11*20,    #white queen
    'K' : 12*20,    #white king
    'p' : 6*20,    #black pawn
    'n' : 5*20,    #black knight
    'r' : 4*20,    #black rook
    'b' : 3*20,   #black bishop
    'q' : 2*20,   #black queen
    'k' : 1*20    #black king
}
##########

######RUN######
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
with tf.Session(config=config) as sess:
    dcgan = DCGAN(sess, image_size=args.imgSize,
                  batch_size=1,checkpoint_dir=args.checkpointDir, lam=args.lam)

    #initialize brand new game board
    board = chess.Board()
    #move number
    move_num = 0

    #initialize game image as np array with all zeros(128x128). Will update image with each move
    #np.array with 8bit pixel integers
    game_image = np.array([[0]*128 for i in range(128)]).astype('uint8')
    game_image = update_image(game_image,convert(board.fen()),move_num)

    #initial Board
    print(board)
    #take in initial user move
    user_move = input("Input Move:")

    #PLAY#
    while(user_move != "quit"):
        #combine the current board with the user move, then covert it into 2d array to pass to model
        '''User move'''
        try: board.push_san(user_move)
        except ValueError:
            print("INVALID MOVE")
            user_move = input()
            continue
        else:
            move_num += 1
            #current board is the integer representation of the game board based on given game move
            fen_board = convert(board.fen())
            #update game image with current board (users move)
            game_image = update_image(game_image, fen_board, move_num)
            #user move, board update
            print("Your move:\n")
            print(board)

            '''Computer Move'''
            #update game_image with trained model. play(args, new_gameboard, move_num) returns the game board
            #the model wants to use in integer 2d representation.
            #computer moved
            predicted_board = dcgan.play(args,game_image,move_num + 1)
            legal_moves, legal_boards = get_legals(board)

            #list of all max differences for each cooresponding legal board and the predicted_board
            max_differences = [max_diff(predicted_board,legal_board) for legal_board in legal_boards]
            #get the index of the smallest value in max_differences
            best_difference = min(max_differences)
            best_index = max_differences.index(best_difference)

            #best move and board based on the best index
            best_move = legal_moves[best_index]
            best_board = legal_boards[best_index]
            board.push(best_move)
            game_image = update_image(game_image,best_board,move_num)
            print('\n',board)
            print("Computer Move:",best_move,'\n')
            move_num += 1

            #If checkmate obtained, end
            if board.is_checkmate():
                print("game over")
                break
            #read in new user move
            user_move = input("Input Move: ")
