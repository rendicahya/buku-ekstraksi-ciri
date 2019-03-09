import numpy as np

data = np.array([[2, 3, 1, 1, 8],
                 [4, 5, 0, 0, 2],
                 [5, 8, 4, 1, 3],
                 [7, 8, 1, 1, 8],
                 [2, 7, 9, 9, 0]])

print(np.where(data == 9))
