"""
Write a function that takes in a matrix of integers with the values of 0 and 1, if there are adjacent 1s, replace them with 0s. If there are any singular 1s, leave them alone. Return the
modified matrix.
"""
import unittest

def remove_islands(matrix):

    width = len(matrix[0])
    height = len(matrix)

    for i in range(height):
        for j in range(width):
            if (i > 0 and i < height - 1) and (j > 0 and j < width - 1):
                continue
            traverse_islands(matrix, i, j, True)
    for i in range(1, height):
        for j in range(1, width):
            traverse_islands(matrix, i, j, False)

    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 2:
                matrix[i][j] = 1
                
    return matrix

def traverse_islands(matrix, i, j, is_edge):
    if matrix[i][j] != 1:
        return
    if is_edge:
        matrix[i][j] = 2
    else:
        matrix[i][j] = 0

    if i > 0:
        traverse_islands(matrix, i - 1, j, is_edge)
    if j > 0: 
        traverse_islands(matrix, i, j - 1, is_edge)
    if i < len(matrix) - 1:
        traverse_islands(matrix, i + 1, j, is_edge)
    if j < len(matrix[0]) - 1:
        traverse_islands(matrix, i, j + 1, is_edge)


class TestRemoveIslands(unittest.TestCase):
    def test_remove_islands(self):
        self.assertEqual(remove_islands([[1, 1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0]]), [[1, 1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0]])


if __name__ == '__main__':
    unittest.main()