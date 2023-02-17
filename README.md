# Sudoku Generator and Solver in Python using Tkinter and Backtrack Algorithm
This is a simple project for solving and generating Sudoku puzzle. This program allow users to input sudoku puzzle on the board, solve the board, clear the board, generate a solved sudoku puzzle, and generate an unsolved sudoku puzzle. In generating a new unsolved puzzle, the user can choose different difficulty levels such as easy, medium, hard, and expert.


## The Original Project

The [orginal project](https://www.youtube.com/watch?v=xAXmfZmC2SI) only solve and clear the board using backtracking algorithm, and it also has GUI.


## Modifications I Made to Improve the Code

***1. Sudoku Generator***

Using backtrack algorithm and random module to uniquely generate solved sudoku puzzle, and unsolved soduku puzzle with varying levels.


***2. Level of Difficulty***

I included a four (4) difficulty levels (Easy, Medium, Hard, and Expert) to make this program more challenging, and to demonstrate how backtrack algorithm works in solving different levels of sudoku puzzle. The Easy level has 34 empty cells, Medium level has 44 empty cells, Hard level has 54 empty cells, and Expert level has 64 empty cells. 


***3. Execution Time of Program***

I imported time module, then measured the execution time in solving a sudoku puzzle and generating a sudoku puzzle using time() function. I decided to inlude this because this project has different levels and each generated puzzle is unique which would affect the execution time of every solved and generated board. Thus, I included this to determine how fast or slow it took to solve and generate a board using backtrack algorithm.


***4. Improved Tkinter GUI***

I enhanced the Tkinter GUI by adding a photo, new buttons for the generator and for the different difficulty levels, and new label for the execution time so the users can see how many seconds it took to solve and generate a board.



Disclaimer: The concept of this program was from ["Sharnav's Tech"](https://www.youtube.com/@SharnavTech) youtube channel and was modified and improved for educational purposes. 

Links: 
https://www.youtube.com/watch?v=xAXmfZmC2SI
https://www.youtube.com/watch?v=OF0H0B0IuFM&t=72s