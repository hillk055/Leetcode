import numpy as np
import pandas as pd
import pyarrow
import string

class queens():

    def __init__(self, BOARD_SIZE, x_coordinate, y_coordinate):

        self.BOARD_HEIGHT = BOARD_SIZE
        self.BOARD_WIDTH = BOARD_SIZE
        self.board = np.zeros((self.BOARD_WIDTH, self.BOARD_HEIGHT))
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.queen_locations = [(x_coordinate, y_coordinate)]
        self.x_values = np.arange(self.BOARD_WIDTH)
    
    def queen_attack(self):
        '''
        generates list of values of all possible squares on the board the queen can attack
        all square that are attacked by a queen are replace with 1, so that in the next iteration we can avoid
        ones when placing the next queen
        :return: none
        '''
        x_values = np.arange(self.BOARD_WIDTH)
        vertical_attack = [(self.x_coordinate, y) for y in x_values if y < self.BOARD_WIDTH]
        horizontal_attack = [(x, self.y_coordinate) for x in x_values if x < self.BOARD_WIDTH]

        c_pos = self.y_coordinate - self.x_coordinate
        c_neg = self.y_coordinate + self.x_coordinate
        pos_diagonal_attack = [(x, x + c_pos) for x in x_values if self.BOARD_WIDTH > x + c_pos >= 0]
        neg_diagonal_attack = [(x, -x + c_neg) for x in x_values if self.BOARD_WIDTH > -x + c_neg >= 0]

        attack_square = horizontal_attack + vertical_attack + pos_diagonal_attack + neg_diagonal_attack

        for i, j in attack_square:
            self.board[i][j] = 1

    def add_queen(self):
        '''
        checks if there are any 0 values left, values which are not covered by an attacking queen, if
        there is an empty square the queen is placed on this square and then run through the attack function again
        to generate the square on which this queen acts
        :return:
        '''
        while (self.board == 0).any():
            rows, cols = np.where(self.board == 0)
            zeros = [i for i in zip(rows, cols)]
            self.x_coordinate, self.y_coordinate = zeros[0]
            self.queen_locations.append((self.x_coordinate, self.y_coordinate))
            self.queen_attack()
        return self.write_queen()

    def write_queen(self):
        '''
        converts the matrix to a datafram so that string can be added to make the board look nicer
        :return:
        '''
        for i, j in self.queen_locations:
            self.board[i][j] = 4
        board = pd.DataFrame(self.board)
        board.replace(float(1),'.', inplace=True)
        board.replace(float(4), 'Q', inplace=True)
        return board

instance1 = queens(4, 2, 2)
instance1.queen_attack()

