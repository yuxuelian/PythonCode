#-*-coding:utf-8-*-



'''同步读取文件'''


def main():
	try:
		f=open("TestText.txt",'r')
		#读取一个字符,文件指针向下移一个位置
		s=f.read(1)
		print(s)
		s=f.read(1)
		print(s)
		s=f.read(1)
		print(s)
		s=f.read()
		print(s)
	except Exception as e:
		print(e)
	finally:
		if f:
			#f不为空,关闭
			f.close()

if __name__ == '__main__':
	main()
