from sudoku import SudokuGame


# states
DISPLAY             = "state1"
GET_INPUT           = "state2"
UPDATE_MATRIX       = "state3"
CHECK_SOLUTION      = "state4"
SELECT_LEVEL        = "state5"


def main():
    game = SudokuGame()
    game.clear_terminal()
    
    state = SELECT_LEVEL
    level = input("Enter the level: [type --help for more info.]  ")
    
    while True:
        # *********** select the level ***********
        if state == SELECT_LEVEL:
            if level == "--help":
                print("Choose one of the following levels:")
                print("- type 'e' for the easy level")
                print("- type 'i' for the intermediate level")
                print("- type 'd' for the difficult level")
                level = input()
                continue

            elif level is None or level not in "eid":
                print("[ERROR] Please enter a valid input.")
                level = "--help"
                continue
        
            game.set_level(level)
            state = DISPLAY


        # *********** display the grid ***********
        if state == DISPLAY:
            game.display()
            state = GET_INPUT


        # *********** get user input ***********
        if state == GET_INPUT:
            if game.get_user_input() is None:
                state = SELECT_LEVEL
                level = "--help"
                game.clear_terminal()
                continue

            if game.is_valid_input():
                state = UPDATE_MATRIX
            else:
                state = DISPLAY


        # *********** update the matrix ***********
        if state == UPDATE_MATRIX:
            game.update_matrix()
            if game.is_matrix_full():
                state = CHECK_SOLUTION
            else:
                state = DISPLAY


        # *********** check the solution ***********
        if state == CHECK_SOLUTION:
            if game.is_solution_correct():
                game.clear_terminal()
                game.print_log_info()
                break
            else:
                state = DISPLAY

    return


if __name__ == "__main__":
    main()