"""
Problem 1
You are given a list of integers, where each element represents the maximum number of steps that can be jumped going forward from that element. Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the list.
For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 1 to 5, and then from 5 to 9.
"""

def minimum_jumps(lst):
    if not lst:
        return 0
    n = len(lst)
    if n == 1:
        return 0
    jumps = [float('inf')] * n
    jumps[0] = 0
    for i in range(1, n):
        for j in range(i):
            if i <= j + lst[j] and jumps[j] != float('inf'):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    print(jumps[-1])

"""
The main idea is to iterate over the list and, for each element, consider all the elements that can jump to it and choose the one that required the minimum number of jumps to reach it. We can then update the minimum number of jumps required to reach the current element by adding 1 to the minimum number of jumps required to reach the element that can jump to it.
For example, consider the list [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]. We can start by initializing an array jumps with the minimum number of jumps required to reach each element, initialized to infinity. Then we can iterate over the list and update the jumps array as follows:

At the first element (index 0), the minimum number of jumps is 0. So jumps becomes [0, inf, inf, inf, inf, inf, inf, inf, inf, inf].
At the second element (index 1), we can jump from the first element (which requires 0 jumps). So the minimum number of jumps to reach the second element is 1. jumps becomes [0, 1, inf, inf, inf, inf, inf, inf, inf, inf].
At the third element (index 2), we can jump from the second element (which requires 1 jump) or the first element (which also requires 1 jump). In either case, the minimum number of jumps to reach the third element is 2. jumps becomes [0, 1, 2, inf, inf, inf, inf, inf, inf, inf].
At the fourth element (index 3), we cannot jump from any of the previous elements because the maximum number of steps that can be jumped from the fourth element is 0. So the minimum number of jumps remains inf. jumps becomes [0, 1, 2, inf, inf, inf, inf, inf, inf, inf].
This process continues until we reach the end of the list. The final value of jumps[-1] is the minimum number of jumps required to reach the end of the list.
"""


# minimum_jumps([6, 2, 4, 0, 5, 1, 1, 4, 2, 9])
# minimum_jumps([1, 1, 1, 1])
# minimum_jumps([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

"""
Problem 2
Implement a function smallest_subarray_with_given_sum(s: int, arr: List[int]) -> int that, given an integer s and a list of integers arr, finds the length of the smallest contiguous subarray of arr whose sum is greater than or equal to s. Return 0 if no such subarray exists.

For example, given the list [2, 1, 5, 2, 3, 2] and the integer 7, your function should return 2, because the smallest subarray with a sum greater than or equal to 7 is [5, 2].
    The list arr has at least one and at most 10^5 elements.
    Each element of arr is an integer in the range [-10^4, 10^4].
    The integer s is an integer in the range [1, 10^9].
"""

def smallest_subarray_with_given_sum(s:int, arr:list[int]) -> int:
    min_length = float('inf')
    left = 0
    sum_value = 0
    for num in range(len(arr)):
        sum_value += arr[num]
        while sum_value >= s:
            min_length = min(min_length, num - left + 1)
            sum_value -= arr[left]
            left += 1
    return min_length if min_length != float('inf') else 0

print(
    smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]),
    smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]),
    smallest_subarray_with_given_sum(7, [2, 1, 1, 1, 1, 1, 1, 1])
)

"""
This solution uses a sliding window approach to find the smallest contiguous subarray with a sum greater than or equal to s.

The idea is to keep a sliding window that starts at the beginning of the list and moves towards the end. The window is represented by the variables left and right, which represent the indices of the first and last elements of the window, respectively.

At each step, we increment the value of right and add the element at index right to the sum of the elements in the window. Then, we check if the sum is greater than or equal to s. If it is, we update the minimum length of the subarray and shrink the window by incrementing left and subtracting the element at index left from the sum. We repeat this process until the sum is less than s.

Finally, we return the minimum length of the subarray, or 0 if no subarray with a sum greater than or equal to s was found.
"""

"""
Problem 3

Implement a function intersection(linked_list_1, linked_list_2) that returns the node at which the intersection of two singly linked lists begins, or None if there is no such intersection.

For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
"""

class ListNode(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


def intersection(ll1, ll2):
    if not ll1 or not ll2:
        return None
    # Use a dictionary to store the visited nodes in ll1
    visited = {}

    current = ll1
    while current:
        visited[current.value] = True
        current = current.next

    # Check if each node in ll2 has been visited
    current = ll2
    while current:
        if current.value in visited:
            return current
        current = current.next

    # If no intersection was found, return None
    return None

# linked_list_1 = ListNode(4)
# linked_list_1.next = ListNode(5)
# linked_list_1.next.next = ListNode(6)
# linked_list_1.next.next.next = ListNode(7)
#
# linked_list_2 = ListNode(1)
# linked_list_2.next = ListNode(2)
# linked_list_2.next.next = ListNode(3)
# linked_list_2.next.next.next = ListNode(4)
#
# print(intersection(linked_list_1, linked_list_2))

"""
Implement a function sort_two_arrays(arr1: List[int], arr2: List[int]) -> List[int] that, given two lists of integers arr1 and arr2, returns a new sorted list containing all the elements of both lists.

The function should not use the built-in sort function or any other sorting algorithm. You may use the pop and insert functions to manipulate the lists, but you should not use any other built-in functions or libraries.

For example, given the lists [3, 2, 1] and [4, 5, 6], your function should return [1, 2, 3, 4, 5, 6].
"""

def sort_two_arrays(arr1:list[int], arr2: list[int]) -> list[int]:
    unsorted_result = arr1 + arr2

    def quicksort(lst: list) -> list:
        if not lst:
            return []
        pivot = lst[0]
        left = [x for x in lst[1:] if x < pivot]
        right = [x for x in lst[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

    return quicksort(unsorted_result)


print(sort_two_arrays([1,2,3], [4,5,6]))
