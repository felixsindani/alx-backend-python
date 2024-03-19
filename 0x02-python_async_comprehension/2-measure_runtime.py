#!/usr/bin/env python3
"""coroutine that measure Run time for four parallel comprehensions"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - function execute async_com 4 times in parallel
    Arguments:
        nothing
    Returns:
        total runtime of task
    """
    t_start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    t_end = time.perf_counter()
    return (t_end - t_start)
