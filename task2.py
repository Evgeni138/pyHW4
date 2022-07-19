# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple(number):
    if number == 2:
        return True
    else:
        res = True
        for i in range(2, number):
            if number % i == 0:
                res = False
                break
        return res


num = int(input())
lst = []
count = {}
for i in range(2, num):
    if num % i == 0 and simple(i):
        lst.append(i)
lst.reverse()

for i in lst:
    num2 = num
    while num2 % i == 0:
        if i in count.keys():
            count[i] += 1
            num2 /= i
        else:
            count[i] = 1
            num2 /= i

st = ''
for k in count.keys():
    for i in range(count[k]):
        st += f'{k}*'

print(st[:-1])
