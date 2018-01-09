# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:51:51 2018

@author: jcy
"""

import numpy as np 

A=np.arange(12).reshape((3,4))
print(A)

print(np.split(A,3,axis=0))

print(np.vsplit(A,3))

print(np.hsplit(A,2))