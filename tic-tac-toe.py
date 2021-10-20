#!/usr/bin/env python
# coding: utf-8

# **Function to print the board**



from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(' ',' ',' ', '|', ' ', '|', ' ')
    print(' ',' ',board[7],'|',board[8],'|',board[9] )
    print(' ',' ',' ', '|', ' ', '|', ' ')
    print('-----------------')
    print(' ',' ',' ', '|', ' ', '|', ' ')
    print(' ',' ',board[4],'|',board[5],'|',board[6] )
    print(' ',' ',' ', '|', ' ', '|', ' ')
    print('-----------------')
    print(' ',' ',' ', '|', ' ', '|', ' ')
    print(' ',' ',board[1],'|',board[2],'|',board[3] )
    print(' ',' ',' ', '|', ' ', '|', ' ')
    


# **Function to take input of the players input which may be either X or O**



def player_input():
    marker = ''
    while (marker != 'X' and marker != 'Y'):
        marker = input('Player 1, choose between X and Y!').upper()
    
    if marker == 'X':
        return ('X','Y')
    else:
        return ('Y','X')


# **Assigning the desired position, entered by the player to the board **



def place_marker(board, marker2, position):
    
    
    board[int(position)] = marker2
    


# **To check after input whether the player has won or not?**



def win_check(board,mark):
     return (board[1] == mark and board[2] == mark and board[3] == mark or
     board[1] == mark and board[2] == mark and board[3] == mark or 
     board[4] == mark and board[5] == mark and board[6] == mark or
     board[7] == mark and board[8] == mark and board[9] == mark or
     board[1] == mark and board[4] == mark and board[7] == mark or
     board[2] == mark and board[5] == mark and board[8] == mark or
     board[3] == mark and board[6] == mark and board[9] == mark or
     board[1] == mark and board[5] == mark and board[9] == mark or                                      
     board[3] == mark and board[5] == mark and board[7] == mark)
    


# **Function which selects the random player**


import random

def choose_first():
    players = ('Player1', 'Player2')
    player = random.choice(players)
    
    return player + ' will go first'
        


# **To check whether the space input by the player is available on the board or not?**


def space_check(board, position):
    return board[position] == " "


# **To check whether the board is full or not after the players input**


def full_board_check(board):
    for position in range(1,len(board)):
        if board[position] == ' ':
            return False
    return True
     


# **Function asking for players next position, checking that the same is available or not in the board and then assigning the value to the board if returned true**


def player_choice(board):
    global num
    
    for location in range(1,10):
        location = input("Choose your next position(1,9) : ")
        num = int(location)
        a = ['Nice!','Well played!','Nice move!']
        if space_check(board,num) == False:
            print('That position is already filled') 
            continue
        else:
            print(random.choice(a))
        break
     
    return num 


# **Function asking players whether they want to play again or not?**


def replay():
    ans = input('Do you want to play again? Enter Yes or No: ')
    return ans.lower() == 'y'


# **Combining each and every function at their respective places**


print('Welcome to Tic Tac Toe!')
while True:
    tic_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    
    ask = input('Are you ready to play?')
    if ask.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        print('Type Yes whenever you are ready!')
        
    while game_on:
        
        if turn == 'Player1':
            display_board(tic_board)
            position = player_choice(tic_board)
            place_marker(tic_board,player1_marker,position)
            
            if win_check(tic_board, player1_marker):
                display_board(tic_board)
                print("Congratulations! You've won the game.")
                game_on = False
            else:
                if full_board_check(tic_board):
                    display_board(tic_board)
                    print('Game is Draw!')
                    break
                else:
                    turn = 'Player2'
        
        else:
            display_board(tic_board)
            position = player_choice(tic_board)
            place_marker(tic_board,player2_marker,position)
            
            if win_check(tic_board, player2_marker):
                display_board(tic_board)
                print("Congratulations! You've won the game.")
                game_on = False
            else:
                if full_board_check(tic_board):
                    display_board(tic_board)
                    print('Game is Draw!')
                    break
                else:
                    turn = 'Player1'
    if not replay():
        print('Thanks for playing')
        break

