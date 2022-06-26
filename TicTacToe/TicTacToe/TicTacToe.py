# Vinson Mach
# This is my first python game: Tic Tac Toe with 2 players on the same keyboard

from IPython.display import clear_output

def display_board(board): 
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def main():
    testboard = ['#','X','O','X','O','X','O','X','O','X']
    display_board(testboard)

if __name__ == "__main__":
    main()