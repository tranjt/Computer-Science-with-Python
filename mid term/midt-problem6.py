# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 04:43:00 2017

@author: Zun
 Write a function that satisfies the following docstring:  
	
    largest_odd_times([2,2,4,4]) returns None
    largest_odd_times([3,9,5,3,5,3]) returns 9
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    
    numbers = {}
    
    # Make dict of all numbers found in list
    # key as the number and value as count of times it occurred in list
    for curNum in L:        
        numbers.setdefault(curNum, 0)
        numbers[curNum] = numbers[curNum] + 1    
    
    
    # make a list of numbers of values from numbers dictionary
    # sorted with the largest number first
    listKeys = list(numbers.keys())
    listKeys.sort()
    listKeys.reverse()    
    
    # return largest number that occurs odd number of times in L
    for num in listKeys:
        if numbers[num] % 2 != 0:
            return num
    
    
L = [2,2,4,4]
    
large = largest_odd_times(L)
print(large)