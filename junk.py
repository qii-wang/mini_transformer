import torch
m = torch.nn.Softmax(dim=2)
input = torch.randn(2, 3,4)
output = m(input)
print(input,"\n", output)
