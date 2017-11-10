#-*-coding:utf-8-*-

'''序列化    反序列化'''


import pickle

def main():
	d = dict(name='Bob', age=20, score=88)
	# print(pickle.dumps(d))

	#打开一个读的二进制文件,不存在就创建
	# f=open('dump.txt','wb')
	# #序列化,并写入文件
	# pickle.dump(d,f)
	# f.close()
	
	#反序列化
	#以只读打开二进制文件
	f=open("dump.txt",'rb')
	#反序列化
	d=pickle.load(f)
	#关闭文件
	f.close()
	#输出
	print(d)

if __name__ == '__main__':
	main()
