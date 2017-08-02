# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 00:01:34 2017

@author: Zun
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 23:27:39 2017

@author: Zun
"""

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
    
import copy
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals:
            self.vals[e] -= 1            

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        return self.vals.get(e, 0)
    
    def __add__(self, e):
        tempBag = copy.deepcopy(e)
        # combine all key value pair that exist in both dict
        for i in tempBag.vals.keys():
            if i in self.vals:
                tempBag.vals[i] = tempBag.vals[i] + self.vals[i]
        # add any key value pair only exist in self.vals to e.vals
        for j in self.vals.keys():
            if j not in tempBag.vals:
                tempBag.vals[j] = self.vals[j]                
        return tempBag
"""    
a = Bag()
a.insert(4)
a.insert(3)
b = Bag()
b.insert(4)
print(a+b)

prints

3:1
4:2
"""
a = Bag()
a.insert(4)
a.insert(3)
b = Bag()
b.insert(4)
print(a+b)

