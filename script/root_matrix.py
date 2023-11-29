import numpy as np

root_matrix_A = np.array([  0, 2, 0,    0, 0, 4,    3, 0, 0  ])
root_matrix_B = np.array([  9, 0, 0,    0, 2, 0,    0, 0, 8  ])
root_matrix_C = np.array([  0, 0, 0,    6, 0, 9,    0, 5, 0  ])

root_matrix_D = np.array([  0, 0, 0,    0, 0, 0,    0, 0, 1  ])
root_matrix_E = np.array([  0, 7, 2,    5, 0, 3,    6, 8, 0  ])
root_matrix_F = np.array([  6, 0, 0,    0, 0, 0,    0, 0, 0  ])

root_matrix_G = np.array([  0, 8, 0,    2, 0, 5,    0, 0, 0  ])
root_matrix_H = np.array([  1, 0, 0,    0, 9, 0,    0, 0, 3  ])
root_matrix_I = np.array([  0, 0, 9,    8, 0, 0,    0, 6, 0  ])

root_matrix = np.array([root_matrix_A, root_matrix_B, root_matrix_C, 
                        root_matrix_D, root_matrix_E, root_matrix_F,
                        root_matrix_G, root_matrix_H, root_matrix_I])
