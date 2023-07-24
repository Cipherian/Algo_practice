"""
Given two non empty arrays of integers write a function that determines whether
the second array is a subsequence of the first one.
"""
import unittest


def is_subsequence(array, sequence):
    """
    :type array: List[int]
    :type sequence: List[int]
    :rtype: bool
    This function uses pointers i and j to iterate through the array and sequence. If the element of the array matches
    the sequence then the j pointer is incremented by 1. If the j pointer reaches the end of the sequence then the
    function returns True. If the i pointer reaches the end of the array without finding a match, then the function
    returns False.
    """
    i = 0
    j = 0
    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            j += 1
        i += 1
    return j == len(sequence)

class Test(unittest.TestCase):
    def test_is_subsequence(self):
        self.assertEqual(is_subsequence([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), True)
        self.assertEqual(is_subsequence([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]), False)
        self.assertEqual(is_subsequence([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]), False)
        self.assertEqual(is_subsequence([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7]), False)

if __name__ == "__main__":
    unittest.main()






