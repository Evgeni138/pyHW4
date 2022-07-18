# Вычислить число pi c заданной точностью d Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import *

d = list(input('Введите d '))
num = pi
count = -1
for i in range(len(d)):
    if d[i] != '.':
        count += 1
print(count)
num = num * 10 ** count // 1 / 10 ** count
print(num)
