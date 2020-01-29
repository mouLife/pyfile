g = lambda x:x*2+1
print(g(2))
f = lambda x,y : x+y
print(f(1,2))
def odd(x):
    return x%2
temp = range(10)
show = filter(odd,temp)
print(list(show))
print(list(filter(lambda x:x%2,range(10))))
print(list(map(lambda x:x+2,range(10)))) #map函数，将每个可迭代的序列放入函数中进行运算

