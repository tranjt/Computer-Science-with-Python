# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 23:08:32 2017

@author: Zun
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. 
        
        cipher("abcd", "dcba", "dab") 
        returns (order of entries in dictionary may not be the same) 
        ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')"""    

    key_code = dict(zip(map_from, map_to))
    decoded = ""
    
    for letter in list(code):
        decoded += key_code[letter]
        
    return (key_code, decoded)



print (cipher("abcd", "dcba", "dab")) 