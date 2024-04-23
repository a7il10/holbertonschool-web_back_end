#!/usr/bin/env python3
"""This module contains the wait_random function."""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay."""
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    delays = []
    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
