from tkinter import *
from solver import Solver, Generator, Puzzle
import time


window = Tk()
window.title("Sudoku Solver")
window.geometry("370x580")


''' Making blank list to store all the entry widget cells '''
cells = {}


''' Checking the validity of numbers '''
def isValid(P):
    out = (P.isdigit() or P=="") and len(P) < 2
    return out

reg = window.register(isValid)


''' Drawing the 3x3 Grid '''
def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            num = Entry(window, width=5, bg=bgcolor, fg='black', 
                              font=('Arial', 10, 'bold'), justify='center', cursor="plus", 
                              validate='key', validatecommand=(reg, '%P'))
            num.grid(row = row + i + 1, column = column + j + 1, sticky='nsew', 
                           padx=1, pady=1, ipady=5)
            cells[(row + i + 1, column + j + 1)] = num


''' Drawing a 9x9 Grid '''
def draw9x9Grid():
    color = "light yellow"
    for row in range(1, 10, 3):
        for col in range(0, 9 , 3):
            draw3x3Grid(row, col, color)
            if color == "light yellow":
                color = "light cyan"
            else:
                color = "light yellow"


''' Update the values in Cells '''
def update(sudoku):
    startTime = time.time()
    solve = Solver(sudoku)
    if solve != "solve":
        for rows in range(2, 11):
            for cols in range(1, 10):
                cells[(rows, cols)].delete(0, END)
                cells[(rows, cols)].insert(0, solve[rows - 2][cols - 1])
                endTime = time.time()
                timeStamp = "Solved in {:.7f} seconds".format(endTime - startTime )
            solvedLabel.configure(text='Sudoku is SOLVED!')
            timeLabel.configure(text=timeStamp)
    else:
        errorLabel.configure(text='Sudoku is UNSOLVABLE!')


'''
Sudoku is in the correct format and is completly random
Generates a completed sudoku 
(called by new button)
'''
def generate(sudoku):
    startTime = time.time()
    new = Generator(sudoku)
    if new != "generate":
        for rows in range(2, 11):
            for cols in range(1, 10):
                cells[(rows, cols)].delete(0, END)
                cells[(rows, cols)].insert(0, new[rows - 2][cols - 1])
                endTime = time.time()
                timeStamp = "Generated in {:.7f} seconds".format(endTime - startTime)
            timeLabel.configure(text=timeStamp)


''' Create an unsolved sudoku puzzle '''
def scramble(sudoku):
    startTime = time.time()
    new = Puzzle(sudoku)
    if new != "puzzle":
        for rows in range(2, 11):
            for cols in range(1, 10):
                cells[(rows, cols)].delete(0, END)
                cells[(rows, cols)].insert(0, new[rows - 2][cols - 1])
                endTime = time.time()
                timeStamp = "Generated in {:.7f} seconds".format(endTime - startTime)
            timeLabel.configure(text=timeStamp)


''' 
Function to solve the sudoku puzzle
(called by solve button) 
'''
def solve():
    board= []
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    timeLabel.configure(text="")

    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))

        board.append(rows)
    
    ''' This will update the board to its correct solution '''
    update(board)


'''
Function to generate solved sudoku puzzle 
(called by generate button)
'''
def regenerate():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    timeLabel.configure(text="")

    grid = [[0 for r in range(9)] for c in range(9)]
                
    for r in range(9):
        for c in range(9):
            grid[r][c] = 0
    
    ''' This will generate a solved sudoku '''
    generate(grid)


'''
Function to create new usolved sudoku puzzle 
(called by generate button)
'''
def new():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    timeLabel.configure(text="")

    grid = [[0 for r in range(9)] for c in range(9)]
    
    ''' This will create an unsolved sudoku'''
    scramble(grid)


'''
Function to clear the board/cells 
(called by clear button)
'''
def clear():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    timeLabel.configure(text="")

    for row in range(2, 11):
        for col in range(1, 10):
            cells[(row, col)].delete(0, END)



''' Labels '''

label = Label(window, text="Welcome to Sudoku Generator and Solver!",
              font=("Helvetica", 12), fg="black", pady = 10)
label.grid(row=0, column=1,columnspan=10)

''' For unsolvavble sudoku puzzle '''
errorLabel = Label(window, text="", fg="red", font=("Arial", 16))
errorLabel.grid(row=20, column=1, columnspan=10, pady=10)

''' For solvable sudoku puzzle '''
solvedLabel = Label(window, text="", fg="green", font=("Arial", 16))
solvedLabel.grid(row=20, column=1, columnspan=10, pady=10)

''' Display time of execution '''
timeLabel = Label(window, text="", fg="black", font=("Arial", 10))
timeLabel.grid(row=15, column=1, columnspan=10)


''' Buttons '''

''' For creating unsolved puzzle '''
newBtn = Button(window, command=new, text='New Puzzle', width=12,
                activebackground='light cyan', font=('Arial', 10, 'bold'))
newBtn.grid(row=30, column=1, columnspan=5, pady=10)

''' For solving the board '''
solveBtn = Button(window, command=solve, text='Solve', width=12, 
                activebackground='light cyan', font=('Arial', 10, 'bold'))
solveBtn.grid(row=30, column=5, columnspan=5, pady=10)

''' For generating new sudoku puzzle '''
generateBtn = Button(window, command=regenerate, text='Generate', width=12,
                activebackground='light cyan', font=('Arial', 10, 'bold'))
generateBtn.grid(row=50, column=1, columnspan=5, pady=10)

''' For clearing the board '''
clearBtn = Button(window, command=clear, text='Clear', width=12, 
                  activebackground='light cyan', font=('Arial', 10, 'bold'))
clearBtn.grid(row=50, column=5, columnspan=5, pady=10)



''' Main Loop '''

draw9x9Grid()
window.mainloop()