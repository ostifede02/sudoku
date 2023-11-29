from sudoku import SudokuGame


# *** CHOOSE THE LEVEL DIFFICULTY ***
# "easy" (solution: [A, 1] = 4)
# "intermediate"
# "difficult"
game = SudokuGame("difficult")

# states
DISPLAY             = "state1"
GET_INPUT           = "state2"
UPDATE_MATRIX       = "state3"
CHECK_SOLUTION      = "state4"


def main():
    state = DISPLAY
    
    while True:
        if state == DISPLAY:
            game.display()
            state = GET_INPUT

        if state == GET_INPUT:
            game.get_user_input()
            
            if game.is_valid_input():
                state = UPDATE_MATRIX
            else:
                state = DISPLAY
        
        if state == UPDATE_MATRIX:
            game.update_matrix()
            if game.is_matrix_full():
                state = CHECK_SOLUTION
            else:
                state = DISPLAY

        if state == CHECK_SOLUTION:
            if game.is_solution_correct():
                game.print_log_info()
                break
            else:
                state = DISPLAY



if __name__ == "__main__":
    main()