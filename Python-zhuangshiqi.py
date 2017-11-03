#-*-coding:utf-8-*-
#装饰器

def now():
	print("2017-10-17")
#函数在Python中也是对象,可以通过 __name__ 属性拿到函数的函数名
print("函数名是:%s"%(now.__name__))


print("-"*50)

def decorator(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@decorator
def now():
    print('2015-3-25')

now()

#通过上面的方式对now函数进行了增强,有点类似java中的装饰者模式
#@decorator   有点类似java中的注解
#因此我们可以向java注解一样   为注解传入参数
def log(text):
    def decorator(func):
        def hahaNow(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return hahaNow
    return decorator

@log("从注解中传入的值")
def now():
    print('2015-3-25')

now()

print("now的名字改变了----->%s"%now.__name__)

#由于函数名发生改变,而有些依赖函数签名的代码执行就会出错
#不需要编写wrapper.__name__ = func.__name__这样的代码
#Python内置的functools.wraps就是干这个事的
import functools
def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log2
def now():
    print('2015-3-25')

now()
print("now的名字改变了----->%s"%now.__name__)


def log3(*args1):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print("start call")
			print(args1)
			temp=func(*args, **kw)
			print("end call")
			return temp
		return wrapper
	return decorator


@log3()
def now():
	print('2015-3-25')

now()




