# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:00:35 2017

    Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary.
	The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. 
	The value for a key in the inverse dictionary is a sorted list (increasing order) of all keys in d that have the same value in d. 

    If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
    If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
    If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
"""



def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    invertDict = {}
    sortedKeys = list(d.keys())    
    sortedKeys.sort()    
    
    # loop thought each key in dictionary d    
    for key in sortedKeys:
        # create new key for current value d(key) 
        # inital value is empty list
        invertDict.setdefault(d[key], [])
        # add current key as value to invertDict with d(key) as key        
        # new values added to certain key by append to existing value list               
        invertDict[d[key]].append(key)
        
    return invertDict
    
d =  {1:10, 2:20, 3:30}
d =  {4:True, 2:True, 0:True}
d = {8: 6, 2: 6, 4: 6, 6: 6}
temp = dict_invert(d)

print(temp)
