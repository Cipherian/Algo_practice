"""
Write a function that takes in two non-empty lists of integers and finds the pair of numbers whose absolute difference
is closest to zero. Returns a list of those two numbers
"""


def smallest_difference(array_one, array_two):
    """
    :type array_one: 'list'
    :type array_two: 'list'
    :rtype: 'list'
    """
    array_one.sort()
    array_two.sort()
    difference = float('inf')
    smallest_pair = []
    i = j = 0
    # iterating through both lists, using pointers to avoid out of index errors
    while i < len(array_one) and j < len(array_two):
        curr_difference = abs(array_one[i] - array_two[j])
        if curr_difference < difference:
            difference = curr_difference
            smallest_pair = [array_one[i], array_two[j]]
        if array_one[i] < array_two[j]:
            i += 1
        else:
            j += 1
    return smallest_pair


if __name__ == '__main__':
    print(smallest_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [66, 11, 44, 22, 87, 66, 111, -111, -222, -55]))
    # [10, 11]
