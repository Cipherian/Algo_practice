"""
Write a function that takes in an array and an integer and mutates the array in place and puts all values that are equal to the target integer to the end of the array,
"""

def move_to_end(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        while left <= right and arr[right] == target:
            right -= 1
        if arr[left] == target:
            #swap places if the array at the left index is equal to the target
            arr[left], arr[right] = arr[right], arr[left]
        left += 1
    return arr

if __name__ == "__main__":
    print(move_to_end([1, 2, 3, 4, 5, 6, 2, 2, 2], 2)) # output: [1, 6, 3, 4, 5, 2, 2, 2, 2]