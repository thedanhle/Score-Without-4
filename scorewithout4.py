import numpy as np #importing numpy library
import pygame
import sys
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (157, 74, 208)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

ROW_COUNT = 12
COLUMN_COUNT = 14

def create_board(): #function for creating board
    board = np.zeros((ROW_COUNT,COLUMN_COUNT)) #variable board to create numpy matrix of 6 x 7
    return board #return value of board

def drop_piece(board, row, col, piece): 
    board[row][col] = piece

def is_valid_location(board, col): #check number inputted to see if it is a valid location + also take column and current board
    return board[ROW_COUNT - 1][col] == 0 #check for empty slot on very top row

def get_next_open_row(board, col): #check for next available row
    for r in range(ROW_COUNT): #count from 0 to ROW_COUNT
        if board[r][col] == 0: #if open row is found
            return r #return value

def print_board(board): #print board correctly due to numpy interpretation, storing from the top
    reverse_board = board[::-1] #reverse board
    print(reverse_board) #print board that is reversed


def winning_move2(board, row, col, piece):
    # check horizontals "col" for win
    
    print(row, col)
#horizontal
    if COLUMN_COUNT-1 >= col+1 and col > 0:
        if board[row][col+1] == piece and board[row][col-1] == piece:
            return True

    if COLUMN_COUNT-1 >= col+2:
        if board[row][col+1] == piece and board[row][col+2] == piece:
            return True
    
    if col > 2:
        if board[row][col-2] == piece and board[row][col-1] == piece:
            return True

#vertical 
    if ROW_COUNT-1 > row and row >= 2:
        if board[row-2][col] == piece and board[row-1][col] == piece:
            return True

#Positive Diagonal
#check upwards
    if row <= ROW_COUNT-3 and COLUMN_COUNT-3 >= col:
        if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece:
            return True

#check downwards
    if row >= ROW_COUNT-10 and col >= COLUMN_COUNT-12:
        if board[row][col] == piece and board[row-1][col-1] == piece and board[row-2][col-2] == piece:
            return True

#check middle
    if row >= 1 and row <= 10 and col >= 1 and col <=12:
        if board[row][col] == piece and board[row+1][col+1] == piece and board[row-1][col-1] == piece:
            return True

#Negative Diagonal
#check upwards
    if row <= 9  and col >= 2:
        if board[row][col] == piece and board[row+1][col-1] == piece and board[row+2][col-2] == piece:
            return True

#check downwards
    if row >= 2 and col <= 11:
        if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece:
            return True

#check middle        
    if row >= 1 and row <= 10 and col >= 1 and col <= 11:
        if board[row][col] == piece and board[row+1][col-1] == piece and board[row-1][col+1] == piece:
            return True


def draw_board(board): #pygame graphics
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE)) #SIZE OF WIDTH AND HEIGHT AND POSITION, adding squaresize for top block
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), RADIUS) #draw circle w/ offset to fit

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS) #draw circle w/ offset to fit
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS) #draw circle w/ offset to fit
            elif board[r][c] == 3:
                pygame.draw.circle(screen, PURPLE, (int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS) #draw circle w/ offset to fit
            elif board[r][c] == 4:
                pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS) #draw circle w/ offset to fit
    pygame.display.update()


board = create_board() #make board to put pieces into)
print_board(board) #print board

game_over = False #turns true if someone gets 4 in a row
turn = 0 #changes when players alternate

pygame.init()
SQUARESIZE = 50 #size of each square
width = COLUMN_COUNT *SQUARESIZE #width for screen
height = (ROW_COUNT+1) * SQUARESIZE #height for screen and +1 to row for aesthetic
size = (width, height) #package in both width and height
RADIUS = int(SQUARESIZE/2 - 5) #radius as an int and has to be smaller than square size so they dont overlap or touch
screen = pygame.display.set_mode(size) #let pygame read and display screen

draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 30)
font2 = pygame.font.SysFont("monospace", 40)

total_clicks = 0
invalid_click = 0
player1 = 0
player2 = 0
player3 = 0
player4 = 0

pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE)) #update last circle to black
label = font2.render("WELCOME TO SCORE WITHOUT 4!", 1, WHITE)
screen.blit(label, (40, 10)) #update screen
pygame.time.wait(750)

