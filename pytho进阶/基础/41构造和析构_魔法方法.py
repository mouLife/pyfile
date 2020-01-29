#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   41构造和析构_魔法方法.py    
@Contact :   moulelin@163.com
@License :   (C)Copyright 2019 Moule
@Modify Time      @Author  
------------      -------    
2020/1/29 11:49   MouleLin     
'''    
# __new__方法 ，继承不可修改的对象的时候，重写这个方法
class CapStr(str):
    def __new__(cls, string):
        '''
        把所有字母转为大写字符
        :param string:
        '''
        string = string.upper()
        return str.__new__(cls,string)
a = CapStr('asd')
print(a)
# __del__析构器 垃圾回收机制调用
class C:
    def __init__(self):
        print('init method')
    def __del__(self):
        print("del method")
c = C()
c2 = c
c3 = c2
del c3
