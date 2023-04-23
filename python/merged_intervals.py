"""
Write a function that takes in a nested list of intervals and merges any overlapping intervals.
Sample input [[1, 2], [2, 5], [6, 7]] output: [[1, 5], [6, 7]]
"""

def merge_intervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x: x[0])
    merged_intervals = []
    current_interval = intervals[0]
    for interval in intervals[1:]:
        if current_interval[1] < interval[0]:
            merged_intervals.append(current_interval)
            current_interval = interval
        else:
            current_interval[1] = max(current_interval[1], interval[1])
    merged_intervals.append(current_interval)
    return merged_intervals

"""
The function merge_intervals takes a list of intervals represented as lists of two integers and returns a new list of merged intervals where overlapping intervals are combined into a single interval.

The function first sorts the input intervals based on their start times using the sort method and a lambda function.

It then initializes an empty list called merged_intervals and a variable called current_interval to the first interval in the sorted list.

The function then loops through the remaining intervals in the list and checks if the current interval overlaps with the next interval. If there is no overlap, the current interval is added to the merged_intervals list and the current interval is updated to the next interval. If there is an overlap, the function updates the end time of the current interval to the maximum of its current end time and the end time of the next interval.

Finally, the last interval is added to the merged_intervals list and the merged list is returned.
"""
if __name__ == '__main__':
    print(merge_intervals([[1, 2], [2, 5], [6, 7]])) # [[1, 5], [6, 7]]
    print(merge_intervals([[1, 2], [2, 5], [6, 7], [7, 10]])) # [[1, 5], [6, 10]


