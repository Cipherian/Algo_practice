"""
Challenge: Write a function that finds the three largest numbers in a list without sorting.
"""


def find_three_largest(lst):
    """
    :param lst: list of numbers
    :return: three largest numbers
    """
    return sorted(lst, reverse=True)[:3]


def find_three_largest_no_builtins(array):
    top_three = [None, None, None]
    for num in array:
        if top_three[2] is None or num > top_three[2]:
            top_three[0] = top_three[1]
            top_three[1] = top_three[2]
            top_three[2] = num
        elif top_three[1] is None or num > top_three[1]:
            top_three[0] = top_three[1]
            top_three[1] = num
        elif top_three[0] is None or num > top_three[0]:
            top_three[0] = num
    return top_three
