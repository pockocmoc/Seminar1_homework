# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"


print('Введите значение предикат.')
x = int(input('X = '))
y = int(input('Y = '))
z = int(input('Z = '))

left = not (x or y or z)
right = not x and not y and not z
result = left == right

if result == True:
    print('Утверждение истинно.')
else:
    print('Утверждение ложно.')
