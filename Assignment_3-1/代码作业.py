#解法一
import numpy as np
from math import sqrt

x_raw = [[1, 1], [0.4, 5.2], [-2.8, -1.1], [3.2, 1.4], [-1.3, 3.2], [-3, 3.1]]
y_raw = [2, 1, 2, 1, 1, 2]
x_train = np.array(x_raw)
y_train = np.array(y_raw)

x_test = [[-2.6, 6.6], [1.4, 1.6], [-2.5, 1.2]]

for i in x_test:
    dis = []
    for j in x_train:
        dis.append(sqrt(np.sum((i - j) ** 2)))
    sort = np.argsort(dis)
    print([y_train[i] for i in sort[:1]])
    


#解法二
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

x_raw = [[1, 1], [0.4, 5.2], [-2.8, -1.1], [3.2, 1.4], [-1.3, 3.2], [-3, 3.1]]
y_raw = [2, 1, 2, 1, 1, 2]
x_train = np.array(x_raw)
y_train = np.array(y_raw)

x_test1 = np.array([-2.6, 6.6])
x_test2 = np.array([1.4, 1.6])
x_test3 = np.array([-2.5, 1.2])

kNN_classifier = KNeighborsClassifier(n_neighbors=1)
kNN_classifier.fit(x_train,y_train )
x_test1 = x_test1.reshape(1,-1)
x_test2 = x_test2.reshape(1,-1)
x_test3 = x_test3.reshape(1,-1)

print(kNN_classifier.predict(x_test1))
print(kNN_classifier.predict(x_test2))
print(kNN_classifier.predict(x_test3))
