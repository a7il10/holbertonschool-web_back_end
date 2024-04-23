#!/usr/bin/env python3
"""This module contains the task_wait_random function."""

import asyncio

# Import wait_random from 0-basic_async_syntax
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task that will wait for a random delay."""
    return asyncio.create_task(wait_random(max_delay))
