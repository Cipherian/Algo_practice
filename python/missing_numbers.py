"""
You are given an unordered list of unique integers in the range of [1, n] where n represents the length of nums + 2. Write a function
that takes in this list and returns a new list with the new missing numbers.
input: nums = [1, 3, 4]
output: [2, 5]
"""
import unittest

def missing_numbers(nums):
    n = len(nums) + 2
    num_set = set(nums)
    return [num for num in range(1, n + 1) if num not in num_set]


class TestMissingNumbers(unittest.TestCase):
    def test_missing_numbers(self):
        self.assertEqual(missing_numbers([1, 3, 4]), [2, 5])
        self.assertEqual(missing_numbers([1, 2, 4, 5, 6, 7, 8, 10]), [3, 9])


if __name__ == '__main__':
    unittest.main()