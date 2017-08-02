# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:57:20 2017

@author: Zun
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    def flatten(nums):
        for i in nums:
            if isinstance(i, (list,tuple)):
                for j in flatten(i):
                    yield j
            else:
                yield i
                
    return max(flatten(t))



print(max_val((5, (1,2), [[1],[2]])))
print(max_val((5, (1,2), [[1],[9]])))