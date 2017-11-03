#-*-coding:utf-8-*-
'''
匿名函数
'''


def sum(x,y):
	return x+y

#等价于
mySum=lambda x,y:x+y


print(sum(1,2))
print(mySum(1,2))


#交换两个变量的值
#方法一

a=5
b=4
c=0

print("交换前")
print(a)
print(b)

c=a
a=b
b=c

print("交换后")
print(a)
print(b)


#方法二
a=5
b=4
print("交换前")
print(a)
print(b)
a=a+b
b=a-b
a=a-b

print("交换后")
print(a)
print(b)

#方法三   Python特有

a=5
b=4
print("交换前")
print(a)
print(b)
a,b=b,a
print("交换后")
print(a)
print(b)