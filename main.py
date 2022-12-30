import numpy as np

## To create the playground board
def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece():
    pass

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row():
    pass


##-------------------------------------------------------------------------------------------
## Start Playing the Game
board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    # Ask the Player 1 Input
    if turn == 0:
        col = input("Player 1 Make your selection (0-6): ")
    # Ask the Player 2 Input
    else:
        col = input("Player 2 Make your selection (0-6): ")
    
    ## Moving to the next turn
    turn+=1
    
    ## To alternate the turn number in just between 0 and 1 (Player1 and player2)
    turn%=2

