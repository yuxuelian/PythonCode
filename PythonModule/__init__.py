# D:/Program Files/Python
#-*-coding:utf-8-*-

' 模块的第一行是文档注释 '

# 作者
__author__ = 'base'


def test():
    args = sys.argv
    if len(args)==1:
        print('module---init')
    elif len(args)==2:
        print('module---init, %s!' % args[1])
    else:
        print('module---init    Too many arguments!')


if __name__=='__main__':
    test()
















