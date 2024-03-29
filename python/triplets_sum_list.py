"""
Write a function that takes in a list of unique integers an an integer represtenting a target sum. This sum should find
all triplets that add up to the target sum.
Sample Input:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15
Sample Output: [[ 2, 3 , 10], [6, 4, 5]]
"""
import unittest


def find_triplets(nums: list[int], target: int) -> list[list[int]]:
    triplets = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    triplets.append([nums[i], nums[j], nums[k]])
    return triplets

"""
Inefficient solution
Time Complexity: O(n^3)
"""


def three_number_sum(array, target_sum):
    array.sort()
    result = []

    for i in range(len(array)):
        two_sum(array, i, result, target_sum)
    return result


def two_sum(array, idx, result, target_sum):
    left, right = idx+1, len(array) - 1
    while left < right:
        if array[idx] + array[left] + array[right] < target_sum:
            left += 1
        elif array[idx] + array[left] + array[right] > target_sum:
            right -= 1
        else:
            result.append([array[idx], array[left], array[right]])
            left += 1
    return result

"""
Three number sum uses pointers and is more efficient
Time Complexity: O(n^2)
"""

class test_three_number_sum(unittest.TestCase):
    def test_three_number_sum(self):
        self.assertEqual(three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15), [[1, 4, 10], [1, 5, 9], [1, 6, 8], [2, 3, 10], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 4, 8], [3, 5, 7], [4, 5, 6]])
        self.assertEqual(find_triplets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15), [[1, 4, 10], [1, 5, 9], [1, 6, 8], [2, 3, 10], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 4, 8], [3, 5, 7], [4, 5, 6]])



if __name__ == '__main__':
    unittest.main()