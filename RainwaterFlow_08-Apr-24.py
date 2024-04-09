# The grid below represents an island completely surrounded by water. 
# The numbers on the grid represent the elevation for the respective locations. 
# Write code to determine if rainwater would flow into the ocean when it rains at a given xy coordinate.
import random
import numpy as np

def willWaterFlowToTheOcean(matrix, x, y):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    def dfs(i, j):
        if (i, j) in visited:
            return False
        visited.add((i, j))
        # Check if the current cell is on the shore (ocean boundary)
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            return True
        # Explore neighboring cells
        neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for ni, nj in neighbors:
            if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] < matrix[i][j]:
                if dfs(ni, nj):
                    return True
        return False
    return dfs(x, y)

min_val, max_val = 0, 10
random_int_matrix = np.random.randint(min_val, max_val, size=(5, 5))

print('Used Matrix:')
print(random_int_matrix)
# Specify the row and column indices
row_index = np.random.randint(0,4)
col_index = np.random.randint(0,4)
# Retrieve the value at the specified indices
valueUsed = random_int_matrix[row_index][col_index]
print('Row Index:', row_index)
print('Col Index', col_index)
print('Value on Matrix: ',valueUsed)
print(willWaterFlowToTheOcean(random_int_matrix, row_index, col_index))  # Output: True
