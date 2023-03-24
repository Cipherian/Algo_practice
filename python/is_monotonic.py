"""
Write a function that takes in an array and determines whether the array is monotonic.
"""

def is_monotonic(arr):
    if len(arr) <= 1:
        return True
    if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        return True
    elif all(arr[i] >= arr[i+1] for i in range(len(arr)-1)):
        return True
    return False


if __name__ == "__main__":
    print(is_monotonic([1, 2, 3, 4, 5])) # True
    print(is_monotonic([1, 2, 6, 4, 5, 6])) # False