"""
Write an asynchronous function async_factorial(n) that takes a non-negative integer n as input and returns the factorial of n.

Your function should use the asyncio library to perform the computation in an asynchronous way.

"""

import asyncio
import tracemalloc
import unittest


tracemalloc.start()

async def async_sum(numbers):
    total = 0
    for n in numbers:
        await asyncio.sleep(0.1)
        total += n
    return total


async def async_factorial(n):
    if n == 0:
        return 1
    else:
        await asyncio.sleep(0.1)
        return n * await async_factorial(n - 1)


def run_async(test_func):
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(test_func(*args, **kwargs))
        loop.close()
    return wrapper


class TestAsyncFactorial(unittest.TestCase):
    @run_async
    async def test_factorial(self):
        tasks = []
        for _ in range(10):
            tasks.append(asyncio.create_task(async_sum([1, 2, 3])))
            tasks.append(asyncio.create_task(async_factorial(5)))
            tasks.append(asyncio.create_task(asyncio.sleep(0.05)))  # add other tasks
        await asyncio.gather(*tasks)
        self.assertEqual(await async_factorial(5), 120)
        self.assertEqual(await async_sum([1, 2, 3]), 6)


if __name__ == '__main__':
    unittest.main()

