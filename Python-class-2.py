#-*-coding:utf-8-*-

'''
动态绑定类的属性方法
'''

class Student(object):
	"""docstring for Student"""

	# 限制允许的属性名
	# __slots__ = ('name', 'age','sum','score') # 用tuple定义允许绑定的属性名称

	# def __new__(slef):
	# 	super(Student,self).__new__()

	def __init__(self):
		super(Student, self).__init__()

	#将方法编程属性
	@property
	def score(self):
		return self.__score

	#设置属性
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self.__score = value

	@property
	def birth(self):
		return self.__birth

	@birth.setter
	def birth(self, value):
		self.__birth = value

	@property
	def age(self):
		return 2015 - self.__birth


def main():
	s=Student()
	#给对象绑定属性
	s.name="王开波"
	# s.age=22
	#给对象绑定方法
	s.sum=lambda x,y:x+y

	s.birth=2001
	s.score=99
	print("分数是:%d"%s.score)

	print("名字是:%s"%s.name)

	# age是只读,没有setter方法
	# s.age=10
	print("年龄是:%d"%s.age)

	#调用方法
	# print(s.sum(1,10))


	#这样的绑定方式对s2是无效的
	s2=Student()

	#成员方法,必须要有self参数
	# def sum(self,a,b):
	# 	return a*b
	# 但是可以给class绑定方法,这样就都起作用了
	Student.sum=lambda self,x,y:x*y

	# 通常情况下，上面的sum方法可以直接定义在class中，
	# 但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

	# print(s2.sum(2,20))

	


if __name__ == '__main__':
	main()