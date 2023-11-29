# Sudoku game
## rules
+ **Rows:** Each row must contain all the digits from 1 to 9 without repetition.

+ **Columns:** Each column must contain all the digits from 1 to 9 without repetition.

+ **Blocks:** Each of the nine 3x3 subgrids must contain all the digits from 1 to 9 without repetition.

![Sudoku Rules](utils/images/sudoku_rules.jpg)


## sript
### finite state machine
For this problem I structured the code with a finite state machine. The flow chart below shows how it has been done.

![Sudoku Rules](utils/images/flow_chart.png)

### class Sudoku
The class Sudoku contains all the methods and attributes to run the game. Each block of the chart above is described by a function within the class.

### levels
In addition the user can choose between three different difficulty levels:
+ easy (just to test the program)
+ intermediate
+ hard