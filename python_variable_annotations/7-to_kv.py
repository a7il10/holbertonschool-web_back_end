#!/usr/bin/env python3
'''
Python - Variable Annotations
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    takes a string and an int or float, and returns a tuple
    '''
    square = v ** 2
    return k, square
