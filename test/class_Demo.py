class Animals:
    def breath(self):
        print("%s"%"asdasdasd")
    def move(self):
        print("move")
    def eat(self):
        print("eat")
    pass


class Manmals(Animals):
    def breastfeed(self):
        print("feed")
    pass


class Cats(Manmals):
    def __init__(self,spots):
        self.spots = spots
    def cat_mouse(self):
        print("catch")
    def dance(self):
        self.cat_mouse()
        self.breath()
    pass

kitty = Cats(10)

print(kitty.spots)
kitty.dance()
import pickle
data = {1:"data1",2:"data2"}
save_file = open("save.txt",'wb')
pickle.dump(data,save_file)
save_file.close()

load_file = open("save.dat","rb")
load = pickle.load(load_file)
print(load)
load_file.close()