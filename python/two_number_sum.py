
"""
Write a function that takes in a non empty array of distinct integers representing a target sum. If any two numbers in
the input array sum up to the target sum, the function should return them om am array in any order. If no two numbers
sum up to the target, the function should return an empty array.
"""
import unittest

def two_number_sum(array, target_sum):
    nums = {}
    for num in array:
        if target_sum - num in nums:
            return [num, target_sum - num]
        else:
            nums[num] = True
    return []

class TestTwoNumberSum(unittest.TestCase):
    def test_two_number_sum(self):
        self.assertEqual(two_number_sum([2, 7, 11, 15], 9), [7, 2])
        self.assertEqual(two_number_sum([2, 5, 11, 15], 16), [11, 5])
        self.assertEqual(two_number_sum([2, 7, 11, 15], 17), [15, 2])
        self.assertEqual(two_number_sum([2, 7, 11, 15], 18), [11, 7])
if __name__ == '__main__':
    unittest.main()