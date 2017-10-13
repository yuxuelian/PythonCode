#-*-coding:utf-8-*-
# 函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，
# 因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。
# 而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，
# 因此，这种函数是有副作用的。

# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

#将一个函数赋值给变量


f=abs

#函数名也是变量

# 可以对函数名赋值


# abs=10

#赋值后  abs就变成普通变量了
# abs(-10)

#把函数当做参数传入函数


def add(x,y,f):
	return f(x)+f(y)

print(add(10,-20,abs))

#Python内建函数  map

def fun1(x):
	return x*x

list2=[1,2,3,4,5,6,7,8]

f=map(fun1,list2)

print(list(f))


# 将lsit2中元素全部转成str
print(list(map(str,list2)))


#reduce


#使用reduce对序列求和
from functools import reduce
list3=[1,2,3,4,5,6]
def f(x,y):
	return x+y

res=reduce(f,list3)
#Python内置函数sum求和

res3=sum(list3)

#等价于  f(f(f(f(f(1,2),3),4),5),6)
res2=f(f(f(f(f(1,2),3),4),5),6)
print(res)
print(res2)
print(res3)

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

list4=['adam', 'LISA', 'barT']
def normalize(name):
    return name.capitalize()
print(list(map(normalize,list4)))

#编写求和函数
def prodTemp(x,y):
	return x+y
def prod(L):
	return reduce(prodTemp,L)

print(prod([1,2,3,4,5,6]))


#1.str--->int
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		L= {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
		return L[s]

# reduce(fn,map(char2num,s))
# 等价于
# map(char2num,s),将字符串转成数字的map
# reduce将数字的map组成int
	return reduce(fn,map(char2num,s))


#1.str--->float
def str2float(s):
	L1=s.split('.')
	print(L1)
	l=str2int(L1[0])
	r=str2int(L1[1])
	return l+r/pow(10,len(L1[1]))
res=str2float("253245.34123")
print(type(res))
print(res)





























