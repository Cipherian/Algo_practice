"""
Daniel Brott
Write a function that returns the total amount of waiting time for all the queries, for example if you are given the
queries of durations [1, 4, 5], then the total waiting time if the queries were executed in the order of [5, 1, 4]
 would be (0 + 5), + (5 + 1) = 11.
"""


def total_waiting_time(queries: list[int]) -> int:
    queries.sort()
    total_time = 0
    for i in range(len(queries)):
        waiting_time = sum(queries[:i])
        total_time += waiting_time
    return total_time


if __name__ == "__main__":
    print(total_waiting_time([1, 4, 5]))
    print(total_waiting_time([5, 1, 4]))
    print(total_waiting_time([1, 2, 3, 4, 5]))
