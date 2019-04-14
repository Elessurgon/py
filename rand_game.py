import sys
import os
import random
#too many global variables
#comp is made only for the ai

comp=['00','01','02',
     '10','11','12',
     '20','21','22']



board={"00":' ',"01":" ","02":" ",
       "10":' ',"11":" ","12":" ",
       "20":' ',"21":" ","22":" "}

winning_condt = [['00','01','02'],
                 ['10','11','12'],
                 ['20','21','22'],
                 ['00','10','20'],
                 ['01','11','21'],
                 ['02','12','22'],
                 ['00','11','22'],
                 ['02','11','20']]
choices_of_X=[]
choices_of_OT=[]

def print_board(board):
    os.system('cls')
    print(board["00"]+"|"+board["01"]+"|"+board["02"])
    print("-+-+-")
    print(board["10"]+"|"+board["11"]+"|"+board["12"])
    print("-+-+-")
    print(board["20"]+"|"+board["21"]+"|"+board["22"])

def put_in_board(position,board,turn,choices_of_X,choices_of_OT):
#checks for X's,O's choices are already there and checks whether it is something other than the board positions
    if position in choices_of_X or position not in board.keys() or position in choices_of_OT: 
        print("Already filled")
        if turn=='X':
            position=input()
        else:
            position=ai_turn(turn)
        put_in_board(position,board,turn,choices_of_X,choices_of_OT)
    elif turn=="X":
        choices_of_X.append(position)
        board[position] = turn
        comp.remove(position)
    elif turn == "O":
        choices_of_OT.append(position)
        board[position] = turn
        comp.remove(position)
        
    
def check_win(board):
    for row in winning_condt:
        if set(row) <= set(choices_of_X):
            print("X won")
            k=input()
            sys.exit()
    for row in winning_condt:
        if set(row) <= set(choices_of_OT):
            print("O won")
            k=input()
            sys.exit()
            
def ai_turn(turn):
    if turn=='O':
        crap=random.choice(list(comp))
        pos=crap
        return pos
    
#this is where it starts

turn='X'
print_board(board)

for i in range(9):
    if turn=='X':
        position=input()
    else:
        position=ai_turn(turn)
    put_in_board(position,board,turn,choices_of_X,choices_of_OT)
    if turn=="X":
        turn="O"
    else:
        turn="X"
    print_board(board)
    check_win(board)
    
print("The game is a tie")
k=input()
