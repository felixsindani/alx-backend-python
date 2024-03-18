#!/usr/bin/env python3
"""measure_time function that measure the total execution time of
for wait_n(n, max_delay), and returns total_time / n as float"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time of a function
    Args:
        n: the number of coroutines to launch
        max_delay: the maximum amount of time to wait for each coroutine
    Returns: elapsed total time in seconds
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
