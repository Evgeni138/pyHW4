# Вычислить число pi c заданной точностью d Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import *

d = list(input('Введите d '))
count = -1
# ВЫчисление числа Пи методом ряда Нилаканта
veracity = 200000
p = 3
c = 2
for i in range(2, veracity):
    p += (-1) ** i * 4 / (c * (c + 1) * (c + 2))
    c += 2

for i in range(len(d)):
    if d[i] != '.':
        count += 1
p = p * 10 ** count // 1 / 10 ** count
print(p)
