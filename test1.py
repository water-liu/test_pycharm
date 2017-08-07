#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""a test module"""

# __author__ = 'water-liu'

import functools
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world!')
    elif len(args) == 2:
        print('Hello, %s!') % args
    else:
        print('Too many arguments')

max2 = functools.partial(max, 10)
print(max2(1, 3, 4, 5))
if __name__ == '__main__':
    test()

