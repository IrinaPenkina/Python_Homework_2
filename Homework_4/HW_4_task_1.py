'''
Задача 1 Напишите функцию для транспонирования матрицы.
'''

def print_matrix(matr):
    for row in matr:
        print(' '.join(map(str, row)))

def trans_matrix(matr):
    trans_matr = [[matr[i][j] for i in range(len(matr))] for j in range(len(matr[0]))]
    return(trans_matr)


matrix = [[1, 7, 5, 3],
          [2, 6, 8, 10]]
print('Исходная матрица:\n')
print_matrix(matrix)
print(' ')
print('Транспонированная матрица:\n')
print_matrix(trans_matrix(matrix))
