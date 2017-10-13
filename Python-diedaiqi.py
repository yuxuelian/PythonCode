#-*-coding:utf-8-*-


#Python迭代器
'''
可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；
'''

#引包
from collections import Iterable

#判断是否可迭代
isinstance({},Iterable)


# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
from collections import Iterator

isinstance((x for x in range(10)), Iterator)
#True
isinstance([], Iterator)
#False
isinstance({}, Iterator)
#False
isinstance('abc', Iterator)
#False


# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
isinstance(iter([]),Iterator)
#True
isinstance(iter({}),Iterator)
#True
isinstance(iter("String"),Iterator)
#True


#使用Iterator遍历list

list1=[1,2,3,4,5,6]


for x in list1:
	print(x)

#等价于
it=iter(list1)
while True:
	try:
		x=next(it)
		print(x)
	except StopIteration as e:
		print("遍历结束")
		break












