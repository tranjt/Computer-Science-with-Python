# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 02:48:18 2017

@author: Zun
"""

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


print(Square(-10))