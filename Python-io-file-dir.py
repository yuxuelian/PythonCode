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

	#在某个目录下创建目录
	print(os.path.join("D:/",'testDir'))


if __name__ == '__main__':
	main()
