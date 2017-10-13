#-*-coding:utf-8-*-

#Python内建的filter()函数用于过滤序列。



#利用filter函数过滤列表   删掉偶数  保留奇数


def isJish(x):
	if x%2==1:
		return True
	else:
		return False

list1=list(filter(isJish,[1,2,3,4,5,6,7,8,10]))
print(list1)


#筛选1000以内的素数
def _list():
	n=1
	while True:
		n=n+1
		yield n

def _not_divisible(n):
	return lambda x:x%n>0

def primes():
	yield 2
	it=_list()
	while True:
		n=next(it)
		yield n
		it=filter(_not_divisible(n),it)

# for n in primes():
# 	if n<1000:
# 		print(n)
# 	else:
# 		break


#回数
def is_palindrome(x):
	s=str(x)
	if s==s[-1::-1]:
		return True
	else:
		return False

output = filter(is_palindrome, range(1, 1000))
print(list(output))
















