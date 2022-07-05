# Vinson Mach 6/29/2022
# First python game: Tic Tac Toe with 2 players on the same keyboard

from IPython.display import clear_output
import random

# This function will assign player idols
def player_input():
    marker = ' '                                                # initialize markers
    while marker != 'X' and marker != 'O':                      # keep asking player 1 if they are x or o
        marker = input("Player 1: Choose X or O: ").upper()     # ask player 1 for their idol

    player1 = marker                                            # assign player idols
    if player1 == 'X':                                          # assign other player's idol
        return ('X', 'O')                                       # return p1 = x, p2 = o
    else:
        return ('O', 'X')                                       # return p1 = o, p2 = x

# This function will handle placing player idols
def place_marker(board, marker, position):                      
    board[position] = marker                                    # places player idol at board position

# This function will check for win conditions
def win_condition(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or    # check accross the bottom row
            (board[4] == board[5] == board[6] == marker) or    # check accross the middle row
            (board[7] == board[8] == board[9] == marker) or    # check accross the top row
            (board[1] == board[4] == board[7] == marker) or    # check down the left column
            (board[2] == board[5] == board[8] == marker) or    # check down the middle column
            (board[3] == board[6] == board[9] == marker) or    # check down the right column
            (board[1] == board[5] == board[9] == marker) or    # check diagonal
            (board[3] == board[5] == board[7] == marker))      # check diagonal

# This function will do a coin flip to see who goes first
def choose_first():
    flip = random.randint(0, 1)                                 # coin flip to see who goes first
    if flip == 0:
        return 'Player 1'                                       # p1 goes first
    else:
        return 'Player 2'                                       # p2 goes first

# This function checks to see if this position is empty
def space_check(board, postion):
    return board[postion] == ' '                                # return contents of board position

# This function checks to see if the board is full
def full_board_check(board):
    for i in range (1, 10):
        if space_check(board, i):
            return False                                        # return false if board not full
    return True                                                 # return true if board is full

# This function asks player for where they want to place their next idol
def player_choice(board):
    position = 0                                                # initialize player position
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('\nChoose a position (1 - 9): '))  # ask player for next position
    return position                                             # return player's next position

# This function asks the players if they want to play again
def replay():
    choice = input('Play again? Enter Y or N ').upper()         # ask players if they want to play again
    return choice == 'Y'                                        # return player input

# This function displays the gameboard
def display_board(board): 
    clear_output()                                              # clear board outputs
    print(board[7] + '|' + board[8] + '|' + board[9])           # display the top row
    print("-----")                                              # display spacer
    print(board[4] + '|' + board[5] + '|' + board[6])           # display the middle row
    print("-----")                                              # display spacer
    print(board[1] + '|' + board[2] + '|' + board[3])           # display the bottom row

# Main Function will handle game intro and end
def main():

    print('\nWelcome to a game of TicTacToe')                   # display title statement
    while True:
        gameboard = [' ']*10                                    # initialize gameboard
        p1Marker, p2Marker = player_input()                     # get player idols
        turn = choose_first()                                   # who goes first
        print(turn + ' will go first')                          # print who goes first
        play_game = input('\nPlay Game? Enter Y or N: ').upper()# ask players if they are ready to play game
        if play_game == 'Y':
            game_on = True                                      # play game
        else:
            game_on = False                                     # dont play game

        while game_on:
            if turn == 'Player 1':
                display_board(gameboard)                        # display gameboard
                position = player_choice(gameboard)             # where p1's next idol goes
                place_marker(gameboard, p1Marker, position)     # place p1's idol at this position
                if win_condition(gameboard, p1Marker):          # check for win condition
                    display_board(gameboard)                    # display current gameboard
                    print('Player 1 has won\n')                   # print p1 win statement
                    game_on = False                             # dont play game
                else:
                    if full_board_check(gameboard):             # check if board is full
                        display_board(gameboard)                # display current gameboard
                        print('Tie Game')                       # print tie statement
                        game_on = False                         # dont play game
                    else:
                        turn = 'Player 2'                       # move to p2's turn
            else:
                display_board(gameboard)                        # display gameboard
                position = player_choice(gameboard)             # where p2's next idol goes
                place_marker(gameboard, p2Marker, position)     # place p2's idol at this position
                if win_condition(gameboard, p2Marker):          # check for win condition
                    display_board(gameboard)                    # display current gameboard
                    print('Player 2 has won\n')                   # print p2 win statement
                    game_on = False                             # dont play game
                else:
                    if full_board_check(gameboard):             # check if board is full
                        display_board(gameboard)                # display current gameboard
                        print('Tie Game\n')                       # print tie statement
                        game_on = False                         # dont play game
                    else:
                        turn = 'Player 1'                       # move to p1's turn
        if not replay():
            break                                               # stop game

if __name__ == "__main__":
    main()