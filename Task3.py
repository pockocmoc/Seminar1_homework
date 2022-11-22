# Напишите программу,
# которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Программа принимает на вход координаты точки (X и Y),'
      '\nпричём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,'
      '\nв которой находится эта точка')
x = int(input('X = '))
y = int(input('Y = '))

if x == 0 and y == 0:
    print('Ошибка!!! X и Y не должны равняться нулю.')
elif x > 0 and y > 0:
    print('Номер четверти: 1')
elif x < 0 and y > 0:
    print('Номер четверти: 2')
elif x < 0 and y < 0:
    print('Номер четверти: 3')
elif x > 0 and y < 0:
    print('Номер четверти: 4')
