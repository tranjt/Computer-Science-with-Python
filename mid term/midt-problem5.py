# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 04:07:11 2017

@author: Zun
Write a Python function that takes in a string and prints out a version of 
this string that does not contain any vowels, according to the specification 
below. Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

For example, if s = "This is great!" 
then print_without_vowels will print Ths s grt!. If s = "a" 
then print_without_vowels will print the empty string . 


"""

def print_without_vowels(s):
    '''     
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''   
    
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U" ]
    
    listS = list(s)
    tempS = []
    for curChar in listS:
        if curChar not in vowels:
            tempS.append(curChar)
            
    print("".join(tempS))
    
    
print_without_vowels("aba")

