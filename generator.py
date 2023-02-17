import random
from solver import generateSudoku

''' 
Create new unsolved puzzle by removing numbers in cells
'''
def removeCells(grid, guess):
    for i in range(guess):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        
        while grid[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)

        grid[row][col] = 0

    return grid


''' Levels of Dificulty '''

''' Easy Level''' 
def Easy(grid):
    if generateSudoku(grid, 0, 0):    
        return removeCells(grid, 35)
    else:
        return "easy"
    

''' Medium Level ''' 
def Medium(grid):
    if generateSudoku(grid, 0, 0):    
        return removeCells(grid, 45)
    else:
        return "medium"
    

''' Hard Level ''' 
def Hard(grid):
    if generateSudoku(grid, 0, 0):    
        return removeCells(grid, 55)
    else:
        return "hard"
    

''' Expert Level ''' 
def Expert(grid):
    if generateSudoku(grid, 0, 0):    
        return removeCells(grid, 65)
    else:
        return "expert"