# Two Number Sum

"""
Write a function that takes in a non empty array of distinct integers representing a target sum. If any two numbers in
the input array sum up to the target sum, the function should return them om am array in any order. If no two numbers
sum up to the target, the function should return an empty array.
"""
def two_number_sum(array, target_sum):
    nums = {}
    for num in array:
        if target_sum - num in nums:
            return [num, target_sum - num]
        else:
            nums[num] = True
    return []