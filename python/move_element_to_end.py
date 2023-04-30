"""
Write a function that takes in an array and an integer and mutates the array in place and puts all values that are equal to the target integer to the end of the array,
"""

import unittest

def move_to_end(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        while left <= right and arr[right] == target:
            right -= 1
        if arr[left] == target:
            #swap places if the array at the left index is equal to the target
            arr[left], arr[right] = arr[right], arr[left]
        left += 1
    return arr

class TestMoveToEnd(unittest.TestCase):
    def test_move_to_end(self):
        arr = [1, 2, 3, 4, 5, 6, 6, 5, 5, 5, 5]

        self.assertEqual(move_to_end(arr, 6), [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 6])



if __name__ == '__main__':
    unittest.main()
