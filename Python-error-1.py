#-*-coding:utf-8-*-

'''异常处理'''

import logging

def main():
	try:
		print('try...')
		r = 10 / 1
		print('result:', r)
	except ZeroDivisionError as e:
		print('except:', e)
		logging.exception(e)
	except ValueError as e2:
		print('except:', e2)
	else:
		#只有没有错误的时候才会走else
		print("no error")
	finally:
		print('finally...')
		print('END')

	print('END-----------------')

	# Python所有的错误都是从BaseException类派生的
	# BaseException可以捕获所有异常
	# 

if __name__ == '__main__':
	main()

