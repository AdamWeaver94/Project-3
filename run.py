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

# generating board with labelled axis 
def print_board(board):
    print(" A B C D E F G H I J")
    print(" +-+-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

# placing ships around the board
# checking sizes and overlaps don't occur
# when user inputs orientation of ships
def place_ships(board):

    for size_of_ship in SHIP_SIZES:

        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,9), random.randint(0,9)
                if check_ship_fit(size_of_ship, row, column, orientation):

                    if ship_overlaps(board, row, column, orientation, size_of_ship) == False:

                        if orientation == "H":
                            for i in range(column, column + size_of_ship):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row, + size_of_ship):
                                board[i][column] = "X"
                        break
            else:
                place_ships = True
                print('Choose your ship size of' + str(size_of_ship))
                row, column, orientation = user_input(place_ships)
                if check_ship_fit(size_of_ship, row, column, orientation):

                         if ship_overlaps(board, row, column, orientation, size_of_ship) == False

                                if orientation == "H"
                                    for i in range(column, column + size_of_ship):
                                        board[row][i] = "X"
                                else:
                                    for i in range(row, row + size_of_ship):
                                        board[i][column] = "X"
                                print_board(PLAYER_BOARD)
                                break

# logic for checking if ship fits on board
def check_ship_fit(SHIP_SIZES, row, column, orientation):
    if orientation == "H":
        if column + SHIP_SIZES > 10:
            return False
        else:
            return True
    else:
        if row + SHIP_SIZES > 10:
            return False
        else:
            return True

# logic for checking ships dont overlap eachother
def ship_overlaps(board, row, column, orientation, size_of_ship):
    if orientation == "H":
        for i in range(column, column + size_of_ship):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + size_of_ship):
            if board[i][column] == "X":
                return True
    return False

# logic for user inputs for placing ships
# showing type errors if input out of spec
def user_input(place_ships):
    if place_ships == True:
        while True:
            try: 
                orientation = input("Enter orientation (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Enter a valid orientation H or V')
        while True:
            try: 
                row = input("Enter the row 1-10 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-10')
        while True:
            try: 
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGHIJ':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-J')
        return row, column, orientation 
    else:
        while True:
            try: 
                row = input("Enter the row 1-10 of the ship: ")
                if row in '12345678910':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-10')
        while True:
            try: 
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGHIJ':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-J')
        return row, column 

# logic for counter of hits + misses
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

# logic for players turn and 
# computer random turn
def turn(board):
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == "~":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "~"
    else:
        row, column = random.randint(0,7), random.randint(0,7)
        if board[row][column] == "~":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "~"

