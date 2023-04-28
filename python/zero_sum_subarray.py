"""
Write a function that takes in a list of integers and determines whether there is a sub array whose sum is equal to 0.
"""
import unittest


def sub_array_sum_zero(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    # Exits in the case of one element whose value is zero: [0]
    if len(arr) == 0 and arr[0] == 0:
        return True
    
    total = 0
    seen = set()
    for num in arr:
        total += num
        if total in seen:
            return True
        seen.add(total)
    
    return False

class TestSubArraySumZero(unittest.TestCase):
    def test_sub_array_sum_zero(self):
        self.assertFalse(sub_array_sum_zero([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertFalse(sub_array_sum_zero([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
        self.assertTrue(sub_array_sum_zero([-4, 4, 0, 11]))


if __name__ == '__main__':
    unittest.main()