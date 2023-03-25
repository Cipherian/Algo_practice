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


if __name__ == '__main__':
    print(merge_intervals([[1, 2], [2, 5], [6, 7]])) # [[1, 5], [6, 7]]
    print(merge_intervals([[1, 2], [2, 5], [6, 7], [7, 10]])) # [[1, 5], [6, 10]