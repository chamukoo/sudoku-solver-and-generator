from tkinter import *
from solver import Solver, Generator, Remove
import time


window = Tk()
window.title("Sudoku Solver")
window.geometry("370x580")
window.configure(bg="black")


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
                              font=('Arial', 10, 'bold'), 
                              justify='center', cursor="plus", 
                              validate='key', validatecommand=(reg, '%P'))
            num.grid(row = row + i + 1, column = column + j + 1, sticky='nsew', 
                           padx=1, pady=1, ipady=5)
            cells[(row + i + 1, column + j + 1)] = num


''' Drawing a 9x9 Grid '''
def draw9x9Grid():
    color = "white"
    for row in range(1, 10, 3):
        for col in range(0, 9 , 3):
            draw3x3Grid(row, col, color)
            if color == "white":
                color = "light cyan"
            else:
                color = "white"


''' Update the values in Cells '''
def updateSudoku(sudoku):
    startTime = time.time()
    solve = Solver(sudoku)
    if solve != "solve":
        for row in range(2, 11):
            for col in range(1, 10):
                cells[(row, col)].delete(0, END)
                cells[(row, col)].insert(0, solve[row - 2][col - 1])
                endTime = time.time()
                timeStamp = "Solved in {:.12f} seconds".format(endTime - startTime )
            solvedLabel.configure(text='Sudoku is SOLVED!')
            timeLabel.configure(text=timeStamp)
    else:
        errorLabel.configure(text='Sudoku is UNSOLVABLE!')


'''
Sudoku is in the correct format and is completly random
Generates a completed sudoku 
(called by new button)
'''
def generateSudoku(sudoku):
    startTime = time.time()
    new = Generator(sudoku)
    if new != "generate":
        for row in range(2, 11):
            for col in range(1, 10):
                cells[(row, col)].delete(0, END)
                cells[(row, col)].insert(0, new[row - 2][col - 1])
                endTime = time.time()
                timeStamp = "Generated in {:.12f} seconds".format(endTime - startTime)
            timeLabel.configure(text=timeStamp)


''' Create an unsolved sudoku puzzle '''
def createSudoku(sudoku):
    startTime = time.time()
    new = Remove(sudoku)
    if new != "remove":
        for row in range(2, 11):
            for col in range(1, 10):
                cells[(row, col)].delete(0, END)
                cells[(row, col)].insert(0, new[row - 2][col - 1])
                endTime = time.time()
                timeStamp = "Generated in {:.12f} seconds".format(endTime - startTime)
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
    updateSudoku(board)


'''
Function to generate solved sudoku puzzle 
(called by generate button)
'''
def regenerate():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    timeLabel.configure(text="")

    grid = [[0 for r in range(9)] for c in range(9)]
                
    for row in range(9):
        for col in range(9):
            grid[row][col] = 0
    
    ''' This will generate a solved sudoku '''
    generateSudoku(grid)


'''
Function to create new usolved sudoku puzzle 
(called by generate button)
'''
def create():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    timeLabel.configure(text="")

    grid = [[0 for r in range(9)] for c in range(9)]
                
    ''' This will create an unsolved sudoku'''
    createSudoku(grid)


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

photo = PhotoImage(file='sudoku.png')
label = Label(window,  pady = 10, padx=10,
              fg="white", bg="black", 
              font=("Helvetica", 12, "bold"), 
              image=photo, compound='bottom')
label.grid(row=0, column=1,columnspan=10)

''' For unsolvavble sudoku puzzle '''
errorLabel = Label(window, text="", 
                   fg="red", bg="black", 
                   font=("Arial", 16, 'bold'))
errorLabel.grid(row=20, column=1, columnspan=10, pady=5)

''' For solvable sudoku puzzle '''
solvedLabel = Label(window, text="", 
                    fg="green", bg="black", 
                    font=("Arial", 16, 'bold'))
solvedLabel.grid(row=20, column=1, columnspan=10, pady=5)

''' Display time of execution '''
timeLabel = Label(window, text="", 
                  fg="white", bg="black", 
                  font=("Arial", 10, 'bold'))
timeLabel.grid(row=15, column=1, columnspan=10)


''' Buttons '''

''' For creating unsolved puzzle '''
newBtn = Button(window, command=create, text='New Puzzle',
                padx=6, pady=6, width=12, 
                fg='white', bg='black',
                activebackground='light cyan', 
                font=('Arial', 10, 'bold'))
newBtn.grid(row=30, column=1, columnspan=5, pady=5)

''' For solving the board '''
solveBtn = Button(window, command=solve, text='Solve', 
                  padx=6, pady=6, width=12, 
                  fg='white', bg='black', 
                  activebackground='light cyan', 
                  font=('Arial', 10, 'bold'))
solveBtn.grid(row=30, column=5, columnspan=5, pady=5)

''' For generating new sudoku puzzle '''
generateBtn = Button(window, command=regenerate, text='Generate', 
                     padx=6, pady=6, width=12, 
                     fg='white', bg='black', 
                     activebackground='light cyan', 
                     font=('Arial', 10, 'bold'))
generateBtn.grid(row=50, column=1, columnspan=5, pady=5)

''' For clearing the board '''
clearBtn = Button(window, command=clear, text='Clear', 
                  padx=6, pady=6, width=12,  
                  fg='white', bg='black', 
                  activebackground='light cyan', 
                  font=('Arial', 10, 'bold'))
clearBtn.grid(row=50, column=5, columnspan=5, pady=5)


''' Main Loop '''

draw9x9Grid()
window.mainloop()