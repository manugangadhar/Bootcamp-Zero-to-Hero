import numpy as np
x = np.array([[2, 3, 4], [2, 3, 16], [2, 3, 8]])
y = np.array([[1, 2, 3], [0, 5, 0], [1, 5, 6]])

i = 0;result = [];element = 0
k = 0
temp = 0
temp_list = []

while i <= (len(x) - 1):
    if k <= (len(y[0]) - 1):
        temp = x[i,:] * y[:,k]
        element = np.sum(temp)
        temp_list.append(element)
        k = k + 1
    else:
        i = i + 1
        k = 0
        result.append(temp_list)
        temp_list = []
print(result)



