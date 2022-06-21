# to keep a reliable number of obstacles at 6dim i use 10

import random
full_triangle = [[1], [2, 7], [3, 8, 13], [4, 9, 14, 19], [5, 10, 15, 20, 25], [6, 11, 16, 21, 26, 31], [12, 17, 22, 27, 32], [18, 23, 28, 33], [24, 29, 34], [30, 35], [36]]
result = random.sample(range(1,36),10)
