import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt
import torch.nn.functional as F

x = torch.unsqueeze(torch.linspace(-1,1,200),dim=1) # unsequence把一位数据转为2维数据
y = x.pow(2) + 0.2*torch.rand(x.size())
x,y = Variable(x), Variable(y)

# plt.scatter(x.data.numpy(),y.data.numpy())
# plt.show()
class Net(torch.nn.Module):
    def __init__(self,n_features, n_hidden, n_output):
        super(Net,self).__init__()
        self.hidden = torch.nn.Linear(n_features,n_hidden) # 隐藏层需要输入的特征维数，隐藏层神经元个数
        self.prediction = torch.nn.Linear(n_hidden,n_output) # 输入n_hideen个数据，1一个输出


    def forward(self, x): #前向传播
        print(x)
        x = self.hidden(x)
        x = F.relu() # 数据先过一遍hidden，之后经过激活函数
        x = self.prediction(x)
        return x

net = Net(1,10,1)
optimizer = torch.optim.SGD(net.parameters(),lr=0.0001) # 随机梯度下降
loss_func = torch.nn.MSELoss()

for i in range(10):
    predict = net(x)
    optimizer.zero_grad()
    loss = loss_func(predict,y)
    optimizer.step()

    print("------------------------")
