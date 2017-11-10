#-*-coding:utf-8-*-

'''操作文件和目录'''

import os

def main():
	print(os.name)
	# print(os.uname())
	# 获取环境变量
	print(os.environ)
	print(type(os.environ))
	#获取PATH环境变量
	print(os.environ.get('PATH'))
	#查看当前目录绝对路径  .  表示当前路径
	print(os.path.abspath(''))

	#拼接目录
	sDir=os.path.join("D:\\a\\2",'testDir')
	print(sDir)
	#删除目录
	# os.rmdir(sDir)
	#创建目录
	# os.mkdir(sDir)

	#拆分目录
	# print(os.path.split(sDir))
	# 
	
	#得到扩展名
	# print(os.path.splitext("C:\\Users\\Administrator\\Desktop\\新建文本文档 (2).txt"))

	#重命名
	# print(os.rename("C:\\Users\\Administrator\\Desktop\\新建文本文档 (2).txt","aaa.txt"))

	#删除文件
	# os.remove('aaa.txt')
	

	#列出当前目录下的所有文件  if os.path.isdir(x)  判断是否是目录
	# print([x for x in os.listdir('.')])
	# 列出当前目录下的所有py文件  os.path.isfile(x)  是否是文件  os.path.splitext(x)[1]=='.py'是否是以.py结尾
	print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


if __name__ == '__main__':
	main()
