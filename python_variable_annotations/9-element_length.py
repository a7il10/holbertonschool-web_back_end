#!/usr/bin/env python3
'''
Python - Variable Annotations
'''


def element_length(lst: List[float]) -> int:
    '''
    return values with the appropriate types
    '''
    return [(i, len(i)) for i in lst]
