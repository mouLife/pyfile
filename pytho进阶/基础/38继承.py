import random
class Parent:
    def __init__(self,x):
        self.x = x
    def hello(self):
        print("这是父类")
class Child(Parent):
    def __init__(self,y,x):
        #Parent.__init__(self,x) # self传入的是子类的对象
        # 这里的self是子类的实例对象，调用未绑定的父类方法,在子类中初始化父类方法，
        # 或者调用super函数
        # 或者使用
        super().__init__(x) #不用给定父类的名字
        self.y = y
    def move(self):
        print(self.y+self.x)
class ChildChild(Parent,Child):
    def __init__(self,x,y):
        super().__init__(x,y)
child = Child(1,2)
child.move()
