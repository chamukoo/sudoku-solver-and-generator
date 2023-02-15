from tkinter import *
from solver import puzzleSolver


window = Tk()
window.title("Sudoku Solver")
window.geometry("370x480")


cells = {}


# Checking the validity of numbers
def isValid(P):
    out = (P.isdigit() or P=="") and len(P) < 2
    return out

reg = window.register(isValid)


# Drawing the 3x3 Grid
def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            userInput = Entry(window, width=5, bg=bgcolor, fg='black', 
                              font=('Arial', 10, 'bold'), justify='center', cursor="plus", 
                              validate='key', validatecommand=(reg, '%P'))
            userInput.grid(row=row+i+1, column=column+j+1, sticky='nsew', 
                           padx=1, pady=1, ipady=5)
            cells[(row+i+1, column+j+1)] = userInput


# Drawing a 9x9 Grid 
def draw9x9Grid():
    color = "light yellow"
    for row in range(1, 10, 3):
        for col in range(0, 9 , 3):
            draw3x3Grid(row, col, color)
            if color == "light yellow":
                color = "light cyan"
            else:
                color = "light yellow"


# Function to get the values (called by solve button)
def access():
    board= []
    errorLabel.configure(text="")
    solvedLabel.configure(text="")

    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))

        board.append(rows)
    update(board)


# Function to clear board (called by clear button)
def clear():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")

    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")


# Update the values in Cells
def update(s):
    solve = puzzleSolver(s)
    if solve != "solve":
        for rows in range(2, 11):
            for cols in range(1, 10):
                cells[(rows, cols)].delete(0, "end")
                cells[(rows, cols)].insert(0, solve[rows - 2][cols - 1])
            solvedLabel.configure(text='Sudoku is SOLVED!')
    else:
        errorLabel.configure(text='Sudoku is UNSOLVABLE!')



label = Label(window, text="Welcome to Sudoku Solver!",
              font=("Helvetica", 12), fg="black", pady = 10)
label.grid(row=0, column=1,columnspan=10)

# For unsolvavble sudoku puzzle
errorLabel = Label(window, text="", fg="red", font=("Arial", 16))
errorLabel.grid(row=20, column=1, columnspan=10, pady=20)

# For solvable sudoku puzzle
solvedLabel = Label(window, text="", fg="green", font=("Arial", 16))
solvedLabel.grid(row=20, column=1, columnspan=10, pady=20)

# Create buttons for solving and clearing the board
getBtn = Button(window, command=access, text='Solve', width=10,
                activebackground='light cyan', font=('Arial', 10, 'bold'))
getBtn.grid(row=50, column=1, columnspan=5, pady=20)

clearBtn = Button(window, command=clear, text='Clear', width=10,
                  activebackground='light cyan', font=('Arial', 10, 'bold'))
clearBtn.grid(row=50, column=5, columnspan=5, pady=20)


# Main Loop
draw9x9Grid()
window.mainloop()