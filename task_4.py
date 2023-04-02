# Задание 4.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод init()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 22
# 37 43
# 51 86
#
# 3 5 32
# 2 4 6
# -1 64 -8
#
# 3 5 8 3
# 8 3 7 1
#
# Следующий шаг — реализовать перегрузку метода str()
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом
# первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join(
            [' '.join([str(i) for i in row]) for row in self.data]) + '\n'

    def __add__(self, other):
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
