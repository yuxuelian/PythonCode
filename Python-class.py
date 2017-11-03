#-*-coding:utf-8-*-

class A(object):
	def __init__(self,height):
		print("-----A初始化------")
		self.height=height

	def test1(self):
		print("访问继承的方法")

class Hello(A):

	# def __new__(self):
	# 	return object.__new__();

	def __init__(self,name,age,height):
		A.__init__(self,height)
		self.name=name

		#私有属性
		self.__age=age

	def getAge(self):
		#通过get方法访问私有属性
		return self.__age;

	def __str__(self):
		return "%s的年龄是%d"%(self.name,self.__age)


def fn():
	pass



def main():
	'''main方法'''
	h=Hello("波爷",22,180)
	print(h)
	print(h.name)

	#访问继承的属性
	print(h.height)

	h.test1()

	#这样仍然可以访问私有属性
	print(h._Hello__age)

	print(h.getAge())

	#判断对象是否是指定的类的对象
	# print(isinstance(h,Hello))
	# print(isinstance([],list))
	# print(isinstance((),tuple))
	# print(isinstance({},dict))
	# print(isinstance("",str))
	# print(isinstance(None,object))
	# print(isinstance(1,int))
	# print(isinstance(1.0,float))

	#得到对象的类型
	# print(type(1.0))
	# print(type(1))
	# print(type([]))
	# print(type(()))
	# print(type({}))
	# print(type(""))
	# print(type(None))
	# print(type(h))

	#判断对象是否是一个函数
	# fun=lambla

	import types
	fn=lambda x,y:x*y

	# fn指向函数
	# print(type(fn))
	#指向类
	# print(type(Hello))

	# 是否是一个函数
	# print(type(fn)==types.FunctionType)

	#获取对象的所有属性和方法
	# print(dir(1))
	# print(dir(h))

	#读对象的属性
	def readName(fp):
		if hasattr(fp, 'name'):
		    return getattr(fp,"name")
		return None
	#写对象属性
	def writeName(fp,new_name):
		if hasattr(fp, 'name'):
		    setattr(fp,"name",new_name)

	writeName(h,"王开波")
	print(readName(h))



if __name__ == '__main__':
	main()

