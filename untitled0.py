# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 23:16:31 2017

@author: Zun
"""

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname
    
    def get_staffnumber(self):
        return self.staffnumber

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber
    


#x = Person("Marge", "Simpson")
#y = Employee("Homer", "Simpson", "1007")

#print(x.Name())
#print(y.GetEmployee())
#print(y.get_staffnumber())

def some_function():
    for i in range(4):
        yield i

    def some_other():
        for i in range(6):
            yield i
    for i in some_other():
        yield i
    
for i in some_function():
    print(i)