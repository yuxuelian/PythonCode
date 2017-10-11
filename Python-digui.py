#-*-coding:utf-8-*-

#递归调用  计算1-n的阶乘



def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

print(fact(5))

# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120

#当数值过大会出现堆栈溢出

#解决办法

#看着很高端,这个其实就是个循环
def fact_iter(n,product):
	if n==1:
		return product
	return fact_iter(n-1,n*product)

def fact(n):
	return fact_iter(n,1)

print(fact(200))

# ===> fact_iter(5, 1)         第一次调用
# ===> fact_iter(4, 5*1)
# ===> fact_iter(3, 4*5)
# ===> fact_iter(2, 3*20)
# ===> fact_iter(1, 2*60)
# ===> 120


# 遗憾的是，大多数编程语言没有针对尾递归做优化，
# Python解释器也没有做优化，所以，
# 即使把上面的fact(n)函数改成尾递归方式，
# 也会导致栈溢出。






