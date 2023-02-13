
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

