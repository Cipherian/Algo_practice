"""
Write a function which takes in a matrix which contains only 0s and 1s, each 0 is land and 1 is a river. 
A river consists of any number of 1s that are horizontal or vertical, but not diagonal. 
Return an array with the size of all rivers found in the matrix.

Example: [[1, 1, 0, 0], 
          [0, 1, 0, 0]]  -> [3]
"""
import unittest
def river_sizes(matrix):
    sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                size = find_river_sizes(matrix, i, j)
                sizes.append(size)

    return sizes



def find_river_sizes(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
        return 0
    
    size = 1
    matrix[i][j] = 0
    size += find_river_sizes(matrix, i+1, j)
    size += find_river_sizes(matrix, i-1, j)
    size += find_river_sizes(matrix, i, j+1)
    size += find_river_sizes(matrix, i, j-1)
    return size

class TestRiverSizes(unittest.TestCase):
    def test_river_sizes(self):
        self.assertEqual(river_sizes([[1, 1, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1]]), [6, 1])
        self.assertNotEqual(river_sizes([[1, 1, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1]]), [2, 2])


if __name__ == '__main__':
    unittest.main()
