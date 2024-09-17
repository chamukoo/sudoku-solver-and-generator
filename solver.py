# Checking whether the guess at the row/column of the grid is a valid guess and if safe to move
def checkValidity(grid, row, col, guess):
    # Check if same number occurs in rows
    for r in range(9):
        if grid[row][r] == guess:
            return False

    # Check if same number occurs in column
    for c in range(9):
        if grid[c][col] == guess:
            return False

    # Check if same number exists in 3x3 Grid
    startRow, startCol = (row // 3) * 3, (col // 3) * 3
    for r in range(startRow, startRow + 3):
        for c in range(startCol, startCol + 3):
            if grid[r][c] == guess:
                return False

    return True

# Solve sudoku puzzle using backtracking
def solveSudoku(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    # Checking if the cell is filled with non-zero number
    if grid[row][col] > 0:
        # Starting the sudoku solver again, then recursion call is done to move to the next column
        return solveSudoku(grid, row, col + 1)

    for guess in range(1, 10):
        # Check if the guess is valid
        if checkValidity(grid, row, col, guess):
            # If valid, then place that guess on the board
            grid[row][col] = guess

            # Then recurse this grid to call our function
            if solveSudoku(grid, row, col + 1):
                return True

            # If not valid, then we need to backtrack and try a new guess/number, reset to zero
            grid[row][col] = 0

    return False

# Solver
def Solver(grid):
    if solveSudoku(grid, 0, 0):
        return grid
    else:
        return "solve"