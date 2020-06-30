#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:59:18 2020

@author: pi
"""

import matplotlib.pyplot as plt
plt.plot(range(10),'0')


def hello(name):
    """Given an object 'name', print 'Hello ' and the object."""
    print("Hello {}".format(name))


i = 42
if __name__ == "__main__":
    hello(i)
    
    
    def average(a, b):
        
        return (a + b) * 0.5