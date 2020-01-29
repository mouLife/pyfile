import numpy as np
# print("hello world")
a = [1,2,3,4,6,7,78]
print(a[-2::-1])
del a[2]
print(a[-2::-1])
a.insert(3,4)
print(a[-2::-1])
b = {1:"lin",2:"mou",3:"le"}
print(b[2])
del b[1]
b[4]="lai"
print(b)