# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:43:37 2017

@author: Zun
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    largestAnimalCount = len(max(aDict.values()))
    print(largestAnimalCount)
    biggest = []
    
    for animals in aDict:
        if len(aDict[animals]) == largestAnimalCount:
            biggest.append(animals)
        return biggest
    
print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}))

