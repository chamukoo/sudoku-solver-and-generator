import random

''' 
Checking whether the guess at the row/column of  
the grid is a valid guess and is safe to move 
'''
def checkValidity(grid, row, col, guess):

    ''' Check if same number occurs in rows '''
    for r in range(9):
        if grid[row][r] == guess:
            return False
        
    ''' Check if same number occurs in column '''
    for c in range(9):
        if grid[c][col] == guess:
            return False
        
    ''' Check if same number exist in 3x3 Grid '''
    startRow, startCol = (row // 3) * 3, (col // 3) * 3
    for r in range(startRow, startRow + 3):
        for c in range(startCol, startCol + 3):
            if grid[r][c] == guess:
                return False
            
    return True


''' Solve sudoku puzzle using backtracking '''
def solveSudoku(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    ''' Checking if the cell is filled with non-zero number '''
    if grid[row][col] > 0:

        ''' 
        Starting the sudoku solver again, then 
        recursion call is done to move to the next column 
        '''
        return solveSudoku(grid, row, col + 1)
    
    for guess in range(1, 10):

        ''' Check if the guess is valid'''
        if checkValidity(grid, row, col, guess):

            ''' If valid, then place that guess on the board '''
            grid[row][col] = guess

            ''' Then recurse this grid to call our function '''
            if solveSudoku(grid, row, col + 1):
                return True

        '''
        If not valid, then we need to backtrack
        and try a new guess/number, reset to zero
        '''
        grid[row][col] = 0

    return False


''' Generate completed sudoku puzzle '''
def generateSudoku(grid, row, col):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if col == 9:
            if row == 8:
                return True
            row += 1
            col = 0

        ''' Skipping grid if the grid has already a number '''
        if grid[row][col] != 0:
            if generateSudoku(grid, row, (col + 1)):
                return True
                
        # Solving for the grid if the grid is empty
        else:
            ''' Randomize number '''
            random.shuffle(num)
            for guess in num:

                ''' Check if the guess is valid '''
                if checkValidity(grid, row, col, guess):

                    ''' If valid, then place that guess on the grid '''
                    grid[row][col] = guess
                    
                    ''' Then recurse this grid to call our function '''
                    if generateSudoku(grid, row, (col + 1)):
                        return True
                    
                ''' 
                If not valid, then we need to backtrack, 
                and try a new number, reset to zero 
                '''
                grid[row][col] = 0

        return False


''' Create New Puzzle '''
def createSudoku(grid, row, col):

    ''' The range here is the amount of numbers in the grid '''
    for r in range(1, 17):

        ''' Choose random numbers '''
        row = random.randrange(9)
        col = random.randrange(9)
        guess = random.randrange(1,10)

        while not checkValidity(grid, row, col, guess) or grid[row][col] != 0:
            row = random.randrange(9)
            col = random.randrange(9)
            guess = random.randrange(1,10)

        grid[row][col] = guess

    return grid


''' Solver '''
def Solver(grid):
    if solveSudoku(grid, 0, 0):
        return grid
    else:
        return "solve"
        

''' Generator '''
def Generator(grid):
    if generateSudoku(grid, 0, 0):
        return grid
    else:
        return "generate"


''' Puzzle '''
def Puzzle(grid):
    if createSudoku(grid, 0, 0):
        return grid
    else:
        return "puzzle"