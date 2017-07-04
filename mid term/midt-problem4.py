# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 02:27:02 2017

@author: Zun

Write a function is_triangular that meets the specification below. 
A triangular number is a number obtained by the continued summation of integers starting from 1. 
For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers. 
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    triangularNumber = False
    tot = 0
    for currentNum in range(k+1):
        tot += currentNum       
        
        if tot == k:
            return True
        if tot > k:
            return False
    
    return triangularNumber


print("input 1: " + str(is_triangular(1)))

print("input 3: " + str(is_triangular(3)))
print("input 5: " + str(is_triangular(5)))
print("input 6: " + str(is_triangular(6)))


print("input 10: " + str(is_triangular(10)))

