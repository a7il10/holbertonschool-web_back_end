#!/usr/bin/env python3
'''
Python - Variable Annotations
'''
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    This function takes a list of strings and returns a list of tuples.
    """

    return [(i, len(i)) for i in lst]
