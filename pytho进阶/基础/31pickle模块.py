import pickle
a = [1,2,2]
pickle_file = open("E:\\test.pkl",'wb')
pickle.dump(a,pickle_file)
pickle_file.close()
pick_read = open("E:\\test.pkl",'rb+')
my_ = pickle.load(pick_read)
print(my_)
import numpy as np
a = np.array([[1,2,3],[2,22,1]])
a_pickle = open('a.txt','wb')
pickle.dump(a,a_pickle)
a_pickle.close()
