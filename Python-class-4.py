#-*-coding:utf-8-*-

'''定制类'''

class CustomClass(object):
	"""docstring for CustomClass"""
	def __init__(self, name):
		super(CustomClass, self).__init__()
		self.name = name
		self.a=1
		self.b=1

	def __str__(self):
		return 'Student object (name=%s)' % self.name
	
	def __repr__ (self):
		return 'Student object (name=%s)' % self.name
	# __repr__ = __str__
	# 
	# 如果一个类想被用于for ... in循环，类似list或tuple那样
	
	def __iter__(self):
		#返回一个进行迭代的对象
		return self 

	#迭代的时候会不停的调用__next__
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b # 计算下一个值

		if self.a > 100000: # 退出循环的条件
			raise StopIteration()

		return self.a # 返回下一个值

from enum import Enum, unique

Month = Enum('Month', 
	('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

@unique#帮助检查是否有重复值
class Weekday(Enum):
	'''继承自Enum,这是一个枚举类'''
	Sun = 0 # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

def main():
	c=CustomClass("王开波")
	print(c)
	# for t in c:
	# 	print(t)

	# 遍历Month
	# for name, member in Month.__members__.items():
	# 	print(name, '=>', member, ',', member.value)
	
	# 访问枚举
	print(Weekday.Mon)
	print(Weekday.Mon.value)


if __name__ == '__main__':
	main()