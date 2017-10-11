#-*-coding:utf-8-*-
#调用函数
print("调用函数")
print(abs(-1))
print(max(1,2,3,41,123,11,1))


#数据类型转换
print('数据类型转换')
print(int('123'))
print(float('123.124'))

print('定义函数')

def my_abs(x):
	if x>=0:
		return x
	else:
		return -x

print(my_abs(-2))

def power(x):
	return x*x

print(power(9))


#计算幂次,
#默认参数必须在后面
def power(x,n=2):
	s=1
	while n>0:
		s=s*x
		n-=1
	return s

print(power(5,10))

#默认参数
print('默认参数')
print(power(19))

#默认参数的坑
def add_end(L=[]):
	L.append("end")
	return L

print(add_end())
print(add_end())
print(add_end())
print(add_end())

# ['end']
# ['end', 'end']
# ['end', 'end', 'end']
# ['end', 'end', 'end', 'end']
# 出现这种结果的原因:
# Python函数在定义的时候，
# 默认参数L的值就被计算出来了，
# 即[]，因为默认参数L也是一个变量，
# 它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，
# 默认参数的内容就变了，
# 不再是函数定义时的[]了
# 修改
def add_end(L=None):
	if L is None:
		L=[]
	L.append("end")
	return L
print(add_end())
print(add_end())
print(add_end())
print(add_end())


#可变参数
#可变参数允许你传入0个或任意个参数，
#这些可变参数在函数调用时自动组装为一个tuple
print("可变参数")

def calc(*numbers):
	sum=0
	for n in numbers:
		sum+=n*n
	return sum

print(calc(1,2,3,10))

list11=[2,1,11,11,34]
#list整体传入
print(calc(*list11))

#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，
#这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

person("王开波",12)


person("王开波",12,city="济南")

person("王开波",12,city="济南",job="Android",monay=12312)
#或者这样调用
extra={'city': '济南', 'job': 'Android', 'monay': 12312}
person("王开波",12,**extra)



def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

#关键字参数  **extra  直接传入  dict 调用
extra={'city': '济南', 'job': 'Android', 'monay': 12312}
person("王开波",12,**extra)


# 命名关键字参数
#只能传入 city,job的key
def person(name,age,*,city,job):
	print(name,age,city,job)

#city="济南",job="Python"  必须按这样   传入参数名   否则调用会报错
person("wangkaibo",24,city="济南",job="Python")

#如果函数定义中已经有了一个可变参数，
#后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
#例如   args已经是一个可变参数了   后面不需要再加个  *
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

#city="济南",job="Python"  必须按这样   传入参数名   否则调用会报错
person("wangkaibo",24,123,35445,"hello world",city="济南",job="Python")

# city='beijing'可以设置默认值   调用的时候可以不用再传入 city="济南"
def person(name, age, *args, city='beijing', job):
    print(name, age, args, city, job)

#使用命名关键字参数时，要特别注意，如果没有可变参数，
#就必须加一个*作为特殊分隔符。如果缺少*，
#Python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass
#在Python中定义函数，
#可以用
#1.必选参数、
#2.默认参数、
#3.可变参数、
#4.关键字参数
#5.命名关键字参数
#参数定义的顺序必须是：
#必选参数、
#默认参数、
#可变参数、
#命名关键字参数
#关键字参数

#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。


