from tkinter import *


window = Tk()
window.title("Sudoku Solver")
window.geometry("370x480")


label = Label(window, text="Welcome to Sudoku Generator and Solver!",
              font=("Helvetica", 12), fg="black", pady = 10)
label.grid(row=0, column=1,columnspan=10)

# For unsolvavble sudoku puzzle
errorLabel = Label(window, text="", fg="red", font=("Arial", 16))
errorLabel.grid(row=20, column=1, columnspan=10, pady=20)

# For solvable sudoku puzzle
solvedLable = Label(window, text="", fg="green", font=("Arial", 16))
solvedLable.grid(row=20, column=1, columnspan=10, pady=20)


window.mainloop()