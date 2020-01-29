class test:
    __priname = 'a' # 前面加两个下划线就是私有的
    def __init__(self,name): #构造函数
        self.name = name
    def play(self):
        print(self.name)
    def print_name(self):
        print(self.__priname)
test1 = test("a")
test1.play()
# print(test1.__priname) ,私有属性，无法调用
test1.print_name() # 从内部方法进行引用
print(test1._test__priname) # 对象._类名__变量名 也能访问


