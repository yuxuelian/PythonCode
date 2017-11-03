# D:/Program Files/Python
# -*- coding: utf-8 -*-

' 模块的第一行是文档注释 '

# 作者
__author__ = 'base'

import sys

def test():
    args = sys.argv
    print(args)
    if len(args)==1:
        print('module---demo')
    elif len(args)==2:
        print('module---demo, %s!' % args[1])
    else:
        print('module---demo  Too many arguments!')


if __name__=='__main__':
    test()