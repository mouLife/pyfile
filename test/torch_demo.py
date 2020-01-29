from torch.autograd import Variable
import torch


tensor = torch.FloatTensor([[1,2],[3,4]])  # tensor不能反向传播
variable = Variable(tensor, requires_grad = True)   # variable是可以反向传播的

print(tensor)
print(variable)

t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)

print(tensor)
print(variable)
v_out.backward()
print(variable.grad)  # 1/4*sum(var*var)  梯度 1/4*2*var
print(variable.data.numpy())