from tabulate import tabulate

# Sudoku Grid
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Functions
def draw_table(sudoku_grid):
    print(tabulate(sudoku_grid, tablefmt="fancy_grid"))

def empty_cells_exist():
    for i in range(9):
        for j in range(9):
            if sudoku_grid[i][j] == 0:
                return [i, j]
    return False

def checkNumber(num, i, j):
    # Vertical Check
    for row in range(9):
        if sudoku_grid[row][j] == num:
            return False
    
    # Horizontal Check
    for column in range(9):
        if sudoku_grid[i][column] == num:
            return False
    
    # Square Check
    start_row = (i // 3) * 3
    start_col = (j // 3) * 3

    for row in range(3):
        for col in range(3):
            if sudoku_grid[start_row + row][start_col + col] == num:
                return False

    return True

def solve_sudoku():
    empty_cell = empty_cells_exist()

    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if checkNumber(num, row, col):
            sudoku_grid[row][col] = num

            if solve_sudoku():
                return True

            sudoku_grid[row][col] = 0

    return False

# Solve Sudoku
solve_sudoku()

# Display the solved Sudoku
if solve_sudoku():
    draw_table(sudoku_grid)
    print("Solved!")
else:
    print("Cannot be solved. :(")