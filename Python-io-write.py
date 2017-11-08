#-*-coding:utf-8-*-

'''在内存中读写'''

def main():
	with open("test.txt","w",encoding="utf-8") as f:
		f.write("写文件测试,哈哈哈哈哈");

if __name__ == '__main__':
	main()
