#-*-coding:utf-8-*-



#函数作为返回值

# 返回一个求和函数


def getSumFun(*agrs):
	def sum():
		ax=0
		for n in agrs:
			ax+=n
		return ax
	return sum


#返回一个求和函数,但是暂时不调用他
res=getSumFun(1,2,3,4,5,6)

#调用这个求和函数 拿到结果
print(res())






























