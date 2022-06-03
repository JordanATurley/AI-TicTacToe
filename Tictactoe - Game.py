# -*- coding: utf-8 -*-
"""
To Do:
The game itself:
- function that is play game.
- create better visualisations
- create better interactions

AI interaction:
- need to keep track of all moves and outputs
- need function that accesses a random move
- need "Bins" for every possible move
- function taht acts on bins when a game finishes

Publishing the game
- Imbed onto website
- store the Bins
- Visualisations

HTML for the website - CSS for style.
Javascript for the game (Or convert from python...I think)
Needs to get the move from somewhere -

Host the data somewhere (A database?, its small so can I use like...sharepoint or something?)
Python to receive the input from the website, read the move, access the data, calculate next move, send it back.

Is there an intermediate that needs to access the python code?
How do I host my python code?

MySQL

HTML
Bootstrap - library does the nice stuff for html
HTTP requests - done in Javascript or HTML form
Python anywhere or Heroku

"""

#%% imports
import numpy as np
import re

#%% Board setup
#define the board. Ill do it as a 3x3 array. Set to empty. 0 is empty, 1 is X and 0 and O.
#Also using the notation 1-9, from top to bottom, left to right.
def setup_board():
    board = np.array([[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']])
    return board

#%% Setup player start
#Start this as X, later make it random.
def setup_player():
    player = 'X'
    return player

#%% Display Board
#Start this off as just a print. Later develop it into an interactive popup, and then imbed into web.
#relace with characters.
def display_board(board):
    print(board[0,0],'|',board[0,1],'|',board[0,2])
    print('----------')
    print(board[1,0],'|',board[1,1],'|',board[1,2])
    print('----------')
    print(board[2,0],'|',board[2,1],'|',board[2,2])
    return

#%% Receive Input
#Currently just do this as a number input, then convert to interactive popup.
def receive_move():
    repeat = True
    move = input('Enter a move (1 - 9):\n')
    return move

#%%Need a function that converts the move into a coordinate
def get_coord(move):
    row = int((int(move)-1)/3)
    col = int((int(move)-1)%3)
    return [row,col]

#%%Check if the move is valid
def valid_check(board, move):
    valid = True
    #check if valid move
    if not re.match('\d',move):
        print('Please select a valid move')
        valid = False
    #Check if its not already used
    coords = get_coord(move)
    if board[coords[0],coords[1]]!=' ':
        print('Please select a valid move')
        valid = False
    return valid

#%% Create function that turn
def switch_turn(player):
    if player == 'O':
        player = 'X'
    else:
        player = 'O'
    return player

#%% Make Move
def make_move(board, move, player):
    #Switch to coordates
    coords = get_coord(move)
    #Set that coord to the current player
    board[coords[0],coords[1]] = player
    return board
        

#%% Check Win
def win_check(board):
    win = False
    #row
    for row in range(0,3):
        if board[row,0] == board[row,1] == board[row,2] != ' ':
            win = True
    #col
    for col in range(0,3):
        if board[0,col] == board[1,col] == board[2,col] != ' ':
            win = True
    #diagonals
    if board[0,0] == board[1,1] == board[2,2] != ' ':
        win = True
    if board[0,2] == board[1,1] == board[2,0] != ' ':
        win = True
    return win


#%% MAIN
board = setup_board()
player = setup_player()
game_active = True
while game_active:
    #Print the board
    display_board(board)
    
    #Repeat until a valid move is made
    valid = False
    while not valid:
        #Request move
        move = receive_move()
        #Check if move is valid
        valid = valid_check(board, move)
        
    #Make the move
    board = make_move(board, move, player)
    
    #Check if game has ended
    win = win_check(board)

    if win:
        game_active = False
        print('Winner is: ',player)
    else:
        #Switch players turn
        player = switch_turn(player)
    





















