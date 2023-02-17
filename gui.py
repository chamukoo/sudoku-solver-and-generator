from tkinter import *
from solver import Solver, Generator
from generator import Easy, Medium, Hard, Expert
import time


window = Tk()
window.title("Sudoku Solver")
window.geometry("370x600")
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
            timeStamp = "Solved in {:.18f} seconds".format(endTime - startTime )
            solvedLabel.configure(text='Sudoku is SOLVED!')
            timeLabel.configure(text=timeStamp)
    else:
        errorLabel.configure(text='Sudoku is UNSOLVABLE!')


'''
Generates a random and completed sudoku 
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
            timeStamp = "Generated in {:.18f} seconds".format(endTime - startTime)
            timeLabel.configure(text=timeStamp)


''' 
Create an unsolved sudoku puzzle 
Level of Difficulty (Easy, Medium, Hard, Expert)
'''

def easySudoku(sudoku):
    startTime = time.time()
    easy = Easy(sudoku)
    if easy != "easy":
        for row in range(2, 11):
            for col in range(1, 10):
                cells[(row, col)].delete(0, END)
                cells[(row, col)].insert(0, easy[row - 2][col - 1])
                endTime = time.time()
            timeStamp = "Generated in {:.18f} seconds".format(endTime - startTime)
            timeLabel.configure(text=timeStamp)

def mediumSudoku(sudoku):
    startTime = time.time()
    medium = Medium(sudoku)
    if medium != "medium":
        for row in range(2, 11):
            for col in range(1, 10):
                cells[(row, col)].delete(0, END)
                cells[(row, col)].insert(0, medium[row - 2][col - 1])
                endTime = time.time()
            timeStamp = "Generated in {:.18f} seconds".format(endTime - startTime)
            timeLabel.configure(text=timeStamp)

def hardSudoku(sudoku):
    startTime = time.time()
    hard = Hard(sudoku)
    if hard != "hard":
        for row in range(2, 11):
            for col in range(1, 10):
                cells[(row, col)].delete(0, END)
                cells[(row, col)].insert(0, hard[row - 2][col - 1])
                endTime = time.time()
            timeStamp = "Generated in {:.18f} seconds".format(endTime - startTime)
            timeLabel.configure(text=timeStamp)

def expertSudoku(sudoku):
    startTime = time.time()
    expert = Expert(sudoku)
    if expert != "expert":
        for row in range(2, 11):
            for col in range(1, 10):
                cells[(row, col)].delete(0, END)
                cells[(row, col)].insert(0, expert[row - 2][col - 1])
                endTime = time.time()
            timeStamp = "Generated in {:.18f} seconds".format(endTime - startTime)
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
    updateSudoku(board)

'''
Function to generate solved sudoku puzzle 
'''
def regenerate():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    timeLabel.configure(text="")

    grid = [[0 for r in range(9)] for c in range(9)]
                
    for row in range(9):
        for col in range(9):
            grid[row][col] = 0
    generateSudoku(grid)

''' 
This will create an unsolved sudoku 
Easy level - 35 empty cells
'''
def easy():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    timeLabel.configure(text="")

    grid = [[0 for r in range(9)] for c in range(9)]    
    easySudoku(grid)

''' 
This will create an unsolved sudoku
Medium level - 45 empty cells
'''
def medium():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    timeLabel.configure(text="")

    grid = [[0 for r in range(9)] for c in range(9)]              
    mediumSudoku(grid)

''' 
This will create an unsolved sudoku 
Hard level - 55 empty cells
'''
def hard():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    timeLabel.configure(text="")

    grid = [[0 for r in range(9)] for c in range(9)]            
    hardSudoku(grid)

''' 
This will create an unsolved sudoku 
Expert level - 65 empty cells
'''
def expert():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    timeLabel.configure(text="")

    grid = [[0 for r in range(9)] for c in range(9)]          
    expertSudoku(grid)

'''
Function to clear the board/cells 
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

''' For Level of Difficulties '''
levelLabel = Label(window, text="Level of Difficulties", 
                  fg="white", bg="black", 
                  font=("Arial", 10, 'bold'))
levelLabel.grid(row=35, column=1, columnspan=10,  pady=5)


''' Buttons '''

''' For solving the board '''
solveBtn = Button(window, command=solve, text='Solve', 
                  padx=1, pady=3, width=12, 
                  fg='white', bg='black', 
                  activebackground='light cyan', 
                  font=('Arial', 10, 'bold'))
solveBtn.grid(row=30, column=0, columnspan=5, pady=5)

''' For generating solved sudoku puzzle '''
generateBtn = Button(window, command=regenerate, text='Generate', 
                     padx=1, pady=3, width=12, 
                     fg='white', bg='black', 
                     activebackground='light cyan', 
                     font=('Arial', 10, 'bold'))
generateBtn.grid(row=30, column=3, columnspan=5, pady=5)

''' For clearing the board '''
clearBtn = Button(window, command=clear, text='Clear', 
                  padx=1, pady=3, width=12,  
                  fg='white', bg='black', 
                  activebackground='light cyan', 
                  font=('Arial', 10, 'bold'))
clearBtn.grid(row=30, column=6, columnspan=5, pady=5)


''' Levels Buttons '''

''' Easy Button '''
easyBtn = Button(window, command=easy, text='Easy',
                padx=4, pady=1, width=12, 
                fg='white', bg='black',
                activebackground='green', 
                font=('Arial', 10, 'bold'))
easyBtn.grid(row=40, column=1, columnspan=5, pady=5)

''' Medium Button '''
mediumBtn = Button(window, command=medium, text='Medium',
                padx=4, pady=1, width=12, 
                fg='white', bg='black',
                activebackground='yellow', 
                font=('Arial', 10, 'bold'))
mediumBtn.grid(row=40, column=5, columnspan=5, pady=5)

''' Hard Button '''
hardBtn = Button(window, command=hard, text='Hard',
                padx=4, pady=1, width=12, 
                fg='white', bg='black',
                activebackground='orange', 
                font=('Arial', 10, 'bold'))
hardBtn.grid(row=50, column=1, columnspan=5, pady=5)

''' Expert Button '''
expertBtn = Button(window, command=expert, text='Expert',
                padx=4, pady=1, width=12, 
                fg='white', bg='black',
                activebackground='red', 
                font=('Arial', 10, 'bold'))
expertBtn.grid(row=50, column=5, columnspan=5, pady=5)


''' Main Loop '''

draw9x9Grid()
window.mainloop()