# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

# constants for game
SHIP_SIZES = [2,3,3,4,5]
PLAYER_BOARD = [[""] * 10 for i in range(10)]
COMPUTER_BOARD = [[""] * 10 for i in range(10)]
PLAYER_GUESS_BOARD = [[""] * 10 for i in range(10)]
COMPUTER_GUESS_BOARD = [[""] * 10 for i in range(10)]
LETTERS_TO-NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

# board axis
def print_board(board):
    print(" A B C D E F G H I J")
    print(" +-+-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

# placing ships
def place_ships(board):

    for ship_length in SHIP_SIZES:

        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,9), random.randint(0,9)
                if check_ship_fit(ship_length, row, column, orientation):

                    if ship_overlaps(board, row, column, orientation, ship_length) == False:

                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row, + ship_length):
                                board[i][column] = "X"
                        break
            else:
                place_ships = True
                print('Choose your ship size of' + str(ship_length))
                row, column, orientation = user_input(place_ships)
                if check_ship_fit(ship_length, row, column, orientation):

                         if ship_overlaps(board, row, column, orientation, ship_length) == False

                                if orientation == "H"
