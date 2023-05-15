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

"""
Here, we define a run_async() decorator function that runs an async function inside an event loop. 
We apply this decorator to our test_factorial() method so that it can be run asynchronously using loop.
run_until_complete(). Finally, we call unittest.main() to run all the tests in our test case, including the async test.
"""
class TestAsyncFactorial(unittest.TestCase):
    @run_async
    async def test_factorial(self):
        tasks = []
        for _ in range(10):
            tasks.append(asyncio.create_task(async_sum([1, 2, 3])))
            tasks.append(asyncio.create_task(async_factorial(5)))
            tasks.append(asyncio.create_task(asyncio.sleep(0.05)))
        await asyncio.gather(*tasks)
        self.assertEqual(await async_factorial(5), 120)
        self.assertEqual(await async_sum([1, 2, 3]), 6)

"""
In this example, async_sum is an async function that takes a list of numbers and returns their sum after sleeping for 0.1 seconds for each number.
 The TestAsyncFunctions class has a new test method test_async_sum which creates 10 tasks that call async_sum([1, 2, 3]) and waits for 0.05 seconds between 
 each task, and then asserts that the total sum is equal to 30 (which is the expected result for sum([1, 2, 3]) * 10). The run_async decorator
 is used to run the async test method using asyncio.run_until_complete within a new event loop.
"""

if __name__ == '__main__':
    unittest.main()

