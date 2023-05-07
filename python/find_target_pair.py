"""
You are given a list of numbers. Write a program that finds the two numbers in the list that add up to the target number.

For example, if the list is [2, 7, 11, 15] and the target number is 9, the program should return (2, 7).

Assume that there is exactly one solution and that the same number cannot be used twice.

"""

from typing import List, Tuple
import unittest

def find_pair(numbers: List[int], target: int) -> Tuple[int, int]:
    seen = {}
    for num in numbers:
        diff = target - num
        if diff in seen:
            return (diff, num)
        seen[num] = True
    return None

class TestFindPair(unittest.TestCase):
    def test_find_pair(self):
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(find_pair(numbers, target), (2, 7))

        numbers = [3, 5, 9, 2]
        target = 8
        self.assertEqual(find_pair(numbers, target), (3, 5))

        numbers = [1, 2, 3, 4, 5]
        target = 7
        self.assertEqual(find_pair(numbers, target), (3, 4))


if __name__ == '__main__':
    unittest.main()