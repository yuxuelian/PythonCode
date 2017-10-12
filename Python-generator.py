#-*-coding:utf=8-*-
#生成器  generator

'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。
'''

# 生成器与生成式的区别在于
# 生成式  []   生成器  ()


L=[x*x for x in range(10)]
print(L)

g=(x*x for x in range(10))

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for temp in g:
	print(temp)

# 得到斐波拉切数列 
# 1,1,2,3,5,8,13,21,34


def fib(max):
	a,b,n=0,1,0

	m=(0,1,0)
	a=m[0]
	b=m[1]
	n=m[2]

	while n<max:
		# print(b)
		yield b
		# a,b = b,a+b
		t = (b, a + b) # t是一个tuple
		a = t[0]
		b = t[1]
		n+=1
	return 'done'

f=fib(10)

# for temp in f:
# 	print(temp)


while True:
	try:
		x=next(f)
		print(x)
	except StopIteration as e:
		print(e.value)
		break


#打印杨辉三角

def triangles(max):
	L=[1]
	n=1
	while n<=max:
		k=0
		L1=[]
		while k<n:
			if k==0:
				L1.append(1)
			elif k==n-1:
				L1.append(1)
			else:
				L1.append(L[k-1]+L[k])
			k+=1
		n+=1
		L=L1
		yield L

g=triangles(10)
for temp in g:
	print(temp)











