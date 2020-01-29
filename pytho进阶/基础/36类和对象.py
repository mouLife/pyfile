class test():
    def __init__(self,name):
        self.name = name
    def setName(self,name):
        self.name  = name
    def play(self):
        print(self.name)

import pickle
test1 = test()
test1.setName("a")
test2 = test()
test2.setName('b')
test1.play()
test2.play()
test_pickle = open("test.plk",'wb')
pickle.dump(test1,test_pickle)
test_pickle.close()
test_load = open('test.plk','rb')
test_ = pickle.load(test_load)
test_.play()
