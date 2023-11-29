import numpy as np


# ********************* LEVEL EASY **********************************

root_matrix_A1 = np.array([  0, 3, 1,    6, 7, 9,    5, 2, 8  ])
root_matrix_B1 = np.array([  9, 6, 7,    2, 5, 8,    3, 4, 1  ])
root_matrix_C1 = np.array([  5, 8, 2,    1, 4, 3,    9, 6, 7  ])

root_matrix_D1 = np.array([  6, 5, 9,    8, 1, 7,    2, 3, 4  ])
root_matrix_E1 = np.array([  3, 2, 8,    5, 6, 4,    1, 7, 9  ])
root_matrix_F1 = np.array([  7, 1, 4,    9, 3, 2,    8, 5, 6  ])

root_matrix_G1 = np.array([  8, 7, 3,    4, 2, 1,    6, 9, 5  ])
root_matrix_H1 = np.array([  1, 4, 5,    3, 9, 6,    7, 8, 2  ])
root_matrix_I1 = np.array([  2, 9, 6,    7, 8, 5,    4, 1, 3  ])

root_matrix1 = np.array([root_matrix_A1, root_matrix_B1, root_matrix_C1, 
                        root_matrix_D1, root_matrix_E1, root_matrix_F1,
                        root_matrix_G1, root_matrix_H1, root_matrix_I1])

# *******************************************************************


# ********************* LEVEL INTERMEDIATE **************************

root_matrix_A2 = np.array([  0, 3, 1,    6, 7, 0,    0, 2, 8  ])
root_matrix_B2 = np.array([  9, 0, 7,    0, 5, 8,    3, 4, 1  ])
root_matrix_C2 = np.array([  5, 8, 2,    1, 4, 0,    0, 6, 0  ])

root_matrix_D2 = np.array([  6, 0, 9,    8, 1, 0,    2, 3, 4  ])
root_matrix_E2 = np.array([  3, 0, 8,    0, 0, 4,    1, 0, 0  ])
root_matrix_F2 = np.array([  0, 1, 4,    9, 3, 2,    0, 5, 6  ])

root_matrix_G2 = np.array([  8, 7, 0,    4, 2, 1,    0, 9, 0  ])
root_matrix_H2 = np.array([  0, 4, 5,    3, 0, 6,    7, 8, 2  ])
root_matrix_I2 = np.array([  2, 9, 6,    7, 8, 0,    4, 0, 3  ])

root_matrix2 = np.array([root_matrix_A2, root_matrix_B2, root_matrix_C2, 
                        root_matrix_D2, root_matrix_E2, root_matrix_F2,
                        root_matrix_G2, root_matrix_H2, root_matrix_I2])

# *******************************************************************


# ********************* LEVEL DIFFICULT *****************************

root_matrix_A3 = np.array([  0, 2, 0,    0, 0, 4,    3, 0, 0  ])
root_matrix_B3 = np.array([  9, 0, 0,    0, 2, 0,    0, 0, 8  ])
root_matrix_C3 = np.array([  0, 0, 0,    6, 0, 9,    0, 5, 0  ])

root_matrix_D3 = np.array([  0, 0, 0,    0, 0, 0,    0, 0, 1  ])
root_matrix_E3 = np.array([  0, 7, 2,    5, 0, 3,    6, 8, 0  ])
root_matrix_F3 = np.array([  6, 0, 0,    0, 0, 0,    0, 0, 0  ])

root_matrix_G3 = np.array([  0, 8, 0,    2, 0, 5,    0, 0, 0  ])
root_matrix_H3 = np.array([  1, 0, 0,    0, 9, 0,    0, 0, 3  ])
root_matrix_I3 = np.array([  0, 0, 9,    8, 0, 0,    0, 6, 0  ])

root_matrix3 = np.array([root_matrix_A3, root_matrix_B3, root_matrix_C3, 
                        root_matrix_D3, root_matrix_E3, root_matrix_F3,
                        root_matrix_G3, root_matrix_H3, root_matrix_I3])

# *******************************************************************



levels = {
    "easy":         root_matrix1,
    "intermediate": root_matrix2,
    "difficult":    root_matrix3
}