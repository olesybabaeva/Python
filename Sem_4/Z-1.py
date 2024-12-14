#Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3], [5, 6, 7]]
print(matrix)

t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(t_matrix)