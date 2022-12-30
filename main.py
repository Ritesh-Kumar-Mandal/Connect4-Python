import numpy as np
import pygame
import sys

## Board design variables
BLUE = (0,0,255)
BLACK = (0,0,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

## To create the playground board
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row


def print_board(board):
    print(np.flip(board), 0)


def winning_move(board, piece):
    
    # Check horizontal locations for win
    for col in range(COLUMN_COUNT-3):
        for row in range(ROW_COUNT):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True
            
    # Check Vertical locations for win
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT-3):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True
    
    # Check positively sloped diaganols
    for col in range(COLUMN_COUNT-3):
        for row in range(ROW_COUNT-3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True
                
    # Check negatively sloped diaganols
    for col in range(COLUMN_COUNT-3):
        for row in range(3, ROW_COUNT):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True

def draw_board(board):
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (col*SQUARE_SIZE,row*SQUARE_SIZE+SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (int(col*SQUARE_SIZE + SQUARE_SIZE/2), int(row*SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE/2)),RADIUS)



# ## ---------------------- Start ----------------------
board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

## Pixel size of unit square on the board
SQUARE_SIZE = 100

width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE

size = (width, height)

## Size of the Circle '5' is an arbitrary value used for spacing
RADIUS = int(SQUARE_SIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:
    
    for event in pygame.event.get():
        
        ## QUIT Event
        if event.type == pygame.QUIT:
            sys.exit()
            
        ## Down event
        if event.type == pygame.MOUSEBUTTONDOWN:
                
#             # Ask the Player 1 Input
#             if turn == 0:
#                 col = int(input("Player 1 Make your selection (0-6): "))

#                 if is_valid_location(board, col):
#                     row = get_next_open_row(board, col)
#                     drop_piece(board, row, col, 1)

#                     if winning_move(board, 1):
#                         print("Player 1 Wins!!! Congrats!!!")
#                         game_over=True

#             # Ask the Player 2 Input
#             else:
#                 col = int(input("Player 2 Make your selection (0-6): "))

#                 if is_valid_location(board, col):
#                     row = get_next_open_row(board, col)
#                     drop_piece(board, row, col, 2)

#                     if winning_move(board, 1):
#                         print("Player 1 Wins!!! Congrats!!!")
#                         game_over=True
            print_board(board)

#             ## Moving to the next turn
#             turn+=1

#             ## To alternate the turn number in just between 0 and 1 (Player1 and player2)
#             turn%=2