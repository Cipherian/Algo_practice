"""
Daniel Brott
Write a function that returns the total amount of waiting time for all the queries, for example if you are given the
queries of durations [1, 4, 5], then the total waiting time if the queries were executed in the order of [5, 1, 4]
 would be (0 + 5), + (5 + 1) = 11.
"""
import unittest

def total_waiting_time(queries: list[int]) -> int:
    queries.sort()  # sorts the queries in ascending order
    total_time = 0
    for i in range(len(queries)):
        waiting_time = sum(queries[:i])  # summing up the waiting time of the first i elements
        total_time += waiting_time  # adding the waiting time to the total time
    return total_time

class TestTotalWaitingTime(unittest.TestCase):
    def test_total_waiting_time(self):
        self.assertEqual(total_waiting_time([1, 4, 5]), 6)
        self.assertEqual(total_waiting_time([1, 3, 4]), 5)

if __name__ == "__main__":
    unittest.main()

