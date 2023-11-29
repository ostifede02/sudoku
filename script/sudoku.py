import numpy as np
import os
import root_matrix as rm


class Sudoku():
    def __init__(self):
        self.root_matrix_ = rm.root_matrix
        self.game_matrix_ = rm.root_matrix

        self.row_input = None
        self.row_index = None
        self.col_input = None
        self.col_index = None
        self.num = None


    # display the matrix on terminal
    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("    1 2 3   4 5 6   7 8 9")
        print("  -------------------------")
        rows = "ABCDEFGHI"
        for i, row in enumerate(self.game_matrix_):
            if i % 3 == 0 and i > 0:
                print("  -------------------------")
            print(rows[i], "|", end=" ")
            for j, num in enumerate(row):
                if j % 3 == 0 and j > 0:
                    print("|", end=" ")
                if num != 0:
                    print(num, end=" ")
                else:
                    print(" ", end=" ")
            print("|")
        print("  -------------------------")
    

    def get_user_input(self):
        self.row_input = input("input row [A-I]: ")
        self.col_input = input("input col [1-9]: ")
        self.num = input("input number [1-9]: ")

    
    def is_valid_input(self):
        valid_rows = "ABCDEFGHI"
        valid_cols = "123456789"
        valid_nums = "123456789"

        if self.row not in valid_rows:
            print("[ERROR!] [Invalid input] Please enter valid values for row.")
            return False
        elif self.col not in valid_cols:
            print("[ERROR!] [Invalid input] Please enter valid values for col.")
            return False
        elif self.num not in valid_nums:
            print("[ERROR!] [Invalid input] Please enter valid values for number.")
            return False
        
        self.row_index = int(ord(self.row_input) - ord("A"))
        self.col_index = int(self.col_input) - 1 
        if self.root_matrix_[self.row_index][self.col_index] != 0:
            return False
        
        return True
    

    def add_num_to_matrix(self):
        self.game_matrix_[self.row_index][self.col_index] = int(self.num)
        return
    
    
    def is_matrix_full(self):
        for row in self.game_matrix_:
            if 0 in row:
                return False
        return True
    

    def is_solution_correct(self):
        # Check rows
        for row in self.game_matrix_:
            if len(np.unique(row)) < 9:
                return False

        # Check columns
        for col in range(9):
            column = [self.game_matrix_[row][col] for row in range(9)]
            if len(np.unique(column)) < 9:
                return False

        # Check 3x3 subgrids
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                subgrid = [self.game_matrix_[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3)]
                if len(np.unique(subgrid)) < 9:
                    return False
                
        return True
