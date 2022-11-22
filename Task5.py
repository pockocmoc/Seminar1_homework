# Напишите программу,
# которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

print('Программа принимает на вход координаты двух точек,\n'
      'и находит расстояние между ними в 2D пространстве.')
print('A')
x1 = int(input('x = '))
y1 = int(input('y = '))
print('B')
x2 = int(input('x1 = '))
y2 = int(input('y1 = '))

a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(format(a, '.2f'))

