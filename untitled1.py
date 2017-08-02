# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:10:26 2017

@author: Zun
"""

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False


"""
L = [0, 1, 2, 3, 4, 5, 6]
print(search(L, 5))
print(newsearch(L, 5))
print(search(L, 8))
print(newsearch(L, 8))

print("List len 0")
L = []
print(search(L, 5))
print(newsearch(L, 5))
print(search(L, 8))
print(newsearch(L, 8))

print("List len 1")
L = [5]
print(search(L, 5))
print(newsearch(L, 5))
print(search(L, 8))
print(newsearch(L, 8))

print("List len 2")
L = [5, 6]
print(search(L, 5))
print(newsearch(L, 5))
print(search(L, 8))
print(newsearch(L, 8))
"""


def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    

L = [6, 5, 4, 3, 3, 2, 1, 0]
K = [1,  5 ]
J = [  5, 1 ]
swapSort(L)
L = [0,1, 2, 3, 4, 5, 6]
swapSort(L)

swapSort(K)
swapSort(J)
print("modded--------------")


def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
L = [0,1, 2, 3, 4, 5, 6]
modSwapSort(L)
L = [6, 5, 4, 3, 3, 2, 1, 0]
modSwapSort(L)
modSwapSort(K)
modSwapSort(J)

def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        print(n)
        answer *= n
        n -= 1
    return answer

def foo_two(n):
    """ Assume n is an int >= 0 """
    print(n)
    if n <= 1: 
        return 1.0
    else: 
        return n*foo_two(n-1)