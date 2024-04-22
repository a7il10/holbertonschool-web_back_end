#!/usr/bin/env python3
'''
Python - Variable Annotations
'''
from typing import list, Union


def sum_mixed_list(mxd_lst: list[union[int, float]]) -> float:
    '''list of integers and floats and returns their sum'''
    return sum(mxd_lst)
