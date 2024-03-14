#!/usr/bin/env python3
'''
 returns a tuple
'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' returns tuple consisting of k and the square of v. '''
    return (k, v * v)
