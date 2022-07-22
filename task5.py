def separation(lst):
    dic = {}
    for elem in lst:
        if elem:
            if '*x^' in elem:
                par = elem.partition('*x^')
                dic[int(par[2])] = int(par[0])
            elif '*x' in elem:
                par = elem.partition('*x')
                dic[1] = int(par[0])
            elif '-x' in elem:
                dic[1] = -1
            elif '+x' in elem:
                dic[1] = 1
            else:
                par = elem.partition(' ')
                dic[0] = int(par[0])
    return dic

with open('file5_1.txt', 'r') as file1:
    equation1 = file1.read()

with open('file5_2.txt', 'r') as file2:
    equation2 = file2.read()

st1 = equation1.replace(' ', '')
st1 = st1.replace('-','+-')
st1 = st1[:-2]
st1 = st1.split('+')

st2 = equation2.replace(' ', '')
st2 = st2.replace('-', '+-')
st2 = st2[:-2]
st2 = st2.split('+')

dic1 = separation(st1)
dic2 = separation(st2)
print(dic1)
print(dic2)

for i in dic1.keys():
    if i in dic2.keys():
        dic1[i] += dic2[i]

for i in dic2.keys():
    if i not in dic1.keys():
        dic1[i] = dic2[i]

print(dic1)
dic1_sorted = dict(sorted(dic1.items(), reverse=True))
print(dic1_sorted)
result = ''
for i in dic1_sorted.keys():
    if i == 1:
        result += (f'{dic1_sorted[i]}*x')
    elif i == 0:
        result += (f'{dic1_sorted[i]}')
    else:
        result += (f'+{dic1_sorted[i]}*x^{i} ')
result = result.replace('+-', '-')
result += ' = 0'
print(result)

with open('file5_3.txt', 'w') as file3:
    file3.write(result)
