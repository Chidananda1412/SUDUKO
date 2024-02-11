import numpy as np

sudoku_puzzle = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

sudoku_solution = [[5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]]

def print_board(board):
    for row in board:
        print(row)

def possible(board, row, col, num):
    # Is the num appearing in the given row?
    if num in board[row]:
        return False

    # Is the num appearing in the given column?
    if num in [board[i][col] for i in range(9)]:
        return False

    # Is the num appearing in the given square?
    x0 = (col // 3) * 3
    y0 = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[y0+i][x0+j] == num:
                return False

    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if possible(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    global sudoku_puzzle
    global sudoku_solution
    print("Welcome to Sudoku!")
    print("Enter the Sudoku puzzle below (use '0' for empty cells):")
    print_board(sudoku_puzzle)

    # Ask the user to fill in the Sudoku puzzle
    for row in range(9):
        for col in range(9):
            while True:
                value = input(f"Enter value for row {row+1}, column {col+1}: ")
                if value.isdigit() and 0 <= int(value) <= 9:
                    sudoku_puzzle[row][col] = int(value)
                    break
                else:
                    print("Invalid entry! Please enter a number between 0 and 9.")

    print("Your Sudoku puzzle:")
    print_board(sudoku_puzzle)

    if solve(sudoku_puzzle) and sudoku_puzzle == sudoku_solution:
        print("Congratulations! You solved the Sudoku puzzle.")
    else:
        print("Sorry, the solution is incorrect. Here is the correct solution:")
        print_board(sudoku_solution)

if __name__ == "__main__":
    main()
