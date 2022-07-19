# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input())
lst = []
for i in range(k, -1, -1):
    a = random.randrange(0, 100)
    if a != 0:
        if i == 0:
            lst.append(f'{a}')
        elif i == 1:
            lst.append(f'{a} * x')
        else:
            lst.append(f'{a} * x ** {i}')
print(lst)


with open('file_task4.txt', 'w') as file:
    for i in range(len(lst)):
        if i != len(lst) - 1:
            file.write(f'{lst[i]} + ')
        else:
            file.write(f'{lst[i]} = 0')
