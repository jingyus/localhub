# -*- coding: utf-8 -*-
"""
Created on Mon Jan 08 14:38:09 2018

@author: jcy
"""

str = 'Hello World!'
 
print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print '\n'
print R'\n'

print str + "TEST"  # 输出连接的字符串

print "My name is %s and weight is %d kg!" % ('Zara', 21) 

hi = '''hi 
there'''
print 'hi:',hi

ustr = u'Hello\u0020World !'
print 'ustr:',ustr