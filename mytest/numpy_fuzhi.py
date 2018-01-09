# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:58:11 2018

@author: jcy
"""

import numpy as np

a=np.arange(4)

print(a)

b=a
c=a
d=b

a[0]=11

print(a)
print(b)
print(c)

print(b is a)

b=a.copy()#只是把a的值复制给b