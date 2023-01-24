"""
Write a function that takes in a non empty array of integers that are sorted in
ascending order and returns a new array of the same length with the squares of the original integers also sorted in
ascending order
"""
# def sortedSquaredArray(array):
#     # Write your code here.
#     return sorted([idx**2 for idx in array])

def sorted_squares(arr:list[int]) -> list[int]:
    result = []
    left:int = 0
    right:int = len(arr) - 1
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result.append(arr[left] ** 2)
            left += 1
        else:
            result.append(arr[right] ** 2)
            right -= 1
    return result[::-1]

"""

Starting with the pointer pointing to the first element and the last element in the array, 
compare the absolute value of the elements at each pointer and add the square of the element
 with the smaller absolute value to the result array. Move the pointer of the element with the 
 smaller absolute value towards the center of the array until both pointers meet. 
 The result array will be in sorted order.
 The time complexity is O(n) compared to the first solution which is O(n log n)
 The space complexity is O(n) in both solutions
"""

if __name__ == "__main__":
    print(sorted_squares([1, 2, 3, 4, 5]))
    print(sorted_squares([1, 2, 5, 8, 9]))