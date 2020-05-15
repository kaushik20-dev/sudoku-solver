# !/usr/bin/env
import numpy as np


class PrintBoard:
    
    def print_board(self, grid):
        """
        print sudoku board

        params: 
        grid - numpy array of (9,9)
        """

        if not self.__is_valid_grid(grid):
            raise ValueError("input grid is not valid")

        print("+" + "---+"*9)
        for i, row in enumerate(grid):
            print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
            if i % 3 == 2:
                print("+" + "---+"*9)
            else:
                print("+" + "   +"*9)
    
    def __is_valid_grid(self, grid):
        """
        Check if the list has 9 nested lists, each should have 9 elements 

        params: 
        grid - numpy array of (9,9)

        return: Boolean value
        """
        
        if grid.shape == (9,9):
            return True
        return False
