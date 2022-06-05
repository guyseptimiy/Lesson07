# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, numbers):
        self.__numbers = numbers

    def __str__(self):
        res = ''
        for line in self.__numbers:
            for col in line:
                res += '{0:5.0f}'.format(col)
            res += '\n'
        return res

    def __add__(self, other):
        # копируем
        new_matrix = []
        for line in self.__numbers:
            new_line = []
            for el in line:
                new_line.append(el)
            new_matrix.append(new_line)

        # Складываем
        for str_i in range(0, len(other.__numbers)):
            for col_i in range(0, len(other.__numbers[str_i])):
                new_matrix[str_i][col_i] += other.__numbers[str_i][col_i]

        return Matrix(new_matrix)


M1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(M1)

M2 = Matrix([[10, 20, 30], [40, 50, 60], [3, 2, 1]])
print(M2)

M3 = M1 + M2
print(M3)
