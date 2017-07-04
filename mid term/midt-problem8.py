# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:53:47 2017

@author: Zun

Write a function called general_poly, that meets the specifications below. For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """    
    
    def polySum(x):
        tot = 0
        k = len(L) - 1
        for n in L:
            tot += n * (x**k)
            k -= 1
        return tot
    
    return polySum
    

L = [1, 2, 3, 4]


polySumFuc = general_poly(L)

total = polySumFuc(10)

print(total)