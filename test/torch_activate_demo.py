import torch
import torch.nn.functional as F
from torch.autograd import Variable
import matplotlib.pyplot as plt

x = torch.linspace(-5,5,200)
x = Variable(x)
x_np = x.data.numpy() # matpltlib不支持tensor，所以转为numpy格式
y_relu = F.relu(x).data.numpy()
y_sigmoid = F.sigmoid(x).data.numpy()
y_tanh = torch.sigmoid(x).data.numpy()
y_softplus = F.softplus(x).data.numpy()
plt.figure(1,figsize=(6,8))
plt.subplot(221)
plt.plot(x_np, y_relu,c="red",label = "relu")
plt.ylim((-1,5))
plt.legend(loc = "best")

plt.subplot(222)
plt.plot(x_np, y_sigmoid,c="red",label = "y_sigmoid")
plt.ylim((0,1))
plt.legend(loc = "best")

plt.subplot(223)
plt.plot(x_np, y_tanh,c="red",label = "y_tanh")
plt.ylim((-1,5))
plt.legend(loc = "best")

plt.subplot(224)
plt.plot(x_np, y_softplus,c="red",label = "relu")
plt.ylim((-1,5))
plt.legend(loc = "best")

plt.show()