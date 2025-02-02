import numpy as np

class SudokuBoard:
    def __init__(self):
        self.board = np.array([
            [0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0.]
        ])

    def setBoard(self,x,y,value):
        """
        Set the contents of the board

        Keyword arguments:
        x -- the x coordinate
        y -- the y coordinate
        value -- desired value of the cell
        """
        self.board[x,y] = value

def checkValid():
        """
        Check board Validity
        """
        
        pass

def solveBoard():
     """
     Solves the Board
     """
     pass