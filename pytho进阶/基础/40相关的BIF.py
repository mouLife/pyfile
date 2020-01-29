#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   40相关的BIF.py    
@Contact :   moulelin@163.com
@License :   (C)Copyright 2019 Moule
@Modify Time      @Author  
------------      -------    
2020/1/29 9:30   MouleLin
'''
class A:
    pass
class B(A):
    def __init__(self,x):
        self.x = 2

print(issubclass(B,A)) # 检查 A是不是B的子类
# isinstance() 是否属于实例对象
# hasattr 是否包含属性
bb = B(2)
print(hasattr(bb,'x')) # bb对象包含x这个属性
print(getattr(bb,'x'))
print(getattr(bb,'y','属性不存在'))
setattr(bb,'x',3)
print(bb.x)
# delattr
# property
class C:
    def __init__(self,size):
        self.size = size 
    def getSize(self):
        return  self.size
    def setSize(self,size):
        self.size = size
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)# property 第一个参数是获取属性的方法，
    # 第二个是设置属性的方法，第三个是删除属性的方法
c = C(1)
print(c.x) # 获取属性
c.x = 2# 设置属性
print(c.x)
del c.x # 删除属性



 
