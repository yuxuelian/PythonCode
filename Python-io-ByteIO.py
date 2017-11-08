#-*-coding:utf-8-*-

'''在内存中读写StringIO'''

from io import BytesIO

def main():
	# f=BytesIO()
	# f.write("中文".encode("utf-8"))
	# print(f.getvalue())

	#或者
	f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
	print(f.getvalue())


if __name__ == '__main__':
	main()
