"""
Given an array of positive integers representing the values of coins in your possession, write a function that returns
the minimum amount of change that you cannot create. The given coins have a positive integer value and aren't necessarily
unique.
For example, if you're given coins = [1,2,5], the minimum amount of change that you can't create is 4, if you're given no
coins, the minimum amount of change that you can't create is 1.
"""

def min_constant_change(coins):
    coins.sort()
    current_change = 0
    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin

    return current_change + 1


if __name__ == "__main__":
    print(min_constant_change([1, 2, 5]))
    print(min_constant_change([100]))
    print(min_constant_change([1, 2, 5, 10, 20]))
    print(min_constant_change([1, 2, 5, 10, 20, 50]))
    print(min_constant_change([1, 2, 33, 10, 20, 50, 100]))
    print(min_constant_change([1, 2, 5, 10, 20, 50, 100, 200]))