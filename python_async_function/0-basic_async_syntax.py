#!/usr/bin/env python3
"""This module contains the wait_random function."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function waits for a random delay between 0 and
    max_delay (included) seconds.
    """

    # Generate a random delay between 0 and max_delay
    delay = random.uniform(0, max_delay)

    # Wait for the delay
    await asyncio.sleep(delay)

    # Return the actual delay
    return delay