while not game_over: #while loop continues while the game_over variable is false

    temp = 0
    temp2 = 0

    for event in pygame.event.get(): #take user input
        if event.type == pygame.QUIT: #proper exit
            sys.exit() #exit

        if event.type == pygame.MOUSEMOTION: #move mouse
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE)) #update last circle to black
            screen.blit(label, (40, 10)) #update screen

            posx = event.pos[0]
            if turn == 0: 
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS) #draw red circle
            elif turn == 1:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)  #draw yellow circle
            elif turn == 2:
                pygame.draw.circle(screen, PURPLE, (posx, int(SQUARESIZE/2)), RADIUS)  #draw yellow circle
            else:
                pygame.draw.circle(screen, GREEN, (posx, int(SQUARESIZE/2)), RADIUS)  #draw yellow circle
                temp = 2
        pygame.display.update() #uodate every loop

        if event.type == pygame.MOUSEBUTTONDOWN: #clicking down
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE)) #update last circle to black

    #Ask player 1 Input
            if turn == 0: #if turn = 0
                posx = event.pos[0] #0th position is position of x ex. (0, 10)
                col = int(math.floor(posx/SQUARESIZE)) #round down as int

                if is_valid_location(board, col): #check if input is valid location
                    row = get_next_open_row(board, col) #find next available row
                    drop_piece(board, row, col, 1) #drop piece in next available spot

                    if winning_move2(board, row, col, 1): #check if won
                        player1 += 1
                        label = myfont.render("       Player 1 Scores!!!", 1, RED) #1 is the axis?
                        screen.blit(label, (40, 10)) #update screen

                else: #if invalid, prompt user
                    label = myfont.render("            Invalid!!!", 1, RED) #1 is the axis?
                    screen.blit(label, (40, 10)) #update screen
                    temp = 1
                    invalid_click += 1

    #Ask player 2 Input
            elif turn == 1:
                posx = event.pos[0] #0th position is position of x ex. (0,10)
                col = int(math.floor(posx/SQUARESIZE)) #round down int for column
                if is_valid_location(board, col): #check if input is a valid location
                    row = get_next_open_row(board, col) #find next available row
                    drop_piece(board, row, col, 2) #drop piece in next available spot

                    if winning_move2(board, row, col, 2): #check if won
                        player2 += 1
                        label = myfont.render("       Player 2 Scores!!!", 1, YELLOW) #1 is the axis?
                        screen.blit(label, (40, 10)) #update screen
                        print("Score ",turn)

                else: #if invalid, prompt user
                    label = myfont.render("            Invalid!!!", 1, YELLOW) #1 is the axis?
                    screen.blit(label, (40, 10)) #update screen
                    temp = 1
                    invalid_click += 1

    #Ask player 3 Input
            elif turn == 2:
                posx = event.pos[0] #0th position is position of x ex. (0,10)
                col = int(math.floor(posx/SQUARESIZE)) #round down int for column
                if is_valid_location(board, col): #check if input is a valid location
                    row = get_next_open_row(board, col) #find next available row
                    drop_piece(board, row, col, 3) #drop piece in next available spot

                    if winning_move2(board, row, col, 3): #check if won
                        player3 += 1
                        label = myfont.render("       Player 3 Scores!!!", 1, PURPLE) #1 is the axis?
                        screen.blit(label, (40, 10)) #update screen
                        print("Score ",turn)

                else: #if invalid, prompt user
                    #print("Invalid")
                    label = myfont.render("            Invalid!!!", 1, PURPLE) #1 is the axis?
                    screen.blit(label, (40, 10)) #update screen
                    temp = 1
                    invalid_click += 1

    #Ask player 4 Input
            elif turn == 3:
                turn = -1 #restart to first player
                posx = event.pos[0] #0th position is position of x ex. (0,10)
                col = int(math.floor(posx/SQUARESIZE)) #round down int for column
                if is_valid_location(board, col): #check if input is a valid location
                    row = get_next_open_row(board, col) #find next available row
                    drop_piece(board, row, col, 4) #drop piece in next available spot

                    if winning_move2(board, row, col, 4): #check if won
                        player4 += 1
                        label = myfont.render("       Player 4 Scores!!!", 1, GREEN) #1 is the axis?
                        screen.blit(label, (40, 10)) #update screen
                        print("Score ",turn)

                else: #if invalid, prompt user
                    label = myfont.render("            Invalid!!!", 1, GREEN) #1 is the axis?
                    screen.blit(label, (40, 10)) #update screen
                    temp = 1
                    invalid_click += 1


            if temp == 0:
                turn += 1 #increment turn by 1
            
            total_clicks += 1
            announce = 0
            end = 0

            if total_clicks - invalid_click == 168:
                announce = 1
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE)) #update last circle to black
            
            if announce == 1:
                if(player1 > player2 and player1 > player3 and player1 > player4):
                    label = myfont.render("Player 1 Wins!!!", 1, RED) #1 is the axis?
                    screen.blit(label, (40, 10)) #update screen
                    end = 1
                elif(player2 > player1 and player2 > player3 and player2 > player4):
                    label = myfont.render("Player 2 Wins!!!", 1, YELLOW) #1 is the axis?
                    screen.blit(label, (40, 10)) #update screen
                    end = 1
                elif(player3 > player1 and player3 > player2 and player3 > player4):
                    label = myfont.render("Player 3 Wins!!!", 1, PURPLE) #1 is the axis?
                    screen.blit(label, (40, 10)) #update screen
                    end = 1
                elif(player4 > player1 and player4 > player2 and player1 > player3):
                    label = myfont.render("Player 4 Wins!!!", 1, GREEN) #1 is the axis?
                    screen.blit(label, (40, 10)) #update screen
                    end = 1
                else:
                    label = myfont.render("DRAW!!!", 1, GREEN) #1 is the axis?
                    screen.blit(label, (40, 10)) #update screen
                    end = 1

            print_board(board)
            draw_board(board)
            print("Player 1: " + str(player1))
            print("Player 2: " + str(player2))
            print("Player 3: " + str(player3))
            print("Player 4: " + str(player4))
            
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE)) #update last circle to black
            label = myfont.render("P1: " + str(player1) + "     P2: " + str(player2) + "     P3: " + str(player3) + "     P4: " + str(player4), 1, WHITE)
            screen.blit(label, (40, 10)) #update screen
            pygame.time.wait(350)

            if end == 1:
                game_over = True

            if game_over:
                pygame.time.wait(10000)