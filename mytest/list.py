# -*- coding: utf-8 -*-
"""
Created on Mon Jan 08 15:28:50 2018

@author: jcy
"""
#1
print "------------------1----------------------"
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [0,1, 2, 3, 4, 5, 6, 7 ];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

#2
print "------------------2----------------------"
list1 = ['physics', 'chemistry', 1997, 2000];

print list1;
del list1[2];
print "After deleting value at index 2 : "
print list1;

#3
print "------------------3----------------------"
L = ['Google', 'Runoob', 'Taobao']
print L[2]
print L[-2]
print L[1:]

#4
print "------------------4----------------------"
list_2d = [ [0 for i in range(5)] for i in range(5)]
print list_2d
print list_2d[0].append(3)
print list_2d[0].append(5)
print list_2d[2].append(7)
print list_2d
print range(5)