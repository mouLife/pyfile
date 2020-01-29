import torch.nn as nn
import matplotlib.pyplot as plt
import torch
N, D_in, H, D_out = 64, 1000, 100, 10  # 一共有64个数据，每个数据输入10000维度，中间层100个神经元，输出10维
# 随机一些数据

x = torch.randn(N, D_in)  # 输入数据
y = torch.randn(N, D_out)  # 输出数据

class TwoLayerNet(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
        super(TwoLayerNet, self).__init__()  # 继承了父类，就需要初始化一下父类
        self.linear1 = torch.nn.Linear(D_in, H)
        self.linear2 = torch.nn.Linear(H, D_out)

    def forward(self, x):
        x = self.linear1(x)
        x = torch.nn.functional.relu(x)
        x = self.linear2(x)
        return x


model = TwoLayerNet(D_in, H, D_out)

# if torch.cuda.is_available(): 有GPU的话
#     device = torch.device("cuda")          # a CUDA device object
#     y = torch.ones_like(x, device=device)  # directly create a tensor on GPU
#     x = x.to(device)                       # or just use strings ``.to("cuda")``
#     z = x + y
#     print(z)
#     print(z.to("cpu", torch.double))
learning_rate = 1e-6
loss_fn = nn.MSELoss(reduction='sum')
# optimizer = torch.optim.SGD(model.parameters(), lr=0.0001, momentum=0.9)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
plt.ion()
for t in range(500):
    # forward pass
    y_pred = model(x)  # 直接做model.forward()
    loss = loss_fn(y_pred, y)
    #     print(t, loss.item())
    # backward pass
    model.zero_grad()
    loss.backward()
    # gradient
    # update weight of w1
    #     with torch.no_grad():
    #        for param in model.parameters():
    #             param-=learning_rate*param.grad
    optimizer.step()
    if t % 5 == 0:
        plt.cla()
        plt.scatter(y_pred.data.numpy(), y.data.numpy())
        # plt.scatter(x.data.numpy(),y_pred.data.numpy,c='red')
        plt.pause(0.1)
plt.ioff()
plt.show()

