# Напишите программу,
# которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
import random
print('Программа по заданному номеру четверти,\n'
      'показывает диапазон возможных координат точек в этой четверти.')
a = int(input('Введите номер четверти: '))
if 1 <= a <= 4:
    if a == 1:
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print(f'x = {x}, y = {y}')
    elif a == 2:
        x = random.randint(-100, -1)
        y = random.randint(1, 100)
        print(f'x = {x}, y = {y}')
    elif a == 3:
        x = random.randint(-100, -1)
        y = random.randint(-100, -1)
        print(f'x = {x}, y = {y}')
    elif a == 4:
        x = random.randint(1, 100)
        y = random.randint(-100, -1)
        print(f'x = {x}, y = {y}')
else:
    print('Ошибка!!! введите число от 1 до 4.')
