# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
lst = [1, 5, 6, 4, 2, 5, 3, 6, 2, 5, 7]
dictionary = {}
lst_result = []
for i in lst:
    if i in dictionary.keys():
        dictionary[i] += 1
    else:
        dictionary[i] = 1

for i in dictionary.keys():
    if dictionary[i] == 1:
        lst_result.append(i)
print(lst_result)
