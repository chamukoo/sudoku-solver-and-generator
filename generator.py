import random
from solver import checkValidity

# Generate completed sudoku puzzle
def generateSudoku(grid, row, col):
    num = list(range(1, 10))
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    # Skipping grid if the grid has already a number
    if grid[row][col] != 0:
        return generateSudoku(grid, row, col + 1)
    else:
        # Randomize number
        random.shuffle(num)
        for guess in num:
            # Check if the guess is valid
            if checkValidity(grid, row, col, guess):
                # If valid, then place that guess on the grid
                grid[row][col] = guess
                # Then recurse this grid to call our function
                if generateSudoku(grid, row, col + 1):
                    return True
                # If not valid, then we need to backtrack, and try a new number, reset to zero
                grid[row][col] = 0

    return False

# Create new unsolved puzzle by removing numbers in cells
def createPuzzle(grid, num):
    while num > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
            num -= 1
    return grid

# Generator
def Generator(grid):
    if generateSudoku(grid, 0, 0):
        return grid
    else:
        return "generate"

# Levels of Difficulty
def generatePuzzleByLevel(grid, empty_cells):
    if generateSudoku(grid, 0, 0):
        return createPuzzle(grid, empty_cells)
    else:
        return "unsolvable"

# Easy Level
def Easy(grid):
    return generatePuzzleByLevel(grid, 34)

# Medium Level
def Medium(grid):
    return generatePuzzleByLevel(grid, 44)

# Hard Level
def Hard(grid):
    return generatePuzzleByLevel(grid, 54)

# Expert Level
def Expert(grid):
    return generatePuzzleByLevel(grid, 64)