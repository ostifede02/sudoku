import numpy as np
import os
from sudoku_levels import levels


class SudokuGame():
    def __init__(self, level):
        self.set_level(level)

        self.row_input = None
        self.row_index = None

        self.col_input = None
        self.col_index = None
        self.num = None

        self.log_info = None


    def set_level(self, level):
        self.root_matrix_ = np.copy(levels[level])
        self.game_matrix_ = np.copy(levels[level])
        return


    # display the matrix on terminal
    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')    # clear the terminal
        print("##### SUDOKU the game #####\n")
        if self.log_info is not None:   # if there has been an exception
            self.print_log_info()
            self.log_info = None

        # *****  display game board   *****
        print("    1 2 3   4 5 6   7 8 9")
        print("  -------- ------- --------")
        rows = "ABCDEFGHI"
        for i, row in enumerate(self.game_matrix_):
            if i % 3 == 0 and i > 0:
                print("  -------- ------- --------")
            print(rows[i], "|", end=" ")
            for j, num in enumerate(row):
                if j % 3 == 0 and j > 0:
                    print("|", end=" ")
                if num != 0:
                    print(num, end=" ")
                else:
                    print(" ", end=" ")
            print("|")
        print("  -------- ------- --------\n")
        return
    

    def print_log_info(self):
        print(self.log_info)
        return
    

    def get_user_input(self):
        self.row_input = input("input row [A-I]: ")
        self.col_input = input("input col [1-9]: ")
        self.num = input("input number [1-9]: ")

    
    def is_valid_input(self):
        valid_rows = "ABCDEFGHI"
        valid_cols = "123456789"
        valid_nums = "0123456789"

        if self.row_input not in valid_rows or self.row_input is None:
            self.log_info = "[ERROR!] [Invalid input] Please enter a valid value for row.\n"
            return False
        elif self.col_input not in valid_cols or self.col_input is None:
            self.log_info = "[ERROR!] [Invalid input] Please enter a valid value for col.\n"
            return False
        elif self.num not in valid_nums or self.row_input is None:
            self.log_info = "[ERROR!] [Invalid input] Please enter a valid value for number.\n"
            return False
        elif int(self.num) > 9 or int(self.num) < 0:
            self.log_info = "[ERROR!] [Invalid input] Please enter a valid value for number.\n"
            return False
        
        # the user can't change the value of the root matrix
        self.row_index = int(ord(self.row_input) - ord("A"))
        self.col_index = int(self.col_input) - 1 
        if self.root_matrix_[self.row_index][self.col_index] != 0:
            self.log_info = "[ERROR!] [Invalid input] Selected cell is immutable.\n"
            return False
        
        # OK! the input is valid
        return True
    

    def update_matrix(self):
        # the value is valid, we can add the value to the matrix
        self.game_matrix_[self.row_index][self.col_index] = int(self.num)
        return
    
    
    def is_matrix_full(self):
        # if the user has filled in all the digits -> we can then proceed to check the solution
        for row in self.game_matrix_:
            if 0 in row:
                return False
        return True
    

    def is_solution_correct(self):
        # Check rows
        for row_index, row in enumerate(self.game_matrix_):
            # if all the digits are different, the total possibilities are 9
            if len(np.unique(row)) < 9:
                self.log_info = f"[ERROR!] [Incorrect solution] Please double-check row {row_index+1}.\n"
                return False


        # Check columns
        for col in range(9):
            column = [self.game_matrix_[row][col] for row in range(9)]
            # if all the digits are different, the total possibilities are 9
            if len(np.unique(column)) < 9:
                self.log_info = f"[ERROR!] [Incorrect solution] Please double check the col {col+1}.\n"
                return False

        # Check 3x3 subgrids
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                subgrid = [self.game_matrix_[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3)]
                if len(np.unique(subgrid)) < 9:
                    self.log_info = f"[ERROR!] [Incorrect solution] Please double check the subgrid ({(row_start//3)+1}, {(col_start//3)+1}).\n"
                    return False
        
        self.log_info = f"[INFO] Congratulations! You have solved the Sudoku!"
        return True
