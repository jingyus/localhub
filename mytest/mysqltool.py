# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 11:12:43 2017

@author: jcy
"""

import time, MySQLdb
     
#连接      
conn=MySQLdb.connect(host="ilovebcj.com",user="jcy",passwd="664550220b",db="test",charset="utf8")    
cursor = conn.cursor()      
print 'cursor',cursor   
#删除表  
#sql = "drop table if exists user"  
#cursor.execute(sql)  
 
#创建  
#sql = "create table if not exists user(name varchar(128) primary key, created int(10))"  
#cursor.execute(sql)  

#写入      
#sql = "insert into test_table(name,wtime) values(%s,%s)"    
#param = ("aaa",time.time())     
#n = cursor.execute(sql,param)
#print 'insert',n      
     
#写入多行      
#sql = "insert into test_table(name,wtime) values(%s,%s)"    
#param = (("bbb",time.time()), ("ccc",33), ("ddd",44) )  
#n = cursor.executemany(sql,param)      
#print 'insertmany',n      

#更新
#sql = "update test_table set name='zzz' where name='aaa'"
#param = ()
#n = cursor.execute(sql,param)
#print 'update',n

#查询  
n = cursor.execute("select * from test_table")
for row in cursor.fetchall():
    print row
    for r in row:
        print r

#删除
name="bbb"
print "name====",name
sql = "delete from test_table where name='%s'"%(name)
print "sql====",sql
param =()
n = cursor.execute(sql,param)  
print 'delete',n

#查询      
n = cursor.execute("select * from test_table")      
print cursor.fetchall()      
 
cursor.close()      
     
#提交      
conn.commit()  
#关闭 
conn.close()
     