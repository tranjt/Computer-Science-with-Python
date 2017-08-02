# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:36:24 2017

@author: Zun
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    sum = 0
    noDigit = True
    for i in range(len(s)):
        try:            
            sum += int(s[i])                        
            noDigit = False
        except ValueError:            
            pass  # it was a string, not an int.    
    
    if noDigit:
        raise ValueError("No digits in string")
    return sum
            

print(sum_digits("a;35d4"))
print(sum_digits("a;d1"))
print(sum_digits("a;d1"))
