import numpy as np

x = ['快递太慢了！','不好吃','特别难吃','要齁死我了','很划算','下次还来','味道很不错！','香']
y = ['差评','差评','差评','差评','好评','好评','好评','好评']

def shuffle(x,y):
    x_array = np.array(x)
    y_array = np.array(y)
    permutation = np.random.permutation(x_array.shape[0])
    x = x_array[permutation]
    y = y_array[permutation]
    return x,y

x, y = shuffle(x, y)

for i,j in zip(x,y):
    print(i,':',j)
