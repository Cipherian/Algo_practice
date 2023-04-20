"""
Write a function that takes in an array of integers, each integer represents a jump to another index in the array. If the value is 3 then you move 3 indexes to the right, -3 moves 3 indexes to the left.
Return a boolean indicating whether or not all indices have been visited.
Example: array = [2, 3, 1, -4, -4, 2] -> true
"""
import unittest
def has_cycle(array:list) -> bool:
    n = len(array)
    visited = [False] * n
    idx = 0

    for _ in range(n):
        if visited[idx]:
            return False
        visited[idx] = True
        idx = (idx + array[idx]) % n
    return idx == 0
    
class Test(unittest.TestCase):
    def test_has_cycle(self):
        self.assertTrue(has_cycle([2, 3, 1, -4, -4, 2]), True)
        self.assertFalse(has_cycle([2, 3, 1, -4, 6, 2]), False)
        self.assertTrue(has_cycle([1]), True)

if __name__ == '__main__':
    unittest.main()