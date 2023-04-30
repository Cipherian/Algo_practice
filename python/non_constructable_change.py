"""
Given an array of positive integers representing the values of coins in your possession, write a function that returns
the minimum amount of change that you cannot create. The given coins have a positive integer value and aren't necessarily
unique.
For example, if you're given coins = [1,2,5], the minimum amount of change that you can't create is 4, if you're given no
coins, the minimum amount of change that you can't create is 1.
"""
import unittest

def min_constant_change(coins):
    coins.sort()
    current_change = 0
    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin

    return current_change + 1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_constant_change([1, 2, 5]), 4)
        self.assertEqual(min_constant_change([100]), 1)
        self.assertEqual(min_constant_change([1, 2, 5, 10, 20]), 4)
        self.assertEqual(min_constant_change([1, 2, 5, 10, 20, 50]), 4)


if __name__ == "__main__":
    unittest.main()