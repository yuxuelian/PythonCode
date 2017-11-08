#-*-coding:utf-8-*-

'''在内存中读写StringIO'''

from io import StringIO

def main():
	# f=StringIO()
	# print(f.write("在内存中读写"))
	# print(f.getvalue())
	# 
	f=StringIO("像操作文件一样\n操作内存")
	while  True:
		s=f.readline()
		if s == '':
			break
		print(s.strip())

if __name__ == '__main__':
	main()
