class Turle:
    def __init__(self,x):
        self.num = x
class Fish:
    def __init__(self,x):
        self.num = x
class Pool:  #  组合。把几个没有关联的类放在一起，如果有相互关系，则用继承
    def __init__(self,x,y):
       self.turle = Turle(x)
       self.fish = Fish(y)
    def print_num(self):
        '''输出函数'''
        print("总共有%d只乌龟，%d只鱼"%(self.turle.num,self.fish.num))
pool = Pool(1,2)
pool.print_num()
print(pool.print_num.__doc__)
