import random
from solver import generateSudoku

''' 
Create new unsolved puzzle by removing numbers in cells
'''
def createPuzzle(grid, num):   

    while num > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
            num -= 1
    return grid


''' Levels of Difficulty '''

''' Easy Level''' 
def Easy(grid):
    if generateSudoku(grid, 0, 0):  
        return createPuzzle(grid, 35)
    else:
        return "easy"
   
    

''' Medium Level ''' 
def Medium(grid):
    if generateSudoku(grid, 0, 0):  
        return createPuzzle(grid, 45)
    else:
        return "medium"
    

''' Hard Level ''' 
def Hard(grid):
    if generateSudoku(grid, 0, 0):    
        return createPuzzle(grid, 55)
    else:
        return "hard"
    

''' Expert Level ''' 
def Expert(grid):
    if generateSudoku(grid, 0, 0):    
        return createPuzzle(grid, 65)
    else:
        return "expert"