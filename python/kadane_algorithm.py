"""
Write a function that takes in an array of integers and returns the maximum sum that can be obtained by summing up all the integers in a non-empty array.
A sub-array must be contiguous in the array(only containing adjacent numbers). Implement Kadane's algorithm.
"""

def max_sum_sub_array(lst) -> int:
    """
    :type lst: List[int]
    :rtype: int
    """
    max_sum:int = float('-inf')
    current_sum:int = 0
    
    for num in lst:
        current_sum += num
        # reassign max_sum if current_sum > max_sum
        max_sum = max(max_sum, current_sum)
        current_sum = max(current_sum, 0)

    return max_sum


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6, -5, -4, -3, -2, -1] # 21

    print(max_sum_sub_array(test_list))