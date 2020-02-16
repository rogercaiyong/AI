import numpy as np

x = ['快递太慢了！','不好吃','特别难吃','要齁死我了','很划算','下次还来','味道很不错！','香']
y = ['差评','差评','差评','差评','好评','好评','好评','好评']

def shuffle(x,y):
    x_array = np.array(x)
    y_array = np.array(y)
    print(x_array)
    print(y_array)
    permutation = np.random.permutation(x_array.shape[0])
    print(permutation)
    a = x_array[permutation]
    b = y_array[permutation]
    print(a)
    print(b)
    return a,b

shuffle(x, y)

for i,j in zip(a,b):
    print(i,':',j)
