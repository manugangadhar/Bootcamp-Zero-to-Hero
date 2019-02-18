matrix1_row = int(input("enter number of rows for matrix 1"))
matrix1_column = int(input("enter number of columns for matrix 1"))

matrix2_row = int(input("enter number of rows for matrix 2"))
matrix2_column = int(input("enter number of columns for matrix 2"))

matrix1 = []
matrix2 = []
matrix3 = []
result = 0

for i in range(0, matrix1_row):
    temp_list = []
    temp1 = input("Enter row values for matrix1")
    for j in temp1.split():
        temp_list.append(int(j))
    matrix1.append(temp_list)

for i in range(0, matrix2_row):
    temp_list = []
    temp1 = input("Enter row values for matrix2")
    for j in temp1.split():
        temp_list.append(int(j))
    matrix2.append(temp_list)

i = 0
j = 0
k = 0
for i in range(0, matrix1_row):
    temp = []
    for k in range(0, matrix2_column):
        for j in range(0, matrix1_column):
            result = result + matrix1[i][j] * matrix2[j][k]
        temp.insert(k, result)
        result = 0
    matrix3.append(temp)
print(matrix3)






