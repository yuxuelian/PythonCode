#-*-coding:utf-8-*-
#迭代

#迭代列表
list1=["123",1,23,"1234","王开波","哈哈",1.2,True]
for temp in list1:
	print(temp)

#迭代字符串
str1="王开波wangkaibo"
for ch in str1:
	print(ch)

#如何判断一个对象是可迭代对象呢？
#方法是通过collections模块的Iterable类型判断
from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

#enumerate将列表转成--------------------
res=enumerate([1,"a","b",2])
print(res)
for i,value in res:
	print(i,value)

#for可以这样用
list3=[(1,2,3,4),(5,6,7,8),(9,10,11,12)]
for i,j,k,m in list3:
	print(i,j,k,m)

#列表生成
#从2到10  步长为2
list4=list(range(2,10,2))
print(list4)

range1=range(5,20,4)

list5=[]
for x in range1:
	list5.append(x*x)

print(list5)

#列出当前目录下的所有的文件和目录
import os
res=[d for d in os.listdir('.')]

print(res)

#简单遍历dict
d={"name":"王开波","age":18}
for k,v in d.items():
	print(k,'=',v)

#将list中的所有字符串变成小写
list6 = ['Hello', 'World', 'IBM', 'Apple']
list6=[s.lower() for s in list6]
print(list6)

list7= ['Hello', 'World', 18, 'Apple', None]
#这种情况不能像上面那样  由于包含整数

# 判断一个变量是不是字符串的方法
a="123"
b=1
print(isinstance(a,str))
print(isinstance(b,str))



























