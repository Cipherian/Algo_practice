"""
Write a function that takes in a list of integers and determines whether there is a sub array whose sum is equal to 0.
"""


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
