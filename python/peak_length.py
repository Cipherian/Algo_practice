"""
Write a function that takes in an array and returns the length of the highest peak in the array. A peak is defined as a value that is greater than its neighbors and must be integers long.
Example: [1, 2 , 4 , 10, 2, 1, 0] forms a peak.
Example: [1, -1, 2, 4] there is no peak.
"""

def longest_peak(arr):
    arr_len = len(arr)
    max_peak = 0
    i = 1
    while i < arr_len - 1:
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            # found a peak
            peak_len = 1
            # expand to the left
            left = i - 1
            while left >= 0 and arr[left] < arr[left+1]:
                peak_len += 1
                left -= 1
            # expand to the right
            right = i + 1
            while right < arr_len and arr[right] < arr[right-1]:
                peak_len += 1
                right += 1
            # update max peak length
            max_peak = max(max_peak, peak_len)
            # skip the rest of the peak
            i = right
        else:
            # not a peak, continue iterating
            i += 1
    return max_peak


if __name__ == "__main__":
  print(longest_peak([1, 2, 4, 10, 2, 1, 0])) # 7
  print(longest_peak([1, -1, 2, 4])) # 0
  print(longest_peak([ 0, 1, 0])) # 3
