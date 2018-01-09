# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 09:06:51 2018

@author: jcy
"""

import numpy as np

A=np.arange(3,15).reshape((3,4))
print(A)
print(A[1][1])

for row in A:
    print(row)
    
for column in A.T:
    print(column)

print(A.flatten())
for column in A.flat:
    print(column)
    
print("----------------------------------------")

A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]
#A=np.array([1,1,1])
#B=np.array([2,2,2])

C=np.vstack((A,B))
C2=np.hstack((A,B))
print(A.shape,C.shape)
print(C)
print(C2)
print("----------------------------------------")

print(A[:,np.newaxis])

C33=np.concatenate((A,B,B,A),axis=1)
print(C33)