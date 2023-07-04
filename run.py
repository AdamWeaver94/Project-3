# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

# constants for game
ship_sizes = [2,3,3,4,5]
player_board = [[""] * 10 for i in range(10)]
computer_board = [[""] * 10 for i in range(10)]
player_guess_board = [[""] * 10 for i in range(10)]
computer_guess_board = [[""] * 10 for i in range(10)]
letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

# board axis
def print_board(board):
    print(" A B C D E F G H I J")
    print(" +-+-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

#