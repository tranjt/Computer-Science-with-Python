# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 19:49:06 2017

@author: Zun

 Write a Python function that takes in two lists and calculates whether they are permutations of each other. The lists can contain both integers and strings. We define a permutation as follows:

    -the lists have the same number of elements
    -list elements appear the same number of times in both lists

If the lists are not permutations of each other, the function returns False.
If they are permutations of each other, the function returns a tuple consisting of the following elements:

    -the element occuring the most times
    -how many times that element occurs
    -the type of the element that occurs the most times

If both lists are empty return the tuple (None, None, None). If more than one element occurs the most number of times, you can return any of them.

For example,

    if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
    if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] then is_list_permutation returns (1, 3, <class 'int'>) 
	because the integer 1 occurs the most, 3 times, and the type of 1 is an integer (note that the third element in the tuple is not a string).
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # make sure length of both lists are the same return False if not
    if len(L1) != len(L2):
        return False   
    
    # handle case were both list are empty
    if len(L1) == len(L2) and len(L1) == 0:
        return (None, None, None)
    
    # make dict with key value pair where value is the number
    # of occures of an integers or a strings in a list
    def make_dict_of_list(L):
        tempDict = {}
        for item in L:
            tempDict.setdefault(item, 0)
            tempDict[item] = tempDict[item] + 1
        return tempDict            

    L1Dict = make_dict_of_list(L1)
    L2Dict = make_dict_of_list(L2)
    
    # Check if both dict are the same
    if L1Dict == L2Dict:      
        # get key for the largest value in dict
        largestValKey = max(L1Dict, key=L1Dict.get)        
        return (largestValKey, L1Dict[largestValKey], type(largestValKey))
    else:
        # Return false if both dict are not the same
        return False
    
    
    

L1 = [1, 'b', 1, 'c', 'c', 1] 
L2 = ['c', 1, 'b', 1, 1, 'c']

#L1 = []
#L2 = []
#L1 = ['a', 'a', 'b']
#L2 = ['a', 'b']
L1 = ["a"]
L2 = ["a"]
test = is_list_permutation(L1, L2)
print(test)