
# Checking whether the guess at the row/column of the grid  
# is a valid guess and is safe to move
def isSafeToMove(grid, row, col, guess):

    # Check if same number occurs in rows
    for r in range(9):
        if grid[row][r] == guess:
            return False
        
    # Check if same number occurs in columns
    for c in range(9):
        if grid[c][col] == guess:
            return False
        
    # Check if same number exist in 3x3 Grid
    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    for r in range(3):
        for c in range(3):
            if grid[startRow + r][startCol + c] == guess:
                return False
            
    return True


# Solve sudoku puzzle using backtracking
def solveSudoku(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    
    for guess in range(1, 10):
        # CHeck if this guess is valid
        if isSafeToMove(grid, row, col, guess):
            # If valid, then place that guess on the board
            grid[row][col] = guess
            # Then recurse this grid to call our function
            if solveSudoku(grid, row, col + 1):
                return True

        # If not valid, then we need to backtrack
        # and try a new guess/number 
        grid[row][col] = -1
