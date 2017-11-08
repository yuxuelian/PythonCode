#-*-coding:utf-8-*-



'''同步读取文件'''


def main():
	# with open("TestText.txt","r") as f:
	# 	print(f.read())
	#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法
	
	#readlines()   一行一行的全部读取进来,并保存在 list   读取配置文件可以使用这种方式
	with open("TestText.txt","r") as f:
		l=f.readlines()
		for line in l:
			print(line.strip())
	

	#读取二进制文件-------以  rb  的方式打开即可
	

	#指定编码的方式读取文件
	with open("TestText2.txt",encoding="gbk") as f:
		print(f.read())


if __name__ == '__main__':
	main()
