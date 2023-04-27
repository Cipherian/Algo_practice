"""
Write a function that takes in an array and determines whether the array is monotonic.
"""
import unittest

def is_monotonic(arr):
    if len(arr) <= 1:
        return True
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        return True
    elif all(arr[i] >= arr[i+1] for i in range(len(arr)-1)):
        return True
    return False

"""
This code defines a function named is_monotonic that takes an array arr as input and checks if the array is monotonic, i.e., if it is either entirely non-increasing or entirely non-decreasing.

The function first checks if the length of the array is less than or equal to 1. If so, it returns True, as an array with only one element is considered to be monotonic.

If the array has more than one element, the function checks if all the elements in the array are in non-decreasing order. To do this, it uses the all function in combination with a generator expression that checks if each element arr[i] is less than or equal to the next element arr[i+1] for all valid i. If all the elements are in non-decreasing order, the function returns True.

If the first check fails, the function then checks if all the elements in the array are in non-increasing order. It does this by again using the all function with a similar generator expression that checks if each element arr[i] is greater than or equal to the next element arr[i+1] for all valid i. If all the elements are in non-increasing order, the function returns True.

If both checks fail, the function returns False, indicating that the array is not monotonic.
"""

class TestIsMonotonic(unittest.TestCase):
    def test_is_monotonic(self):
        self.assertEqual(is_monotonic([1, 2, 3, 4, 5]), True)
        self.assertEqual(is_monotonic([1, 2, 6, 4, 5, 6]), False)
        
if __name__ == "__main__":
    unittest.main()