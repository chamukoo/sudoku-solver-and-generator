# Sudoku Generator and Solver in Python using Tkinter and Backtracking Algorithm

This is a simple yet powerful Sudoku project built in Python using Tkinter for the GUI and the Backtracking Algorithm for solving Sudoku puzzles. The program allows users to input, solve, clear, and generate Sudoku puzzles, with options to create puzzles at various difficulty levels (Easy, Medium, Hard, and Expert).

![Sudoku GUI](https://user-images.githubusercontent.com/95155301/219721175-5b6e8eb0-a846-4438-a4d0-dd2f0402d615.png)

## Features

1. **Input Puzzle**: Users can manually input a Sudoku puzzle on the board.
2. **Solve Puzzle**: Automatically solve any valid Sudoku puzzle using the Backtracking Algorithm.
3. **Clear Board**: Clear the board to input a new puzzle.
4. **Generate Puzzle**: Generate both solved and unsolved Sudoku puzzles.
5. **Difficulty Levels**: Choose from Easy, Medium, Hard, and Expert difficulty levels for unsolved puzzles.
6. **Execution Time**: Display how long it takes to generate or solve each puzzle.

---

## The Original Project

This project is based on a tutorial by [Sharnav's Tech](https://www.youtube.com/@SharnavTech), which demonstrated how to solve Sudoku using the Backtracking Algorithm and included a basic Tkinter GUI.

You can view the original project here:  
[Sudoku Solver in Python - Sharnav's Tech](https://www.youtube.com/watch?v=xAXmfZmC2SI)

---

## Modifications and Improvements

### 1. **Sudoku Puzzle Generator**

I added functionality to generate random Sudoku puzzles using the Backtracking Algorithm and the `random` module. The generator creates both solved and unsolved puzzles, ensuring that each puzzle is unique.

### 2. **Difficulty Levels**

The unsolved puzzles can be generated at four levels of difficulty:
- **Easy**: 34 empty cells
- **Medium**: 44 empty cells
- **Hard**: 54 empty cells
- **Expert**: 64 empty cells

This makes the program more engaging and showcases how the Backtracking Algorithm performs across different levels of complexity.

### 3. **Execution Time Display**

I incorporated the `time` module to measure the execution time for solving and generating Sudoku puzzles. This feature helps users understand the performance of the algorithm, especially when working with puzzles of different difficulty levels.

Execution time is shown in milliseconds, allowing users to see how fast or slow the Backtracking Algorithm solves or generates a puzzle based on the number of empty cells and the randomness of the puzzle.

![Execution Time Example](https://user-images.githubusercontent.com/95155301/219746921-28f50551-b5d2-49fe-8f63-d6ae0c16a915.png)

### 4. **Enhanced Tkinter GUI**

The GUI has been improved for a more polished user experience:
- Added background images for visual appeal.
- New buttons for generating puzzles and selecting difficulty levels.
- A label to display the execution time for solving and generating puzzles.
- Cleaner layout for better usability.

---

## Installation and Usage

### Prerequisites
- Python 3.x
- `tkinter` (should be included with Python)

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/sudoku-generator-solver.git
cd sudoku-generator-solver
```

Install any required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Program

Run the `sudoku.py` file to launch the program:

```bash
python sudoku.py
```

### Controls

- **Input Puzzle**: Manually enter numbers on the Sudoku grid.
- **Solve Puzzle**: Click the "Solve" button to solve the current board.
- **Clear Board**: Click the "Clear" button to reset the board.
- **Generate Solved Puzzle**: Click "Generate Solved Puzzle" to create a fully solved Sudoku board.
- **Generate Unsolved Puzzle**: Select a difficulty level (Easy, Medium, Hard, Expert) to generate a new Sudoku puzzle with missing cells.

---

## Acknowledgments

- The original concept and code were derived from [Sharnav's Tech](https://www.youtube.com/@SharnavTech) on YouTube.
- Modifications were made to add features for generating puzzles, introducing difficulty levels, improving the GUI, and displaying execution time for educational purposes.

For more details, you can check out the related tutorial:  
[How to Solve Sudoku using Python](https://www.youtube.com/watch?v=xAXmfZmC2SI)

--- 

Feel free to contribute to this project by submitting issues or pull requests.