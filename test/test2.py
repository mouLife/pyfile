#coding:utf-8
# a = input("请输入")
# if int(a)>=123 or int(a)<=140:
#     print(a)
# elif int(a)>145:
#     print(int(a)+123)

# for i in range(0,5):
#     print("hello world%s"%i)
a = ['a','b','c']
for i in a:
    print(i)
    for j in a:
        print(j)
import numpy as np
d = [np.random.rand(10,x) for x in range(10)]
#十行一列，十行两列，，，
print(d)